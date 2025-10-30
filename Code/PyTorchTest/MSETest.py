import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 1. 生成合成数据 ----------------------
np.random.seed(42)
x = np.random.rand(100, 1) * 10  # 生成100个[0,10)范围内的输入
y = 2 * x + 3 + np.random.randn(100, 1) * 1.5  # 线性关系y=2x+3，添加随机噪声

# 转换为PyTorch张量
x_tensor = torch.FloatTensor(x)
y_tensor = torch.FloatTensor(y)

# ---------------------- 2. 定义回归模型 ----------------------
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 输入维度1，输出维度1的线性层
    
    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

# ---------------------- 3. 定义损失函数和优化器 ----------------------
criterion = nn.MSELoss()  # 均方误差损失（MSE Loss）
optimizer = optim.Adam(model.parameters(), lr=0.01)  # Adam优化器

# ---------------------- 4. 训练模型 ----------------------
epochs = 100
losses = []

for epoch in range(epochs):
    # 前向传播
    y_pred = model(x_tensor)
    # 计算损失
    loss = criterion(y_pred, y_tensor)
    losses.append(loss.item())
    
    # 反向传播与优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# ---------------------- 5. 可视化结果 ----------------------
# 绘制训练损失曲线
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('Training Loss Curve')

# 绘制预测结果与真实数据对比
plt.subplot(1, 2, 2)
with torch.no_grad():
    y_pred = model(x_tensor)
plt.scatter(x, y, label='True Data')
plt.plot(x, y_pred.numpy(), color='red', label='Predicted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Result')

plt.tight_layout()
plt.show()

# 输出模型学到的参数
print(f'Learned Weight: {model.linear.weight.item():.4f}, Bias: {model.linear.bias.item():.4f}')