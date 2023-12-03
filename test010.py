# """
# 演示对list列表的循环，使用while和for循环两种方式
# """
#
# def list_while_func():
#     """
#     使用while循环遍历列表演示函数
#     :return:None
#     """
#
#     my_list = ["zi", "yu", "xuan"]
#     # 循环控制变量通过控制下标索引来控制，默认0
#     # 每一次索引将下标索引变量+1
#     # 循环条件：下标索引变量 < 列表的元素数量
#
#     # 定义一个变量用来标记列表的下标
#     index = 0           # 初始值为0
#     while index < len(my_list):
#         # 通过index变量取出对应下标的元素
#         num = my_list[index]
#         print(num)
#         index += 1
# list_while_func()
#
# def list_for_funs():
#     """
#     使用for循环遍历列表的演示函数
#     :return:None
#     """
#
#     my_list = [1, 2, 3, 4, 5]
#     # for 临时变量 in 数据容器:
#     for element in my_list:
#         print(element)
#
# list_for_funs()

"""
取出列表内的偶数
定义一个列表，内容是：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
·遍历列表，取出列表内的偶数，并存入新的列表对象中
·使用while循环和for循环各操作一次
"""

# 定义列表
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_1 = []

# 使用while循环
index = 0
while index < len(my_list):
    element = my_list[index]
    if element % 2 == 0:
        my_list_1.append(element)
    index += 1
print(f"通过while循环，从列表：{my_list}中取出偶数，组成新列表:{my_list_1}")
