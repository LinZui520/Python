import numpy as np
import matplotlib.pyplot as plt
from torch import nn, optim
from torch.autograd import Variable
import torch


class NonlinearRegression(nn.Module):
    # 定义模型的初始化函数，这个函数定义了这个模型的基本结构
    def __init__(self):
        # 调用父类的初始化函数
        super(NonlinearRegression, self).__init__()
        # 定义一个连接层1 -> 10 -> 1
        self.linear1 = nn.Linear(1, 10)
        self.tanh = nn.Tanh()
        self.linear2 = nn.Linear(10, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.tanh(x)
        x = self.linear2(x)
        return x


def main():
    # 生成数据
    x = np.linspace(0, 1, 100)
    noise = np.random.normal(0, 0.015, x.shape)
    y = (x - 1.1) * (x + 0.1) + 0.5 + noise
    # 将x,y转换为矩阵形式
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    # 将x,y转换为张量形式tensor
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    inputs = Variable(x)
    target = Variable(y)
    # 定义模型
    model = NonlinearRegression()
    # 定义损失函数
    criterion = nn.MSELoss()
    # 定义优化器
    optimizer = optim.SGD(model.parameters(), lr=0.3)
    # 训练模型
    for i in range(20000):
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
        if i % 200 == 0:
            print('i: {}, loss: {:.4}'.format(i, loss.item()))

    # 绘制图像
    y_pred = model(inputs)
    plt.scatter(x, y)
    plt.plot(x, y_pred.data.numpy(), 'r-', lw=3)
    plt.show()


if __name__ == '__main__':
    main()
