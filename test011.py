# """
# 分割字符串
# 给定一个字符串："zi yu xuan"
# ·统计字符串内有多少个"ua"字符
# ·将字符串内的空格，全部替换为字符“|”
# ·并按照“|”进行字符串分割，得到列表
# """
#
# # 定义字符串
# name = "zi yu xuan"
#
# # 统计字符串内有多少个"ua"字符
# name_1 = name.count("ua")
# print(name_1)
#
# # 将字符串内的空格，全部替换为字符"|"
# name_2 = name.replace(" ", "|")
# print(name_2)
#
# # 并按照"|"进行字符串分割，得到列表
# name_3 = name_2.split("|")
# print(name_3)

# # 对序列进行切片
# my_str = "123456789"
# my_str_1 = my_str[2:3:1]
# print(my_str_1)
#

"""
序列的切片实践
有字符串"嗨，轩宇紫，你好啊！"
请使用任何学过的方式，得到"紫宇轩"
"""

# 定义字符串
my_sentence = "嗨，轩宇紫，你好啊！"

# 切片得到新的序列
my_name_1 = my_sentence[-6:-9:-1]
print(my_name_1)

# 使用split将字符串分隔开
my_name_2 = my_sentence.split(",")
print(my_name_2)
# 通过替换直接得到
my_name_3 = my_sentence.replace("嗨，轩宇紫，你好啊！", "紫宇轩")
print(my_name_3)

# 通过切片直接得到
my_name_4 = my_sentence[2:5][::-1]
print(my_name_4)
