import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

# 数据预处理：转换为张量并归一化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # 归一化到[-1, 1]
])

# 加载CIFAR-10数据集
trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)

testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=128, shuffle=False)

# 定义CNN模型
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # 卷积层1：3通道输入，64通道输出，卷积核3x3，步长1，padding=1
        self.conv1 = nn.Conv2d(3, 64, 3, padding=1)
        # 激活函数
        self.relu = nn.ReLU()
        # 池化层：2x2最大池化，步长2
        self.pool = nn.MaxPool2d(2, 2)
        # 卷积层2：64通道输入，128通道输出，卷积核3x3，步长1，padding=1
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        # 全连接层1：输入维度128*8*8，输出维度1024
        self.fc1 = nn.Linear(128 * 8 * 8, 1024)
        # 全连接层2：输入维度1024，输出维度512
        self.fc2 = nn.Linear(1024, 512)
        # 全连接层3：输入维度512，输出维度10（CIFAR-10有10个类别）
        self.fc3 = nn.Linear(512, 10)
        #  dropout层，防止过拟合
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        # 卷积层1 + 激活 + 池化
        x = self.pool(self.relu(self.conv1(x)))  # 输出尺寸：16x16x64
        # 卷积层2 + 激活 + 池化
        x = self.pool(self.relu(self.conv2(x)))  # 输出尺寸：8x8x128
        # 展平
        x = x.view(-1, 128 * 8 * 8)
        # 全连接层1 + 激活 + dropout
        x = self.dropout(self.relu(self.fc1(x)))
        # 全连接层2 + 激活 + dropout
        x = self.dropout(self.relu(self.fc2(x)))
        # 全连接层3，输出类别概率
        x = self.fc3(x)
        return x

# 实例化模型、损失函数和优化器
model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 10
train_losses = []
test_losses = []

for epoch in range(epochs):
    running_loss = 0.0
    for inputs, labels in trainloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    train_loss = running_loss / len(trainloader)
    train_losses.append(train_loss)

    # 测试模型
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in testloader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
    test_loss = test_loss / len(testloader)
    test_losses.append(test_loss)
    accuracy = 100. * correct / total

    print(f'Epoch {epoch+1}, Train Loss: {train_loss:.3f}, Test Loss: {test_loss:.3f}, Accuracy: {accuracy:.2f}%')

# 绘制损失曲线
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Testing Loss')
plt.show()

# 打印最终准确率
print(f'Final Accuracy: {accuracy:.2f}%')

# 可视化部分测试样本的预测结果
def imshow(img):
    img = img / 2 + 0.5  # 反归一化
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

dataiter = iter(testloader)
images, labels = next(dataiter)
imshow(torchvision.utils.make_grid(images[:4]))
print('Ground Truth: ', ' '.join(f'{testset.classes[labels[j]]:5s}' for j in range(4)))

outputs = model(images[:4])
_, predicted = torch.max(outputs, 1)
print('Predicted: ', ' '.join(f'{testset.classes[predicted[j]]:5s}' for j in range(4)))