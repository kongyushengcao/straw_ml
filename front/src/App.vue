<template>
  <el-config-provider>
    <div class="app-wrapper">
      <el-header class="app-header">
        <div class="header-content">
          <div class="header-left">
            <el-icon :size="28" class="header-icon"><Monitor /></el-icon>
            <div class="header-text">
              <span class="header-title">生物质预处理预测系统</span>
              <span class="header-subtitle">Biomass Pretreatment ML Predictor</span>
            </div>
          </div>
          <div class="header-right">
            <el-tag type="info" effect="dark" round>6 个预测目标</el-tag>
          </div>
        </div>
      </el-header>

      <el-main class="main-content">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>

      <el-footer class="app-footer">
        <div class="footer-line"></div>
        <p>&copy; 2026 机器学习模型预测系统 &middot; 南京工业大学</p>
      </el-footer>
    </div>
  </el-config-provider>
</template>

<script setup lang="ts">
import { Monitor } from "@element-plus/icons-vue";
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 50%, #f0f2f5 100%);
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", Arial, sans-serif;
  min-height: 100vh;
}

.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* ---- Header ---- */
.app-header {
  background: linear-gradient(135deg, #1a3a5c 0%, #2d6aa0 100%);
  color: white;
  height: 72px;
  padding: 0 28px;
  display: flex;
  align-items: center;
  box-shadow: 0 4px 20px rgba(26, 58, 92, 0.25);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.header-icon {
  opacity: 0.85;
}

.header-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.header-title {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: 1px;
}

.header-subtitle {
  font-size: 12px;
  font-weight: 400;
  opacity: 0.7;
  letter-spacing: 0.5px;
}

/* ---- Main ---- */
.main-content {
  flex: 1;
  width: 92%;
  max-width: 1280px;
  margin: 32px auto;
  padding: 0;
}

/* ---- Footer ---- */
.app-footer {
  text-align: center;
  padding: 0 0 24px;
}

.footer-line {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, #c0c4cc, transparent);
  margin: 0 auto 16px;
}

.app-footer p {
  margin: 0;
  color: #909399;
  font-size: 13px;
}

/* ---- Page transition ---- */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
