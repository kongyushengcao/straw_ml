<template>
  <div class="result-page">
    <div class="result-card">
      <!-- 成功标记 -->
      <div class="result-icon-wrap">
        <div class="result-icon">
          <el-icon :size="40"><CircleCheckFilled /></el-icon>
        </div>
      </div>

      <h2 class="result-title">预测完成</h2>
      <p class="result-subtitle">基于 {{ modelLabel }} 模型的 {{ predictionTypeName }} 计算结果</p>

      <!-- 数值展示 -->
      <div class="result-value-box">
        <span class="result-label">{{ predictionTypeName }}</span>
        <span class="result-number">{{ formattedValue }}</span>
        <span class="result-unit">{{ unit }}</span>
      </div>

      <!-- 模型信息 -->
      <div class="model-info">
        <div class="info-item">
          <el-icon><Cpu /></el-icon>
          <span>模型：{{ modelLabel }}</span>
        </div>
        <div class="info-item">
          <el-icon><DataLine /></el-icon>
          <span>R² (CV)：{{ r2 }}</span>
        </div>
      </div>

      <!-- 操作按钮 -->
      <div class="result-actions">
        <el-button type="primary" size="large" round @click="$router.push('/')">
          <el-icon><RefreshLeft /></el-icon>
          <span>重新预测</span>
        </el-button>
        <el-button size="large" round @click="$router.back()">
          <el-icon><Back /></el-icon>
          <span>返回修改</span>
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router";
import { computed } from "vue";
import { predictionTypeNames } from "../types/prediction";
import type { PredictionType } from "../types/prediction";
import {
  CircleCheckFilled,
  Cpu,
  DataLine,
  RefreshLeft,
  Back,
} from "@element-plus/icons-vue";

const route = useRoute();

const MODEL_META: Record<string, { label: string; r2: string }> = {
  cellulose_recovery:    { label: "Random Forest", r2: "0.8725" },
  hemicellulose_removal: { label: "XGBoost",       r2: "0.9048" },
  glucose:               { label: "XGBoost",       r2: "0.8407" },
  furfural:              { label: "XGBoost",       r2: "0.8371" },
  HMF:                   { label: "XGBoost",       r2: "0.8227" },
  acetic_acid:           { label: "XGBoost",       r2: "0.8445" },
};

const UNITS: Record<string, string> = {
  cellulose_recovery:    "%",
  hemicellulose_removal: "%",
  glucose:               "%",
  furfural:              "%",
  HMF:                   "%",
  acetic_acid:           "g/L",
};

const predictionValue = computed(() => {
  const val = route.query.result;
  return Number(val) || 0;
});

const formattedValue = computed(() => {
  return predictionValue.value.toFixed(3);
});

const predictionType = computed(() => {
  const type = route.query.predictionType as PredictionType;
  return type in predictionTypeNames ? type : "cellulose_recovery";
});

const predictionTypeName = computed(() => {
  return predictionTypeNames[predictionType.value];
});

const modelLabel = computed(() => {
  return MODEL_META[predictionType.value]?.label ?? "ML";
});

const r2 = computed(() => {
  return MODEL_META[predictionType.value]?.r2 ?? "-";
});

const unit = computed(() => {
  return UNITS[predictionType.value] ?? "%";
});
</script>

<style scoped>
.result-page {
  max-width: 560px;
  margin: 0 auto;
}

.result-card {
  background: white;
  border-radius: 16px;
  padding: 48px 40px 40px;
  text-align: center;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
}

/* ---- Icon ---- */
.result-icon-wrap {
  margin-bottom: 20px;
}

.result-icon {
  width: 72px;
  height: 72px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e1f3d8, #c6f0b8);
  border-radius: 50%;
  color: #67c23a;
  animation: pop-in 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes pop-in {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  60% {
    transform: scale(1.15);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.result-title {
  margin: 0 0 6px;
  font-size: 24px;
  font-weight: 700;
  color: #1a3a5c;
}

.result-subtitle {
  margin: 0 0 32px;
  font-size: 14px;
  color: #909399;
}

/* ---- Value box ---- */
.result-value-box {
  background: linear-gradient(135deg, #f8fafc, #eef2f7);
  border-radius: 12px;
  padding: 28px 24px;
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.result-label {
  font-size: 14px;
  color: #909399;
  font-weight: 500;
}

.result-number {
  font-size: 48px;
  font-weight: 800;
  color: #2d6aa0;
  letter-spacing: -1px;
  line-height: 1.2;
}

.result-unit {
  font-size: 16px;
  color: #606266;
  font-weight: 600;
}

/* ---- Model info ---- */
.model-info {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 36px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #909399;
}

.info-item .el-icon {
  color: #409eff;
}

/* ---- Actions ---- */
.result-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
}
</style>
