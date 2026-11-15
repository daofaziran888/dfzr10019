"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class SeedlingEntry(BaseModel):
    """育苗批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 作物品种
    field_2: str | None = None  # 育苗盘数
    field_3: str | None = None  # 播种日期
    field_4: str | None = None  # 出苗率
    field_5: str | None = None  # 苗龄天数
    field_6: str | None = None  # 管护人员
    field_7: str | None = None  # 批次状态

class PlantingEntry(BaseModel):
    """种植地块明细结构。"""

    field_0: str | None = None  # 地块编号
    field_1: str | None = None  # 地块名称
    field_2: str | None = None  # 面积亩数
    field_3: str | None = None  # 土壤类型
    field_4: str | None = None  # 前茬作物
    field_5: str | None = None  # 定植日期
    field_6: str | None = None  # 种植密度
    field_7: str | None = None  # 地块状态

class IrrigationEntry(BaseModel):
    """灌溉计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 覆盖地块
    field_2: str | None = None  # 灌溉方式
    field_3: str | None = None  # 计划水量
    field_4: str | None = None  # 执行时段
    field_5: str | None = None  # 水源类型
    field_6: str | None = None  # 执行人员
    field_7: str | None = None  # 执行状态

class FertilizerEntry(BaseModel):
    """施肥记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 覆盖地块
    field_2: str | None = None  # 肥料名称
    field_3: str | None = None  # 肥料类型
    field_4: str | None = None  # 施用方式
    field_5: str | None = None  # 施用量
    field_6: str | None = None  # 操作人员
    field_7: str | None = None  # 记录状态

class PestEntry(BaseModel):
    """病虫害记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 发生地块
    field_2: str | None = None  # 病虫种类
    field_3: str | None = None  # 危害程度
    field_4: str | None = None  # 防治措施
    field_5: str | None = None  # 用药名称
    field_6: str | None = None  # 防治日期
    field_7: str | None = None  # 记录状态

class TaskEntry(BaseModel):
    """农事任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 任务类型
    field_2: str | None = None  # 执行地块
    field_3: str | None = None  # 指派人员
    field_4: str | None = None  # 计划工时
    field_5: str | None = None  # 计划日期
    field_6: str | None = None  # 完成情况
    field_7: str | None = None  # 任务状态

class HarvestEntry(BaseModel):
    """采收批次明细结构。"""

    field_0: str | None = None  # 采收编号
    field_1: str | None = None  # 作物品种
    field_2: str | None = None  # 采收地块
    field_3: str | None = None  # 采收日期
    field_4: str | None = None  # 采收数量
    field_5: str | None = None  # 品质等级
    field_6: str | None = None  # 采收人员
    field_7: str | None = None  # 批次状态

class SortingEntry(BaseModel):
    """分拣单明细结构。"""

    field_0: str | None = None  # 分拣单号
    field_1: str | None = None  # 关联采收
    field_2: str | None = None  # 分拣线号
    field_3: str | None = None  # 分拣日期
    field_4: str | None = None  # 一级品数量
    field_5: str | None = None  # 二级品数量
    field_6: str | None = None  # 次品数量
    field_7: str | None = None  # 分拣状态

class PackagingEntry(BaseModel):
    """包装单明细结构。"""

    field_0: str | None = None  # 包装单号
    field_1: str | None = None  # 关联分拣
    field_2: str | None = None  # 包装规格
    field_3: str | None = None  # 包装数量
    field_4: str | None = None  # 包装日期
    field_5: str | None = None  # 出厂检验
    field_6: str | None = None  # 运输方式
    field_7: str | None = None  # 包装状态

class InputEntry(BaseModel):
    """投入品明细结构。"""

    field_0: str | None = None  # 物品编号
    field_1: str | None = None  # 物品名称
    field_2: str | None = None  # 物品类别
    field_3: str | None = None  # 供应商名称
    field_4: str | None = None  # 采购日期
    field_5: str | None = None  # 采购数量
    field_6: str | None = None  # 使用地块
    field_7: str | None = None  # 当前余量

class GreenhouseEntry(BaseModel):
    """温室大棚明细结构。"""

    field_0: str | None = None  # 大棚编号
    field_1: str | None = None  # 大棚名称
    field_2: str | None = None  # 覆盖面积
    field_3: str | None = None  # 覆盖材料
    field_4: str | None = None  # 温控设备
    field_5: str | None = None  # 建成日期
    field_6: str | None = None  # 当前种植
    field_7: str | None = None  # 大棚状态

class SoilEntry(BaseModel):
    """检测样本明细结构。"""

    field_0: str | None = None  # 样本编号
    field_1: str | None = None  # 采样地块
    field_2: str | None = None  # 采样日期
    field_3: str | None = None  # pH值
    field_4: str | None = None  # 有机质含量
    field_5: str | None = None  # 氮磷钾指标
    field_6: str | None = None  # 检测人员
    field_7: str | None = None  # 检测状态

class CertificationEntry(BaseModel):
    """认证项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 认证类型
    field_2: str | None = None  # 认证机构
    field_3: str | None = None  # 覆盖地块
    field_4: str | None = None  # 申请日期
    field_5: str | None = None  # 审核日期
    field_6: str | None = None  # 有效期限
    field_7: str | None = None  # 认证状态

class SafetyEntry(BaseModel):
    """检测批次明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 检测对象
    field_2: str | None = None  # 检测项目
    field_3: str | None = None  # 送样日期
    field_4: str | None = None  # 检测方法
    field_5: str | None = None  # 限量标准
    field_6: str | None = None  # 检测结果
    field_7: str | None = None  # 检测状态

class WorkerEntry(BaseModel):
    """农场工人明细结构。"""

    field_0: str | None = None  # 工人编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 工种
    field_3: str | None = None  # 技能等级
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 进场日期
    field_6: str | None = None  # 日薪标准
    field_7: str | None = None  # 在岗状态

class TraceEntry(BaseModel):
    """溯源档案明细结构。"""

    field_0: str | None = None  # 档案编号
    field_1: str | None = None  # 产品批次
    field_2: str | None = None  # 溯源起点
    field_3: str | None = None  # 溯源终点
    field_4: str | None = None  # 投入品记录
    field_5: str | None = None  # 农事记录
    field_6: str | None = None  # 检测记录
    field_7: str | None = None  # 档案状态

class MarketEntry(BaseModel):
    """销售批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 客户名称
    field_2: str | None = None  # 产品品种
    field_3: str | None = None  # 批次数量
    field_4: str | None = None  # 单价
    field_5: str | None = None  # 交付日期
    field_6: str | None = None  # 物流方式
    field_7: str | None = None  # 批次状态

class WeatherEntry(BaseModel):
    """气象记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 监测站点
    field_2: str | None = None  # 记录日期
    field_3: str | None = None  # 最高气温
    field_4: str | None = None  # 最低气温
    field_5: str | None = None  # 降水量
    field_6: str | None = None  # 日照时长
    field_7: str | None = None  # 霜冻预警
