import { ref, reactive } from "vue";
import type { PredictionInput, PredictionOutput } from "../types/prediction";
import { predictBiomass } from "../api/prediction";
import { ElMessage } from "element-plus";

const results = ref<PredictionOutput | null>(null);
const loading = ref<boolean>(false);

export function usePrediction() {
  const submitPrediction = async (
    formData: PredictionInput
  ): Promise<boolean> => {
    loading.value = true;
    try {
      const response = await predictBiomass(formData);
      if (response.data.status === "success") {
        results.value = response.data;
        return true;
      }
      return false;
    } catch (error) {
      ElMessage.error("模型调用失败，请检查后端连接");
      return false;
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    results,
    submitPrediction,
  };
}
