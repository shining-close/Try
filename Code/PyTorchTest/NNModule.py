import torch  #the core PyTorch library
import torch.nn as nn  #contains the building blocks for neural networks.
import torch.nn.functional as F  #provides functions for different operations, including activation functions.



# Define the neural network class.
# The network is defined by creating a subclass of nn.Module,
# which is the base class for all neural network modules in PyTorch.
class SimpleNN(nn.Module):
    # The __init__ method defines the layers of the network
    def __init__(self):
        super(SimpleNN, self).__init__()

        # Define the layers
        self.fc1 = nn.Linear(784, 128)  # First fully connected layer (input: 784, output: 128)
        self.fc2 = nn.Linear(128, 64)  # Second fully connected layer (input: 128, output: 64)
        self.fc3 = nn.Linear(64, 10)   # Third fully connected layer (input: 64, output: 10)

    # The forward method defines how the input data flows through the network.
    def forward(self, x):
        # Apply ReLU activation to the first layer
        x = F.relu(self.fc1(x))

        # Apply ReLU activation to the second layer
        x = F.relu(self.fc2(x))

        # Apply softmax activation to the output layer
        x = F.log_softmax(self.fc3(x), dim=1)

        return x

# Instantiate the model
model = SimpleNN()

# Print the model architecture
print(model)


import torch.optim as optim
from torchvision import datasets, transforms

# Load the MNIST dataset
transform = transforms.Compose([transforms.ToTensor()])
trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1, 6):  # 5 epochs
    running_loss = 0.0
    for images, labels in trainloader:
        # Flatten the images into vectors
        images = images.view(images.shape[0], -1)
        
        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Compute loss
        loss = criterion(outputs, labels)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        # Update running loss
        running_loss += loss.item()

    print(f"Epoch {epoch}, Loss: {running_loss/len(trainloader)}")


testset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False)

correct = 0
total = 0

with torch.no_grad():
    for images, labels in testloader:
        images = images.view(images.shape[0], -1)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total}%")

