import { ref, reactive } from 'vue';
import type { PredictionInput, PredictionOutput } from '../types/prediction';
import { predictBiomass } from '../api/prediction';
import { ElMessage } from 'element-plus';

// 定义在函数外，实现数据在页面跳转时不丢失
const results = ref<PredictionOutput | null>(null);
const loading = ref<boolean>(false);

const formData = reactive<PredictionInput>({
  cellulose: 40.0,
  hemicellulose: 25.0,
  lignin: 20.0,
  acidConcentration: 1.5,
  soakingTime: 12.0,
  steamexploTemp: 180,
  steamexploTime: 5.0
});

export function usePrediction() {
  const submitPrediction = async (): Promise<boolean> => {
    loading.value = true;
    try {
      const response = await predictBiomass(formData);
      if (response.data.code === 200) {
        results.value = response.data.data;
        return true;
      }
      return false;
    } catch (error) {
      ElMessage.error('模型调用失败，请检查后端连接');
      return false;
    } finally {
      loading.value = false;
    }
  };

  return {
    formData,
    loading,
    results,
    submitPrediction
  };
}