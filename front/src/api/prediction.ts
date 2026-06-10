import axios from "axios";
import type { PredictionInput, PredictionOutput } from "../types/prediction";

const request = axios.create({
  baseURL: "http://localhost:8000",
});

export const predictBiomass = (data: PredictionInput) => {
  return request.post<PredictionOutput>("/api/prediction", data);
};
