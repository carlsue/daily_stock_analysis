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
    mood_index_code="SPX",
    news_queries=[
        "美股 大盘",
        "US stock market",
        "S&P 500 NASDAQ",
    ],
    prompt_index_hint="""
    角色设定： “你是有 20 年经验的华尔街宏观策略分析师。”
    任务拆解： 
    1. 提取今日关键宏观数据（预期值 vs 前值）。 
    2. 汇总隔夜/盘前重大公司新闻。 
    3. 分析深度： 不要只罗列新闻，要解释“为什么这很重要”以及“市场情绪可能如何反应”。
    
    格式要求： 
    - 必须包含【今日看点】、【深度解读】、【风险提示】三个板块。
    - **核心指令**：请专门分析 **标普500 (^GSPC)**、**纳斯达克 (^IXIC)**、**道琼斯 (^DJI)** 的走势特点。
    - **禁止事项**：严禁提及 A 股、上证指数或人民币相关数据。仅关注美元资产和美股市场。
    """, # ✅ 这里补上了缺失的逗号
    has_market_stats=False,
    has_sector_rankings=False,
)


def get_profile(region: str) -> MarketProfile:
    """根据 region 返回对应的 MarketProfile"""
    if region == "us":
        return US_PROFILE
    return CN_PROFILE
