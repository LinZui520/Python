import win32ras

import time


def connect(dialname, account, passwd):
    dialparams = (dialname, '', '', account, passwd, '')
    return win32ras.Dial(None, None, dialparams, None)


def dialbroadband():
    dialname = 'Campus Network'
    account = '18942324853'
    passwd = '324853'
    handle, result = connect(dialname, account, passwd)

    return not result


for i in range(0, 10):
    if dialbroadband():
        print('连接成功')
        break
    else:
        print("连接失败，等待1秒再次尝试")
        time.sleep(1)
