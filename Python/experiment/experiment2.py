# encoding=utf-8
import jieba

jieba.setLogLevel(jieba.logging.INFO)

list1 = ['Mark']
list1.insert(0, 'Alex')
list1.append('Jack')
list1.remove('Mark')
print(list1)

colors = ('red', 'blue')
print(colors)

var1 = 'Hello'
var2 = 'Python'
print(var1 + ' ' + var2)

value1 = set()
value1.add(7)
value1.add(8)
value1.remove(7)
value2 = {5, 2, 0, 8}
print(value2 - value1)

dic = {'apple': 100, 'banana': 50, 'strawberry': 75}
print(dic)
dic['banana'] = 25
del dic['strawberry']
print(dic)

seg_list1 = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list1))  # 全模式

seg_list2 = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list2))  # 精确模式

seg_list3 = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list3))

seg_list4 = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list4))
