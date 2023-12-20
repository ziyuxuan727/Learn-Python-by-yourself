# 打开文件并定义文件名
f = open("D:/word.txt", "r", encoding="UTF-8")
print(type(f))
num_1 = f.read()
print(type(num_1))
counter = num_1.count("itheima")
print(num_1)
print(f"个数有：{counter}")

# f = open("D:/word.txt", "r", encoding="UTF-8")
# num_1 = f.read()
# print(num_1)
# import time
