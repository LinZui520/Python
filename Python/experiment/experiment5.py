import datetime


def feibo(n):
    if n == 1 or n == 2:
        return 1
    return feibo(n - 1) + feibo(n - 2)


print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

for i in range(1, 15):
    print(feibo(i), end=' ')
