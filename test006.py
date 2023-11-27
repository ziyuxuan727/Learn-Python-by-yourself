"""
演示while循环的基础应用
"""

# i = 0
# while i < 100:
#     print("加油，冲冲冲！")
#     i += 1
#

# 求1~100的整数和
# 定义变量和为num_1
# a = 1
# num_1 = 0
# while a <= 100:
#     num_1 += a
#     a += 1
# print(f"1~100的整数和为：{num_1}")

'''
设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
'''
# # 生成一个1~100的随机数
# import random
# num_2 = random.randint(1,100)
# # 输入猜测的数字
# b = int(input("请输入你猜的数字："))
# # 定义num_3为猜测次数
# num_3 = 1
# # 开始循环判断
# while b != num_2:
#     if b < num_2:
#         print("不好意思，您猜的数字小了，请您继续。")
#     else:
#         print("不好意思，您猜的数字大了，请您继续。")
#     b = int(input("请再次输入你猜的数字："))
#     num_3 += 1
# print(f"恭喜你第{num_3}次猜对了！")


# 方法2
# 获取一个1~100的整数
# import random
# num_4 = random.randint(1, 100)
# # 通过一个布尔类型的变量，做循环继续的标志
# flag = True
# # 定义一个变量，记录猜测次数
# count_1 = 0
#
# while flag:
#     c = int(input("请输入您猜的数字："))
#     count_1 += 1
#     if c == num_4:
#         print("恭喜您猜对了！")
#         flag = False
#     else:
#         if c < num_4:
#             print("不好意思，你猜的数字小了。")
#         else:
#             print("不好意思，您猜的数字大了。")
# print(f"您总共猜了:{count_1}次。")


# # print语句一般都是默认换行，现在让print不换行
# print("Hello")
# print("ziyuxuan")
#
# print("Hello", end='')
# print("ziyuxuan", end='')

# 制表符\t 可以让我们多行字符串对齐
# print("hello xiaowang")
# print("hello ziyuxuan727")
#
# print("hello\txiaowang")
# print("hello\tziyuxuan727")


# 打印一个九九乘法表

# 定义i为行数,j为列数，定义i*j结果为num_6
# i = j = 1
# num_6 = 1
#
# while i <= 9:
#     j = 1
#     while i >= j:
#         num_6 = i * j
#         if i == j:
#             print(f"{j} * {i} = {num_6}\t")
#         else:
#             print(f"{j} * {i} = {num_6}\t", end="")
#         j += 1
#     i += 1


# 上述是自己写的屎山代码，下面再进行优化

# 定义i为行数
# i = 1
#
# while i <= 9:
#     # 定义j为列数
#     j = 1
#     while j <= i:
#         print(f"{j} + {i} = {i * j}\t", end="")
#         j += 1
#     i += 1
#     print()

# 演示for循环的基础语法

# 定义变量
# name_1 = "ziyuxuan"
#
# for x in name_1:
#     # 其中for的作用是：将name_1中的内容，挨个取出赋予x临时变量
#     # 就可以在循环体内对x进行处理了
#     print(x)
#

# 数一数有几个a

#定义a的数量为num_6
num_6 = 0
# 定义字符串变量name_5
name_5 = "itheima is a brand ofitcast"

for x in name_5:
    if x == "a":
        num_6 += 1
print(f"里面有{num_6}个a")

