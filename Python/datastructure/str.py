s = input()
dic = {}
for i in range(0, 10):
    dic[str(i)] = 0
for i in s:
    dic[i] += 1
print(dic)
