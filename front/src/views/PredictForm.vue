<template>
  <div class="predict-container">
    <el-card :header="`生物质转化模型预测输入 (${predictionTypeNames[formData.prediction_type]}预测)`">
      <el-form :model="formData" label-width="160px" label-position="left">
        
        <!-- 预测类型选择 -->
        <el-divider content-position="left">预测类型</el-divider>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="选择预测类型">
              <el-select v-model="formData.prediction_type" placeholder="请选择预测类型">
                <el-option 
                  v-for="(name, type) in predictionTypeNames" 
                  :key="type" 
                  :label="name" 
                  :value="type" 
                />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        
        <el-divider content-position="left">原料组分含量 (%)</el-divider>
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="纤维素 (%wt/wt)">
              <el-input-number v-model="formData.cellulose_content" :precision="2" :step="0.1" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="半纤维素 (%wt/wt)">
              <el-input-number v-model="formData.hemicellulose_content" :precision="2" :step="0.1" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="木质素 (%wt/wt)">
              <el-input-number v-model="formData.lignin_content" :precision="2" :step="0.1" />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="灰分 (%wt/wt)">
              <el-input-number v-model="formData.ash_content" :precision="2" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="提取物 (%wt/wt)">
              <el-input-number v-model="formData.extract_content" :precision="2" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="颗粒度 (mm)">
              <el-input-number v-model="formData.particles" :precision="2" />
            </el-form-item>
          </el-col>
        </el-row>

        <el-divider content-position="left">物理化学性质</el-divider>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="pka (酸)">
              <el-input-number v-model="formData.kpa" :precision="4" :step="0.1" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="反应器体积 (L)">
              <el-input-number v-model="formData.reactor_volume" :precision="2" />
            </el-form-item>
          </el-col>
        </el-row>

        <el-divider content-position="left">预处理条件</el-divider>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="酸浓度 (%wt/wt)">
              <el-input-number v-model="formData.acid_concentration" :step="0.01" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="浸酸时间 (min)">
              <el-input-number v-model="formData.acid_time" />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="汽爆温度 (℃)">
              <el-input-number v-model="formData.temp_steam_explosion" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="汽爆时间 (min)">
              <el-input-number v-model="formData.time_steam_explosion" />
            </el-form-item>
          </el-col>
        </el-row>

        <div style="margin-top: 20px; text-align: center;">
          <el-button type="primary" size="large" @click="handlePredict" :loading="loading">
            开始预测
          </el-button>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { predictBiomass } from '../api/prediction';
import { predictionTypeNames } from '../types/prediction';
import type { PredictionType } from '../types/prediction';

const router = useRouter();
const loading = ref(false);

// 13 个参数对应的初始值，确保字段名与后端 PredictionInput 严格一致
const formData = reactive({
  cellulose_content: 29.39,
  hemicellulose_content: 25.58,
  lignin_content: 16.49,
  particles: 28.74,
  ash_content: 3.90,
  extract_content: 16.44,
  kpa: -2.6047,
  acid_concentration: 0.96,
  acid_time: 909.07,
  temp_steam_explosion: 190.88,
  time_steam_explosion: 12.10,
  reactor_volume: 2.01,
  prediction_type: 'glucose' as PredictionType
});

const handlePredict = async () => {
  loading.value = true;
  try {
    const response = await predictBiomass(formData);
    // 假设后端返回 { predictionValue: 20.13, status: 'success', predictionType: 'glucose' }
    const resultValue = response.data.predictionValue; 
    const predictionType = response.data.predictionType;
    
    router.push({
      name: 'Result',
      query: { 
        result: resultValue,
        predictionType: predictionType
      }
    });
  } catch (error) {
    console.error('预测失败', error);
  } finally {
    loading.value = false;
  }
};
</script>