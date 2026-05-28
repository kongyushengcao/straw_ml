// 预测类型枚举
export type PredictionType = 'glucose' | 'xylose' | 'furfural' | 'HMF' | 'acetic';

// 预测类型显示名称映射
export const predictionTypeNames: Record<PredictionType, string> = {
  glucose: '葡萄糖 (Glucose)',
  xylose: '木糖 (Xylose)',
  furfural: '糠醛 (Furfural)',
  HMF: '羟甲基糠醛 (HMF)',
  acetic: '乙酸 (Acetic Acid)'
};

// 修改 PredictionInput 为 13 参数版本（包含预测类型）
export interface PredictionInput {
  cellulose_content: number;
  hemicellulose_content: number;
  lignin_content: number;
  particles: number;
  ash_content: number;
  extract_content: number;
  kpa: number;
  acid_concentration: number;
  acid_time: number;
  temp_steam_explosion: number;
  time_steam_explosion: number;
  reactor_volume: number;
  prediction_type: PredictionType;
}

// 修改输出结果的定义
export interface PredictionOutput {
  predictionValue: number;
  status: string;
  predictionType: PredictionType;
}

// 如果你有一个统一的响应包装类
export interface ApiResponse<T> {
  data: T;
  message?: string;
  status?: string;
}