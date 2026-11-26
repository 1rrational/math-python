import numpy as np
import matplotlib.pyplot as plt

# 初始参数
S0 = 100       # 初始股价100
mu = 0.05      # 预期收益率 5%
sigma = 0.2    # 波动率 20%
T = 1.0        # 时间 1年
N = 252        # 一年有252个交易日
dt = T / N     # 每天的时间步长

# 核心魔法：生成 252 个标准正态分布的随机数
Z = np.random.standard_normal(N)

# 几何布朗运动公式（概率论）
daily_returns = np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
price_path = S0 * np.cumprod(daily_returns)

# 画图
plt.plot(price_path, color='blue')
plt.title("Simulated Stock Price")
plt.xlabel("Trading Days")
plt.ylabel("Price")
plt.show()