import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Seedling = () => import('@/views/seedling/index.vue')
const Planting = () => import('@/views/planting/index.vue')
const Irrigation = () => import('@/views/irrigation/index.vue')
const Fertilizer = () => import('@/views/fertilizer/index.vue')
const Pest = () => import('@/views/pest/index.vue')
const Task = () => import('@/views/task/index.vue')
const Harvest = () => import('@/views/harvest/index.vue')
const Sorting = () => import('@/views/sorting/index.vue')
const Packaging = () => import('@/views/packaging/index.vue')
const Input = () => import('@/views/input/index.vue')
const Greenhouse = () => import('@/views/greenhouse/index.vue')
const Soil = () => import('@/views/soil/index.vue')
const Certification = () => import('@/views/certification/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Worker = () => import('@/views/worker/index.vue')
const Trace = () => import('@/views/trace/index.vue')
const Market = () => import('@/views/market/index.vue')
const Weather = () => import('@/views/weather/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/seedling', name: 'seedling', component: Seedling },
    { path: '/planting', name: 'planting', component: Planting },
    { path: '/irrigation', name: 'irrigation', component: Irrigation },
    { path: '/fertilizer', name: 'fertilizer', component: Fertilizer },
    { path: '/pest', name: 'pest', component: Pest },
    { path: '/task', name: 'task', component: Task },
    { path: '/harvest', name: 'harvest', component: Harvest },
    { path: '/sorting', name: 'sorting', component: Sorting },
    { path: '/packaging', name: 'packaging', component: Packaging },
    { path: '/input', name: 'input', component: Input },
    { path: '/greenhouse', name: 'greenhouse', component: Greenhouse },
    { path: '/soil', name: 'soil', component: Soil },
    { path: '/certification', name: 'certification', component: Certification },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/worker', name: 'worker', component: Worker },
    { path: '/trace', name: 'trace', component: Trace },
    { path: '/market', name: 'market', component: Market },
    { path: '/weather', name: 'weather', component: Weather },
  ],
})

export default router
