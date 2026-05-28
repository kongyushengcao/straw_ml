<template>
  <el-config-provider>
    <div class="app-wrapper">
      <!-- 顶部导航栏（可选） -->
      <el-header class="header">
        <div class="logo">Biomass ML Predictor</div>
      </el-header>

      <!-- 路由出口：PredictForm 和 PredictResult 会渲染在这里 -->
      <el-main class="main-content">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
      
      <el-footer class="footer">
        © 2026 机器学习模型预测系统 - 核心算法驱动 南京工业大学
      </el-footer>
    </div>
  </el-config-provider>
</template>

<style>
/* 全局样式自定义 */
body {
  margin: 0;
  padding: 0;
  background-color: #f5f7fa; /* 淡淡的底色让卡片更突出 */
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', Arial, sans-serif;
}

.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background-color: #409eff;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
  font-size: 1.5rem;
  font-weight: bold;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.main-content {
  flex: 1;
  padding: 40px auto;
  max-width: 1000px;
  width: 90%;
  margin: 20px auto;
}

.footer {
  text-align: center;
  color: #909399;
  font-size: 12px;
  padding: 20px 0;
}

/* 页面切换动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>