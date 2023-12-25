# 设计一个类
class Student:
    neme = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建对象
student_1 = Student()
student_2 = Student()

# 赋值属性进行赋值
student_1.name = "周杰伦"
student_1.gender = "男"
student_1.nationality = "中国台湾"
student_1.native_place = "中国台湾"
student_1.age = 31

student_2.name = "王力宏"
student_1.gender = "男"
student_1.nationality = "中国香港"
student_1.native_place = "中国香港"
student_1.age = 31

# 获取信息
print(student_1.name)
print(student_1.gender)
print(student_1.nationality)
print(student_1.native_place)
print(student_1.age)
