<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">高山生态农场种植全流程管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向高山有机蔬菜、林果与菌菇的育种育苗、定植管护、农事派工、采收分拣与投入品台账的一体化农场生产管理系统。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "育苗管理", path: "/seedling" }, { label: "定植管理", path: "/planting" }, { label: "灌溉排涝", path: "/irrigation" }, { label: "施肥管理", path: "/fertilizer" }, { label: "植保防治", path: "/pest" }, { label: "农事派工", path: "/task" }, { label: "采收管理", path: "/harvest" }, { label: "分拣分级", path: "/sorting" }, { label: "包装出厂", path: "/packaging" }, { label: "投入品台账", path: "/input" }, { label: "设施大棚", path: "/greenhouse" }, { label: "土壤检测", path: "/soil" }, { label: "有机认证", path: "/certification" }, { label: "农残检测", path: "/safety" }, { label: "劳力管理", path: "/worker" }, { label: "产品溯源", path: "/trace" }, { label: "销售对接", path: "/market" }, { label: "气象监测", path: "/weather" }]
</script>
