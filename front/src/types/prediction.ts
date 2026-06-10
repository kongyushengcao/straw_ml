export type PredictionType =
  | "cellulose_recovery"
  | "hemicellulose_removal"
  | "glucose"
  | "furfural"
  | "HMF"
  | "acetic_acid";

export const predictionTypeNames: Record<PredictionType, string> = {
  cellulose_recovery: "纤维素回收率 (Cellulose Recovery)",
  hemicellulose_removal: "半纤维素脱除率 (Hemicellulose Removal)",
  glucose: "葡萄糖固相酶解 (Glucose Solid Enzymatic Hydrolysis)",
  furfural: "糠醛 (Furfural)",
  HMF: "羟甲基糠醛 (HMF)",
  acetic_acid: "乙酸 (Acetic Acid)",
};

export interface PredictionInput {
  cellucose: number;
  hemicellulose: number;
  lignin: number;
  ash: number;
  acid: number;
  concentration: number;
  acid_time: number;
  T: number;
  time: number;
  cellulase_addition: number | null;
  B_glucosidase_addition: number | null;
  hydrolysis_time: number | null;
  solid_load: number | null;
  prediction_type: PredictionType;
}

export interface PredictionOutput {
  predictionValue: number;
  status: string;
  predictionType: PredictionType;
}
