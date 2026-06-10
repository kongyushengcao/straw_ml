<template>
  <div class="predict-page">
    <!-- 顶部提示卡片 -->
    <div class="welcome-card">
      <div class="welcome-icon">
        <el-icon :size="36"><TrendCharts /></el-icon>
      </div>
      <div class="welcome-text">
        <h2>模型预测</h2>
        <p>输入原料参数与预处理条件，选择预测目标，即可获得模型计算结果</p>
      </div>
    </div>

    <!-- 预测类型选择卡 -->
    <div class="type-selector">
      <el-radio-group
        v-model="formData.prediction_type"
        size="large"
      >
        <el-radio-button
          v-for="(name, type) in predictionTypeNames"
          :key="type"
          :value="type"
        >
          {{ name }}
        </el-radio-button>
      </el-radio-group>
    </div>

    <!-- 主表单卡片 -->
    <el-card class="form-card" shadow="hover">
      <template #header>
        <div class="card-header">
          <el-icon :size="20"><EditPen /></el-icon>
          <span>输入参数</span>
        </div>
      </template>

      <el-form :model="formData" label-width="200px" label-position="left">
        <!-- 原料组成 -->
        <div class="section-title">
          <el-icon><Box /></el-icon>
          <span>原料组成</span>
        </div>
        <el-row :gutter="24">
          <el-col :span="12">
            <el-form-item label="纤维素 Cellulose">
              <el-input-number
                v-model="formData.cellucose"
                :precision="2"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="半纤维素 Hemicellulose">
              <el-input-number
                v-model="formData.hemicellulose"
                :precision="2"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="24">
          <el-col :span="12">
            <el-form-item label="木质素 Lignin">
              <el-input-number
                v-model="formData.lignin"
                :precision="2"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="灰分 Ash">
              <el-input-number
                v-model="formData.ash"
                :precision="2"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
        </el-row>

        <!-- 预处理条件 -->
        <div class="section-title">
          <el-icon><SetUp /></el-icon>
          <span>预处理条件</span>
        </div>
        <el-row :gutter="24">
          <el-col :span="12">
            <el-form-item label="酸电离程度 (pKa)">
              <el-input-number
                v-model="formData.acid"
                :precision="4"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="酸浓度 Acid conc. (%)">
              <el-input-number
                v-model="formData.concentration"
                :precision="2"
                :step="0.1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="24">
          <el-col :span="12">
            <el-form-item label="酸处理时间 Acid time (min)">
              <el-input-number
                v-model="formData.acid_time"
                :precision="2"
                :step="1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="温度 T (°C)">
              <el-input-number
                v-model="formData.T"
                :precision="2"
                :step="1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="24">
          <el-col :span="12">
            <el-form-item label="处理时间 Time (min)">
              <el-input-number
                v-model="formData.time"
                :precision="2"
                :step="1"
                controls-position="right"
              />
            </el-form-item>
          </el-col>
        </el-row>

        <!-- 酶解条件 — 仅葡萄糖预测时显示 -->
        <transition name="slide-fade">
          <div v-if="formData.prediction_type === 'glucose'" class="enzyme-block">
            <div class="section-title enzyme-section">
              <el-icon><MagicStick /></el-icon>
              <span>酶解条件（葡萄糖预测专属）</span>
            </div>
            <el-row :gutter="24">
              <el-col :span="12">
                <el-form-item label="纤维素酶 (FPU/g)">
                  <el-input-number
                    v-model="formData.cellulase_addition"
                    :precision="2"
                    :step="0.1"
                    controls-position="right"
                  />
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="β-葡萄糖苷酶 (IU/g)">
                  <el-input-number
                    v-model="formData.B_glucosidase_addition"
                    :precision="2"
                    :step="0.1"
                    controls-position="right"
                  />
                </el-form-item>
              </el-col>
            </el-row>

            <el-row :gutter="24">
              <el-col :span="12">
                <el-form-item label="酶解时间 (h)">
                  <el-input-number
                    v-model="formData.hydrolysis_time"
                    :precision="2"
                    :step="1"
                    controls-position="right"
                  />
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="固体负载量 (%)">
                  <el-input-number
                    v-model="formData.solid_load"
                    :precision="2"
                    :step="0.1"
                    controls-position="right"
                  />
                </el-form-item>
              </el-col>
            </el-row>
          </div>
        </transition>

        <!-- 提交按钮 -->
        <div class="submit-area">
          <el-button
            type="primary"
            size="large"
            round
            @click="handlePredict"
            :loading="loading"
            class="submit-btn"
          >
            <el-icon v-if="!loading"><CaretRight /></el-icon>
            <span>{{ loading ? '正在计算...' : '开始预测' }}</span>
          </el-button>
          <p class="submit-hint">点击后将调用后端模型进行计算，结果将在新页面展示</p>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { predictBiomass } from "../api/prediction";
