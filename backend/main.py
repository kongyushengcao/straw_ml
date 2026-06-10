import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionInput(BaseModel):
    cellucose: float
    hemicellulose: float
    lignin: float
    ash: float
    acid: float
    concentration: float
    acid_time: float
    T: float
    time: float
    # Enzyme features — only used for glucose prediction
    cellulase_addition: Optional[float] = None
    B_glucosidase_addition: Optional[float] = None
    hydrolysis_time: Optional[float] = None
    solid_load: Optional[float] = None
    prediction_type: str


MODEL_FILES = {
    "cellulose_recovery":    "best_model_cellulose_retention.pkl",
    "hemicellulose_removal": "best_model_hemicellulose_removal.pkl",
    "glucose":               "best_model_glucose_solid_enzymatic_hydrolysis.pkl",
    "furfural":              "best_model_furfural.pkl",
    "HMF":                   "best_model_HMF.pkl",
    "acetic_acid":           "best_model_acetic_acid.pkl",
}

BASE_FEATURES = ["cellucose", "hemicellulose", "lignin", "ash",
                 "acid", "concentration", "acid_time", "T", "time"]
ENZYME_FEATURES = ["cellulase_addition", "B_glucosidase_addition",
                   "hydrolysis_time", "solid_load"]

models = {}
for pred_type, filename in MODEL_FILES.items():
    try:
        models[pred_type] = joblib.load(filename)
        print(f"Loaded {pred_type} from {filename}")
    except Exception as e:
        print(f"Failed to load {pred_type}: {e}")

if not models:
    raise RuntimeError("No models loaded — check pkl files in backend directory.")


@app.post("/api/prediction")
async def predict(data: PredictionInput):
    if data.prediction_type not in models:
        raise HTTPException(status_code=400, detail=f"Unknown prediction type: {data.prediction_type}")

    row = {feat: getattr(data, feat) for feat in BASE_FEATURES}

    if data.prediction_type == "glucose":
        for feat in ENZYME_FEATURES:
            val = getattr(data, feat)
            if val is None:
                raise HTTPException(status_code=400, detail=f"{feat} is required for glucose prediction")
            row[feat] = val

    features = pd.DataFrame([row])

    try:
        prediction = models[data.prediction_type].predict(features)
        return {
            "predictionValue": float(prediction[0]),
            "status": "success",
            "predictionType": data.prediction_type,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
