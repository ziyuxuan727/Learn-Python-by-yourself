# 设计一个类
class Student:

    # 构造方法
    def __init__(self, name, age, native):
        self.name = name
        self.age = age
        self.native = native
        print(f"学生{x}信息录入完成，信息为：【学生姓名：{name}，年龄：{age}，地址：{native}】")

# # 定义对象
# stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("情输入学生地址："))

for x in range(1,11):
    print(f"当前录入第{x}位学生信息，总共需录入10名学生信息")
    # 定义对象
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("情输入学生地址："))
