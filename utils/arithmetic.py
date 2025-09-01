"""
file: utils/arithmetic.py
illustrate: 提供基本四則運算的工具函式
"""


def add(a: float, b: float) -> float:
    """回傳 a + b 的結果"""
    return float(a+b)


def sub(a: float, b: float) -> float:
    """回傳 a - b 的結果"""
    return float(a-b)


def mul(a: float, b: float) -> float:
    """回傳 a * b 的結果"""
    return float(a*b)


def div(a: float, b: float) -> float:
    """
    回傳 a / b 的結果

    Args:
        a: 被除數
        b: 除數，不可為 0

    Raises:
        ValueError: 當 b == 0 時拋出
    """
    if b==0:
        raise ValueError("當 b == 0 時拋出")
    # 安全檢查很重要喔！ 如果 b 是 0
    return float(a/b)