import numpy as np
import matplotlib.pyplot as plt
from torch import nn, optim
from torch.autograd import Variable
import torch


# 构建线性回归模型
class LinearRegression(nn.Module):

    # 定义模型的初始化函数，这个函数定义了这个模型的基本结构
    def __init__(self):
        # 调用父类的初始化函数
        super(LinearRegression, self).__init__()
        # 定义一个全连接层，输入大小为1，输出大小为1
        self.linear = nn.Linear(1, 1)

    # 定义前向传播函数，这个函数定义了输入和输出之间的运算关系
    def forward(self, x):
        out = self.linear(x)
        return out


def main():
    # 生成数据
    x = np.random.rand(100)
    noise = np.random.normal(0, 0.01, x.shape)
    y = x * 0.1 + 0.2 + noise
    # 绘制散点图
    plt.scatter(x, y)
    plt.show()
    # 将x,y转换为矩阵形式
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    # 将x,y转换为张量形式tensor
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)

    inputs = Variable(x)
    target = Variable(y)
    # 定义模型
    model = LinearRegression()
    # 定义损失函数
    criterion = nn.MSELoss()
    # 定义优化器
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    # 训练模型
    for epoch in range(1000):
        # 前向传播
        out = model(inputs)
        # 计算损失
        loss = criterion(out, target)
        # 梯度清零
        optimizer.zero_grad()
        # 计算梯度
        loss.backward()
        # 修改权值
        optimizer.step()
        # 打印损失
        if epoch % 200 == 0:
            print('epoch: {}, loss: {:.4}'.format(epoch, loss.item()))

    # 绘制图像
    y_pred = model(inputs)
    plt.scatter(x, y)
    plt.plot(x, y_pred.data.numpy(), 'r-', lw=5)
    plt.show()


if __name__ == '__main__':
    main()
