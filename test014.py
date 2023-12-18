# 打开文件并定义文件名
f = open("D:/word001.txt", "r", encoding="UTF-8")
# 输出文件类型
print(type(f))
# 读取文件
num_1 = f.read()
# 消除换行符
num_4 = num_1.replace("\n", " ")
# 输出读取的内容类型
print(type(num_1))
# 输出除去换行符的字符串
print(num_4)
# 将字符串以空格为界限分割为多个字符串
num_2 = num_4.split(" ")
# 输出得到的新字符串
print(num_2)
# 统计字符串指定字符串的个数
num_3 = num_2.count("itheima")
# 输出指定字符串的个数
print(num_3)
# 关闭文件
f.close()
# time.sleep(16800)
