# -*- coding: utf-8 -*-
"""
大盘复盘市场区域配置

定义各市场区域的指数、新闻搜索词、Prompt 提示等元数据，
供 MarketAnalyzer 按 region 切换 A 股/美股复盘行为。
"""

from dataclasses import dataclass
from typing import List


@dataclass
class MarketProfile:
    """大盘复盘市场区域配置"""

    region: str  # "cn" | "us"
    # 用于判断整体走势的指数代码，cn 用上证 000001，us 用标普 SPX
    mood_index_code: str
    # 新闻搜索关键词
    news_queries: List[str]
    # 指数点评 Prompt 提示语
    prompt_index_hint: str
    # 市场概况是否包含涨跌家数、涨停跌停（A 股有，美股无）
    has_market_stats: bool
    # 市场概况是否包含板块涨跌（A 股有，美股暂无）
    has_sector_rankings: bool


CN_PROFILE = MarketProfile(
    region="cn",
    mood_index_code="000001",
    news_queries=[
        "A股 大盘 复盘",
        "股市 行情 分析",
        "A股 市场 热点 板块",
    ],
    prompt_index_hint="分析上证、深证、创业板等各指数走势特点",
    has_market_stats=True,
    has_sector_rankings=True,
)

US_PROFILE = MarketProfile(
    region="us",
    mood_index_code="GSPC",
    news_queries=[
        "美股 盘前",
        "pre-market trading",
        "overnight news US stocks",
        "Asian markets impact US",
        "Federal Reserve overnight",
        "earnings after hours",
        "economic data today",
    ],
    prompt_index_hint="""
    任务要求：
    1. 生成【美股盘前内参】报告，包含以下 6 个核心部分
    2. **每部分必须插入 1-2 张关联性强的配图**（图表、K线、热力图等）
    3. 分析要简洁有力，直接指导当日交易决策

    报告结构（每部分配图要求）：

    📊 【一、隔夜市场回顾】
    - 配图1：标普500、纳斯达克、道指隔夜走势对比图
    - 配图2：亚洲市场（日经、恒生）对美股影响示意图
    - 内容：美股期货表现、欧洲市场收盘、亚洲市场影响

    📰 【二、隔夜要闻速递】
    - 配图1：新闻热点词云图
    - 配图2：重大事件时间轴图
    - 内容：美联储动态、公司财报、地缘政治、经济数据

    📈 【三、宏观数据前瞻】
    - 配图1：今日经济数据日历表
    - 配图2：关键指标预期值对比图（如CPI、非农）
    - 内容：今日待公布数据、预期影响、历史对比

    🔥 【四、板块资金流向】
    - 配图1：板块涨跌幅热力图
    - 配图2：资金流入流出柱状图
    - 内容：领涨板块、领跌板块、资金偏好分析

    🎯 【五、个股重点关注】
    - 配图1：重点个股技术分析图（K线+均线）
    - 配图2：期权异动监控图
    - 内容：盘前异动股、财报股、新闻驱动股

    ⚠️ 【六、风险提示】
    - 配图1：波动率指数（VIX）趋势图
    - 配图2：风险等级雷达图
    - 内容：技术面风险、消息面风险、操作建议

    格式要求：
    - 标题：【美股盘前内参】YYYY-MM-DD
    - 每部分用 emoji 标识，清晰分隔
    - 配图说明要简洁，直接关联分析内容
    - 禁止提及 A 股、港股等非美股市场
    """, # ✅ 这里补上了缺失的逗号
    has_market_stats=False,
    has_sector_rankings=False,
)


def get_profile(region: str) -> MarketProfile:
    """根据 region 返回对应的 MarketProfile"""
    if region == "us":
        return US_PROFILE
    return CN_PROFILE
