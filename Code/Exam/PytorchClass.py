import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import torch
import torch.nn as nn
import torch.optim as optim

import torch
# 生成特征数据 X：120 个样本，8 个特征
X = torch.randn(200, 4)


w = torch.tensor([[0.8],[0.6],[0.7],[0.5]])
b = torch.tensor([-1.0])
noise = 0.3 * torch.randn(200, 1)
proba = torch.sigmoid(X @ w + b + noise)  # values in (0, 1)
y = (proba > 0.5).float()                 # binary labels (0/1), shape (200,1)

# 打印维度
print("X.shape:", X.shape)
print("y.shape:", y.shape)

class RiskNN(nn.Module):
    def __init__(self):
        super(RiskNN, self).__init__()
        # 输入层（4个神经元）到隐藏层（8个神经元）
        self.layer1 = nn.Linear(in_features=4, out_features=8)
        # 隐藏层（8个神经元）到输出层（1个神经元）
        self.layer2 = nn.Linear(in_features=8, out_features=1)
        # ReLU激活函数（用于隐藏层）
        self.relu = nn.ReLU()
        # Sigmoid激活函数（用于输出层）
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x

# Instantiate the model
model = RiskNN()
criterion = nn.BCELoss()  # Mean Squared Error loss function
optimizer = optim.SGD(model.parameters(), lr=0.05)  # Stochastic Gradient Descent optimizer


# Training the network
losses = []
for epoch in range(15):  # Train for 20 epochs
    # optimizer.zero_grad()  # Zero the gradients
    preds = model(X)  # Forward pass
    loss = criterion(preds, y)  # Compute the loss
    loss.backward()  # Backpropagation
    optimizer.step()  # Update weights
    losses.append(loss.item())  # Record the loss
    # print(f"Epoch {epoch}, Loss: {running_loss/len(trainloader)}")
    print(f"Epoch {epoch:02d} | Loss: {loss:.6f}")

'''
for epoch in range(1, 16):
    # 计算预测
    preds = model(X)
    # 计算损失
    loss = criterion(preds, y)
    # 零梯度
    optimizer.zero_grad()
    # 反向传播
    loss.backward()
    # 逐步优化
    optimizer.step()
    # 打印每个纪元的损失，格式：纪元 01：损失=0.6931
    print(f"纪元 {epoch:02d}：损失={loss.item():.4f}")
'''

# Plotting the training loss over time
plt.plot(losses)
plt.title('Training Loss Over Time')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()