import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 连续余弦信号
t = np.arange(0, 10, 0.01)
A = 1
omega = 2 * np.pi
phi = 0
x_continuous = A * np.cos(omega * t + phi)

# 2. 离散单位冲激信号
n = np.arange(-5, 6, 1)
x_discrete = np.zeros_like(n, dtype=float)
x_discrete[n == 0] = 1

plt.figure(figsize=(10, 8))

# 子图1：连续信号
plt.subplot(2, 1, 1)
plt.plot(t, x_continuous, linewidth=1.5, color='blue')
plt.title('连续余弦信号 x(t) = cos(πt)')
plt.xlabel('时间 t (s)')
plt.ylabel('幅值 x(t)')
plt.grid(True, linestyle='--')
plt.ylim(-1.2, 1.2)

# 子图2：离散信号
plt.subplot(2, 1, 2)
plt.stem(n, x_discrete, linefmt='red', markerfmt='ro', basefmt=' ')
plt.title('离散单位冲激信号 δ[n]')
plt.xlabel('离散时间 n')
plt.ylabel('幅值 x[n]')
plt.grid(True, linestyle='--')
plt.ylim(-0.2, 1.2)
plt.xticks(n)

plt.tight_layout()
plt.show()