# # ATM机
# """
# 定义一个全局变量: money，用来记录银行卡余额（默认5000000)定义一个全局变量: name，用来记录客户姓名（启动程序时输入)
# 定义如下的函数:
# 查询余额函数·存款函数·取款函数·主菜单函数
# 要求:
# 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都应显示一下当前余额
# 客户选择退出或输入错误，程序会退出，否则一直运行
# """
#
# # 昨天写的屎山代码，今天优化一下
#
# # 定义全局变量
# money = 50000000
# name = input("请输入您的名字；")
#
# # 定义查询余额函数
# def query(show_header):
#     if show_header:
#         print("-----查询余额-----")
#     print(f"您的余额为：{money}元")
#
# # 定义存款函数
# def saving(num):
#     # 定义全局变量money
#     global money
#     money += num
#     # 显示余额
#     query(False)
#
# # 定义取款函数
# def get_money(num):
#     # 定义全局变量money
#     global money
#     money -= num
#     # 显示余额
#     query(False)
#
# # 定义主菜单函数
# def main():
#     print("--------主菜单--------")
#     print("欢迎来到ATM，请您选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入你的选择：")
#
# # 设置无限循环
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue        # 通过continue继续下一次循环，一进来就是回到了主菜单
#     elif keyboard_input == "2":
#         saving(int(input("请输入您的存款数额：")))
#         continue
#     elif keyboard_input == "3":
#         get_money(int(input("请输入您的取款数额：")))
#         continue
#     elif keyboard_input == "4":
#         print("退出程序了")
#         break
#     else:
#         print("退出程序了")
#
# # 试试return的用法
# def main():
#     print("dd")
#     return input("请输入您输入的内容：")
# print(main())         # 由内向外执行操作
#

"""
演示数据类型之：list列表
"""
# my_list = ["zi", "yu", "xuan"]
# print(my_list)
# print(type(my_list))

# 常用功能练习
"""
有一个列表，内容是[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄
请通过列表的功能(方法)，对其进行
1.定义这个列表，并用变量接收它
2.追加一个数字31，到列表的尾部
3.追加一个新列表[29,33,30]，到列表的尾部
4.取出第一个元素(应是: 21)
5.取出最后一个元素(应是:30)
6.查找元素31，在列表中的下标位置
"""

# 定义列表
year_student = [21, 25, 21, 23, 22, 20]
# 追加一个 数字31到列表尾部
year_student = year_student.append(31)
# 追加一个新列表
year_student.extend([29, 33, 30])
# 取出第一个元素
ele_1 = year_student.index(21)
print(ele_1)
