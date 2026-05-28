<template>
  <div class="result-container">
    <el-card shadow="hover" style="max-width: 600px; margin: 50px auto; text-align: center;">
      <el-result
        icon="success"
        title="预测完成"
        :sub-title="`基于 XGBoost 模型的${predictionTypeName}计算结果`"
      >
        <template #extra>
          <div class="result-display">
            <!-- 使用 el-statistic 展示核心数值 -->
            <el-statistic 
              :title="`${predictionTypeName}预测含量 (%wt/wt)`" 
              :value="predictionValue" 
              :precision="3"
            />
          </div>

          <div style="margin-top: 40px">
            <el-button type="primary" @click="$router.push('/')">重新预测</el-button>
            <el-button @click="$router.back()">返回修改</el-button>
          </div>
        </template>
      </el-result>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { computed } from 'vue';
import { predictionTypeNames } from '../types/prediction';
import type { PredictionType } from '../types/prediction';

const route = useRoute();

/**
 * 注意：
 * 在上一步 handlePredict 中，你使用了 router.push({ name: 'Result', query: { result: data.predictionValue, predictionType: data.predictionType } })
 * 所以这里通过 route.query.result 和 route.query.predictionType 获取
 */
const predictionValue = computed(() => {
  const val = route.query.result || route.query.predictionValue;
  return Number(val) || 0;
});

const predictionType = computed(() => {
  const type = route.query.predictionType as PredictionType;
  return type in predictionTypeNames ? type : 'glucose';
});

const predictionTypeName = computed(() => {
  return predictionTypeNames[predictionType.value];
});
</script>

<style scoped>
.result-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 80vh;
}

.result-display {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #ebeef5;
  display: inline-block;
  min-width: 200px;
}

:deep(.el-statistic__content) {
  color: #409eff;
  font-size: 28px;
  font-weight: bold;
}
</style>