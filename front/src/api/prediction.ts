import axios from 'axios';
import type { PredictionInput, PredictionOutput } from '../types/prediction';

const request = axios.create({
  baseURL: 'http://localhost:8000'
});

// 使用泛型，告诉 TS 返回的是 PredictionOutput
export const predictBiomass = (data: PredictionInput) => {
  return request.post<PredictionOutput>('/api/prediction', data);
};