import { predictionTypeNames } from "../types/prediction";
import type { PredictionType } from "../types/prediction";
import {
  TrendCharts,
  EditPen,
  Box,
  SetUp,
  MagicStick,
  CaretRight,
} from "@element-plus/icons-vue";

const router = useRouter();
const loading = ref(false);

const formData = reactive({
  cellucose: 40.0,
  hemicellulose: 25.0,
  lignin: 20.0,
  ash: 5.0,
  acid: -2.6,
  concentration: 1.0,
  acid_time: 30.0,
  T: 190.0,
  time: 10.0,
  cellulase_addition: null as number | null,
  B_glucosidase_addition: null as number | null,
  hydrolysis_time: null as number | null,
  solid_load: null as number | null,
  prediction_type: "cellulose_recovery" as PredictionType,
});

const handlePredict = async () => {
  loading.value = true;
  try {
    const response = await predictBiomass(formData);
    const { predictionValue, predictionType } = response.data;

    router.push({
      name: "Result",
      query: {
        result: predictionValue,
        predictionType,
      },
    });
  } catch (error) {
    console.error("预测失败", error);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.predict-page {
  max-width: 1100px;
  margin: 0 auto;
}

/* ---- Welcome card ---- */
.welcome-card {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px 28px;
  margin-bottom: 24px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}

.welcome-icon {
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e8f4fd, #d4e9fb);
  border-radius: 12px;
  color: #2d6aa0;
  flex-shrink: 0;
}

.welcome-text h2 {
  margin: 0 0 4px;
  font-size: 20px;
  font-weight: 700;
  color: #1a3a5c;
}

.welcome-text p {
  margin: 0;
  font-size: 14px;
  color: #909399;
}

/* ---- Type selector ---- */
.type-selector {
  margin-bottom: 24px;
  display: flex;
  justify-content: center;
}

.type-selector :deep(.el-radio-button__inner) {
  padding: 10px 18px;
  font-size: 14px;
}

/* ---- Form card ---- */
.form-card {
  border-radius: 12px;
  border: none;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
}

.form-card :deep(.el-card__header) {
  background: linear-gradient(135deg, #f8fafc, #eef2f7);
  border-bottom: 1px solid #e8ecf1;
  border-radius: 12px 12px 0 0;
  padding: 16px 24px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  font-weight: 600;
  color: #1a3a5c;
}

.form-card :deep(.el-card__body) {
  padding: 28px 32px;
}

/* ---- Section titles ---- */
.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 28px 0 18px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e8ecf1;
  font-size: 15px;
  font-weight: 600;
  color: #2d6aa0;
}

.section-title:first-child {
  margin-top: 0;
}

.section-title .el-icon {
  color: #409eff;
}

.enzyme-section {
  color: #67c23a;
  border-bottom-color: #e1f3d8;
}

.enzyme-section .el-icon {
  color: #67c23a;
}

/* ---- Input numbers ---- */
:deep(.el-input-number) {
  width: 100%;
}

:deep(.el-form-item__label) {
  font-weight: 500;
  color: #606266;
}

/* ---- Submit area ---- */
.submit-area {
  margin-top: 36px;
  text-align: center;
}

.submit-btn {
  min-width: 200px;
  height: 48px;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #409eff, #2d6aa0);
  border: none;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(45, 106, 160, 0.35);
}

.submit-btn:active {
  transform: translateY(0);
}

.submit-hint {
  margin: 12px 0 0;
  font-size: 12px;
  color: #c0c4cc;
}

/* ---- Slide transition for enzyme section ---- */
.slide-fade-enter-active {
  transition: all 0.4s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.2s ease-in;
}
.slide-fade-enter-from {
  transform: translateY(-10px);
  opacity: 0;
}
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
