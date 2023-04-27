import os


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hello, my name is {} and I am {} years old.'.format(self.name, self.age))

    def __str__(self):
        return 'People(name={}, age={})'.format(self.name, self.age)


class Student(People):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def speak(self):
        print("Hello, my name is {} and I am a student in grade {}.".format(self.name, self.grade))


alice = Student('Alice', 20, 2)
alice.speak()
print(alice)

# 打开文件
file = open("example.txt", "w")

# 写入数据
file.write("This is an example file.\n")
file.write("It contains some text.\n")

# 关闭文件
file.close()

# 打开文件并读取数据
file = open("example.txt", "r")

# 读取整个文件
content = file.read()
print(content)

# 关闭文件
file.close()

# 打开文件并逐行读取数据
file = open("example.txt", "r")

# 逐行读取文件
for line in file:
    print(line)

# 关闭文件
file.close()

# 获取当前工作目录
current_dir = os.getcwd()
print(current_dir)

# 创建目录
new_dir = "new_directory"
os.mkdir(new_dir)

# 重命名目录
os.rename(new_dir, "renamed_directory")

# 删除目录
os.rmdir("renamed_directory")

# 获取目录下的文件和目录列表
files = os.listdir(".")
for file in files:
    print(file)

# 删除文件
os.remove("example.txt")
