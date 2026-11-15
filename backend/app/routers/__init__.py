"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import seedling as router_seedling
from app.routers import planting as router_planting
from app.routers import irrigation as router_irrigation
from app.routers import fertilizer as router_fertilizer
from app.routers import pest as router_pest
from app.routers import task as router_task
from app.routers import harvest as router_harvest
from app.routers import sorting as router_sorting
from app.routers import packaging as router_packaging
from app.routers import input as router_input
from app.routers import greenhouse as router_greenhouse
from app.routers import soil as router_soil
from app.routers import certification as router_certification
from app.routers import safety as router_safety
from app.routers import worker as router_worker
from app.routers import trace as router_trace
from app.routers import market as router_market
from app.routers import weather as router_weather

ROUTERS = [router_seedling, router_planting, router_irrigation, router_fertilizer, router_pest, router_task, router_harvest, router_sorting, router_packaging, router_input, router_greenhouse, router_soil, router_certification, router_safety, router_worker, router_trace, router_market, router_weather]
