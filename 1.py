import math

# 参数设置
mu = 3.5  # 真实平均值
sigma_single = math.sqrt(35 / 12)  # 单次掷骰子的标准差
margin = 0.035  # 1% 的范围
z_score = 1  # 对应 68% 置信水平的 Z 值

# 直接计算所需的 n
n_min = (z_score * sigma_single / margin) ** 2

# 输出结果
print(f"最少需要的掷骰子次数: {math.ceil(n_min)}")