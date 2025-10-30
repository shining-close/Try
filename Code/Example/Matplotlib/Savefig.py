import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]

# 创建图表
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='正弦曲线')
plt.title('正弦函数图像')
plt.legend()
plt.grid(alpha=0.3)

# 保存为高分辨率PNG，带透明背景和紧凑布局
plt.savefig(
    'sin_curve.png',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.2,
    transparent=True
)

plt.show()