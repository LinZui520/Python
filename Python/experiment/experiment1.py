import math

number1 = math.pow(3, 4)
number2 = math.sqrt(81)
number3 = math.exp(3)
print(number1, " ", number2, " ", number3)

# int类型
number4 = 3 + 4 * 5

# float类型
number5 = (number1 + number2 + number3) / 3

# str类型
name = 'Jack'
print(number4, " ", number5, " ", name)

studentNumber = int(input('输入学号'))
print(type(studentNumber), studentNumber)

studentName = input('输入姓名')
print(type(studentName), studentName)

grades = float(input('输入成绩'))
print(type(grades), grades)
