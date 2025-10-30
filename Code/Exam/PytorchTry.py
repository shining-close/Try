import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import torch
import torch.nn as nn
import torch.optim as optim

import torch
# 生成特征数据 X：120 个样本，8 个特征
X = torch.randn(120, 8)
# 定义权重 w (8×1) 和偏置 b
w = torch.randn (8, 1)
b = torch.randn (1) # 标量
# 生成噪声：服从 N (0, 0.5) 的正态分布，形状与 y 一致
noise = torch.normal(mean=0, std=0.5, size=(120, 1))
# 计算目标 y
y = X @ w + b + noise
# 打印维度
print("X.shape:", X.shape)
print("y.shape:", y.shape)

class RevenueNet(nn.Module):
    def __init__(self):
        super(RevenueNet, self).__init__()
        self.fc1 = nn.Linear(8, 16)  # Input layer: 10 features -> 5 neurons
        self.fc2 = nn.Linear(16, 8)   # Hidden layer: 5 neurons -> 3 neurons
        self.fc3 = nn.Linear(8, 1)   # Output layer: 3 neurons -> 1 neuron
        self.relu = nn.ReLU()

    '''
    def __init__(self):
    super().__init__()
    # Input Layer (8 features) to Hidden Layer 1 (16 neurons)
    self.layer1 = nn.Linear(in_features=8, out_features=16)
    # Hidden Layer 1 (16 neurons) to Hidden Layer 2 (8 neurons)
    self.layer2 = nn.Linear(in_features=16, out_features=8)
    # Hidden Layer 2 (8 neurons) to Output Layer (1 neuron)
    self.layer3 = nn.Linear(in_features=8, out_features=1)
    # ReLU activation function for hidden layers
    self.relu = nn.ReLU()
    '''
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


'''
    def __init__(self):
        super(RevenueNet, self).__init__()
        # 输入层（8个神经元）到隐藏层1（16个神经元）
        self.layer1 = nn.Linear(in_features=8, out_features=16)
        # 隐藏层1（16个神经元）到隐藏层2（8个神经元）
        self.layer2 = nn.Linear(in_features=16, out_features=8)
        # 隐藏层2（8个神经元）到输出层（1个神经元）
        self.layer3 = nn.Linear(in_features=8, out_features=1)
        # ReLU激活函数
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x
'''
# Instantiate the model
model = RevenueNet()
criterion = nn.MSELoss()  # Mean Squared Error loss function
optimizer = optim.Adam(model.parameters(), lr=0.01)  # Stochastic Gradient Descent optimizer


# Training the network
losses = []
for epoch in range(30):  # Train for 20 epochs
    optimizer.zero_grad()  # Zero the gradients
    output = model(X)  # Forward pass
    loss = criterion(output, y)  # Compute the loss
    loss.backward()  # Backpropagation
    optimizer.step()  # Update weights
    losses.append(loss.item())  # Record the loss
    # print(f"Epoch {epoch}, Loss: {running_loss/len(trainloader)}")
    print(f"Epoch {epoch:02d} | Loss: {loss:.6f}")

# Plotting the training loss over time
plt.plot(losses)
plt.title('Training Loss Over Time')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()