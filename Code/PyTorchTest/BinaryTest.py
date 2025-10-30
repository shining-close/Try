import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 1. 生成合成二元分类数据 ----------------------
np.random.seed(42)
# 生成两类数据，分别服从不同的高斯分布
class0 = np.random.normal(loc=2, scale=1, size=(100, 2))
class1 = np.random.normal(loc=5, scale=1, size=(100, 2))
x = np.vstack([class0, class1])
y = np.hstack([np.zeros(100), np.ones(100)]).reshape(-1, 1)  # 二元标签（0和1）

# 转换为PyTorch张量
x_tensor = torch.FloatTensor(x)
y_tensor = torch.FloatTensor(y)

# ---------------------- 2. 定义二元分类模型 ----------------------
class BinaryClassifier(nn.Module):
    def __init__(self):
        super(BinaryClassifier, self).__init__()
        self.layer1 = nn.Linear(2, 16)  # 输入维度2，隐藏层维度16
        self.layer2 = nn.Linear(16, 8)  # 隐藏层维度8
        self.layer3 = nn.Linear(8, 1)   # 输出维度1（用于二元分类的概率）
        self.sigmoid = nn.Sigmoid()     # Sigmoid激活函数，将输出映射到[0,1]
    
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.sigmoid(self.layer3(x))
        return x

model = BinaryClassifier()

# ---------------------- 3. 定义损失函数和优化器 ----------------------
criterion = nn.BCELoss()  # 二元交叉熵损失（适用于单输出+Sigmoid的场景）
optimizer = optim.SGD(model.parameters(), lr=0.01)  # SGD优化器

# ---------------------- 4. 训练模型 ----------------------
epochs = 100
losses = []
accuracies = []

for epoch in range(epochs):
    # 前向传播
    y_pred = model(x_tensor)
    # 计算损失
    loss = criterion(y_pred, y_tensor)
    losses.append(loss.item())
    
    # 计算准确率（预测概率>0.5则视为类别1，否则为类别0）
    predicted = (y_pred > 0.5).float()
    accuracy = (predicted == y_tensor).float().mean()
    accuracies.append(accuracy.item())
    
    # 反向传播与优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}, Accuracy: {accuracy.item():.4f}')

# ---------------------- 5. 可视化结果 ----------------------
# 绘制训练损失和准确率曲线
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('BCELoss')
plt.title('Training Loss Curve')

plt.subplot(1, 2, 2)
plt.plot(accuracies)
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training Accuracy Curve')

plt.tight_layout()
plt.show()

# 绘制分类边界（可选）
plt.figure(figsize=(8, 6))
# 生成网格点用于绘制决策边界
x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))
grid = torch.FloatTensor(np.c_[xx.ravel(), yy.ravel()])

with torch.no_grad():
    z = model(grid).numpy().reshape(xx.shape)

plt.contourf(xx, yy, z, alpha=0.3, levels=[0, 0.5, 1])
plt.scatter(x[y == 0, 0], x[y == 0, 1], label='Class 0')
plt.scatter(x[y == 1, 0], x[y == 1, 1], label='Class 1')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Binary Classification Decision Boundary')
plt.show()