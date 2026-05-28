import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. 修改 Pydantic 模型中的字段名为 kpa
class PredictionInput(BaseModel):
    cellulose_content: float
    hemicellulose_content: float
    lignin_content: float
    particles: float
    ash_content: float
    extract_content: float
    kpa: float  # 这里从 pka 改为 kpa
    acid_concentration: float
    acid_time: float
    temp_steam_explosion: float
    time_steam_explosion: float
    reactor_volume: float
    prediction_type: str  # 新增预测类型字段

# 加载所有5种预测模型
models = {}
try:
    # 确保模型文件路径正确
    models['glucose'] = joblib.load("S_xgboost_model_glucose.pkl")
    models['xylose'] = joblib.load("S_svr_model_xylose.pkl")
    models['furfural'] = joblib.load("S_xgboost_model_furfural.pkl")
    models['HMF'] = joblib.load("S_xgboost_model_HMF.pkl")
    models['acetic'] = joblib.load("S_xgboost_model_acetic.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    models = {}

@app.post("/api/prediction")
async def predict(data: PredictionInput):
    # 验证预测类型
    if data.prediction_type not in models:
        raise HTTPException(status_code=400, detail="Invalid prediction type")
    
    if not models:
        raise HTTPException(status_code=500, detail="Models not found")
    
    try:
        # 2. 构造 DataFrame，列名必须完全对应训练时的 'kpa'
        # 注意：这里的 Key 必须与你模型训练时的特征名称（Column Name）完全一致
        features = pd.DataFrame([{
            'Cellulose content': data.cellulose_content,
            'Hemicellulose content': data.hemicellulose_content,
            'Lignin content': data.lignin_content,
            'particles': data.particles,
            'Ash content': data.ash_content,
            'extract content': data.extract_content,
            'kpa': data.kpa, 
            'acid concentration': data.acid_concentration,
            'acid time': data.acid_time,
            'temperature for steam explosion': data.temp_steam_explosion,
            'time for steam explosion': data.time_steam_explosion,
            'reactor volume for steam explosion': data.reactor_volume
        }])

        # 使用对应类型的模型进行预测
        prediction = models[data.prediction_type].predict(features)
        
        return {
            "predictionValue": float(prediction[0]),
            "status": "success",
            "predictionType": data.prediction_type
        }
    except Exception as e:
        # 如果报错，返回详细的错误信息（方便调试特征名对不对）
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)