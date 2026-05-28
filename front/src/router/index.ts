import { createRouter, createWebHistory } from 'vue-router';
import PredictForm from '../views/PredictForm.vue';
import PredictResult from '../views/PredictResult.vue';

const routes = [
  { path: '/', component: PredictForm },
  { path: '/result', name: 'Result', component: PredictResult, props: true }
];

export const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;