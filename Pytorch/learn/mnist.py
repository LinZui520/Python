from torch import nn, optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch


# 利用卷积神经网络的mnist数字识别
# 定义网络结构
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(1, 32, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2, 2))
        self.conv2 = nn.Sequential(nn.Conv2d(32, 64, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2, 2))
        self.fc1 = nn.Sequential(nn.Linear(3136, 1000), nn.Dropout(p=0.5), nn.ReLU())
        self.fc2 = nn.Sequential(nn.Linear(1000, 10), nn.Softmax(dim=1))

    def forward(self, x):
        # [64, 1, 28, 28]
        x = self.conv1(x)
        x = self.conv2(x)
        # [64, 63, 7, 7]
        x = x.view(x.size()[0], -1)
        x = self.fc1(x)
        x = self.fc2(x)
        return x


def train():
    model.train()
    for i, data in enumerate(train_loader):
        # 获得一个批次的数据和标签
        inputs, labels = data
        # 获得模型预测结果
        out = model(inputs)
        # 计算loss
        loss = criterion(out, labels)
        # 梯度清零
        optimizer.zero_grad()
        # 计算梯度
        loss.backward()
        # 修改权值
        optimizer.step()


def test():
    model.eval()
    correct = 0
    for i, data in enumerate(test_loader):
        # 获得一个批次的数据和标签
        inputs, labels = data
        # 获得模型预测结果
        out = model(inputs)
        # 获得最大值,以及最大值所在的位置
        _, predicted = torch.max(out, 1)
        # 预测正确的数量
        correct += sum((predicted == labels)[:])
    print('Test acc:{0}'.format(correct / len(test_dataset)))

    correct = 0
    for i, data in enumerate(train_loader):
        # 获得数据和对应标签
        inputs, labels = data
        # 获得模型预测结果
        out = model(inputs)
        # 获得最大值,以及最大值所在的位置
        _, predicted = torch.max(out, 1)
        # 预测正确的数量
        correct += sum((predicted == labels)[:])
    print('Train acc:{0}'.format(correct / len(train_dataset)))


# 训练集
train_dataset = datasets.MNIST(root='./',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

# 测试集
test_dataset = datasets.MNIST(root='./',
                              train=False,
                              transform=transforms.ToTensor(),
                              download=True)

# 批次大小
batch_size = 64

# 装载训练集
train_loader = DataLoader(dataset=train_dataset,
                          batch_size=batch_size,
                          shuffle=True)
# 装载测试集
test_loader = DataLoader(dataset=test_dataset,
                         batch_size=batch_size,
                         shuffle=True)

# 定义模型
model = Net()
# 定义代价函数
criterion = nn.CrossEntropyLoss()
# 定义优化器
optimizer = optim.Adam(model.parameters(), lr=0.0003)

for epoch in range(1, 21):
    print('epoch:', epoch)
    train()
    test()
