# 高山生态农场种植全流程管理平台

面向高山有机蔬菜、林果与菌菇的育种育苗、定植管护、农事派工、采收分拣与投入品台账的一体化农场生产管理系统。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 育苗管理 | `seedling` | 育苗批次 | 批次编号、作物品种、育苗盘数 |
| 定植管理 | `planting` | 种植地块 | 地块编号、地块名称、面积亩数 |
| 灌溉排涝 | `irrigation` | 灌溉计划 | 计划编号、覆盖地块、灌溉方式 |
| 施肥管理 | `fertilizer` | 施肥记录 | 记录编号、覆盖地块、肥料名称 |
| 植保防治 | `pest` | 病虫害记录 | 记录编号、发生地块、病虫种类 |
| 农事派工 | `task` | 农事任务 | 任务编号、任务类型、执行地块 |
| 采收管理 | `harvest` | 采收批次 | 采收编号、作物品种、采收地块 |
| 分拣分级 | `sorting` | 分拣单 | 分拣单号、关联采收、分拣线号 |
| 包装出厂 | `packaging` | 包装单 | 包装单号、关联分拣、包装规格 |
| 投入品台账 | `input` | 投入品 | 物品编号、物品名称、物品类别 |
| 设施大棚 | `greenhouse` | 温室大棚 | 大棚编号、大棚名称、覆盖面积 |
| 土壤检测 | `soil` | 检测样本 | 样本编号、采样地块、采样日期 |
| 有机认证 | `certification` | 认证项目 | 项目编号、认证类型、认证机构 |
| 农残检测 | `safety` | 检测批次 | 检测编号、检测对象、检测项目 |
| 劳力管理 | `worker` | 农场工人 | 工人编号、姓名、工种 |
| 产品溯源 | `trace` | 溯源档案 | 档案编号、产品批次、溯源起点 |
| 销售对接 | `market` | 销售批次 | 批次编号、客户名称、产品品种 |
| 气象监测 | `weather` | 气象记录 | 记录编号、监测站点、记录日期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
