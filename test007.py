# 1~100（不含100本身）范围内有多少偶数

# 定义变量num_1为偶数数量
# num_1 = 0
# for x in range(1, 100):
#     if x % 2 == 0:
#         num_1 += 1
# print(f"一共有{num_1}个偶数。")

# 通过for循环来打印九九乘法表

# for x in range(1, 10):
#     # 定义i为内循环行数
#     i = 1
#     while i <= x:
#         print(f"{i} * {x} = {i * x}\t", end='')
#         i += 1
#     print()
#
# # 方法二
#
# # 通过外部循环控制行数
# for i in range(1,10):
#     # 通过内部循环控制每一行的数据
#     for j in range(1, i + 1):
#         # 在内层输出每一行的内容
#         print(f"{j} + {i} = {j * i}\t", end='')
#     print()

"""
某公司，账户余额一万元，给20名员工发工资
· 员工编号从1到20，从编号1开始依次领取工资，每人领取1000元
· 领取工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
· 如果工资发完了，结束发工资
"""

# # 定义变量num_2为账户余额
# num_2 = 10000
# # 定义变量num_3为已发工资的人数
# num_3 = 0
#
# # 通过外层循环控制员工编号
# for m in range(1, 21):
#     # 定义变量绩效为员工KPI（随机生成）
#     import random
#     KPI = random.randint(1, 10)
#     if KPI < 5:
#         print(f"员工{m}，您的绩效分为{KPI}，您KPI低于5，不发工资，下一位")
#     else:
#         num_3 += 1
#         # 判断是否还有工资可发
#         if num_3 <= 10000 / 1000:
#             print(f"员工{m}，绩效分为{KPI}，可以领取1000元工资。")
#         else:
#             print(f"员工{m},不好意思，工资发完了。")
#             break

# """
# 某公司，账户余额一万元，给20名员工发工资
# · 员工编号从1到20，从编号1开始依次领取工资，每人领取1000元
# · 领取工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
# · 如果工资发完了，结束发工资
# """
#
# # 定义变量num_2为账户余额
# num_2 = 10000
# # 定义变量num_3为已发工资的人数
# num_3 = 0
#
# # 通过外层循环控制员工编号
# for m in range(1, 21):
#     # 定义变量绩效为员工KPI（随机生成）
#     import random
#     KPI = random.randint(1, 10)
#     if KPI < 5:
#         print(f"员工{m}，您的绩效分为{KPI}，您KPI低于5，不发工资，下一位")
#         continue
#     num_3 += 1
#     # 判断是否还有工资可发
#     if num_3 <= 10000 / 1000:
#         print(f"员工{m}，绩效分为{KPI}，可以领取1000元工资。")
#     else:
#         print(f"员工{m},不好意思，工资发完了。")
#         break

# 演示函数的定义法

# 定义一个函数
# def say_hi():
#     print("你好啊！")
# a = say_hi()

"""
自动查核酸
定义一个函数，函数名任意，要求调用函数后可以输出如下欢迎语：
欢迎ziyuxuan！
请出示您的健康码和72小时核酸证明！
"""

# 定义函数
# def action_1():
#     print("欢迎ziyuxuan！")
#     print("请出示您的健康码和72小时核酸证明！")
#
# # 调用函数
# a = action_1()

# 定义两数相加的函数，通过参数接收被计算的2个数字
# def add_1(x, y):
#     print(x + y)
# add_1(1,6)

# 升级版自动查核酸
"""
定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温）
在函数内进行体温判断（正常范围：小于等于37.5度）。
"""

# 定义一个函数
# def num_5(x):
#     if x <= 37.5:
#         print("体温正常")
#     else:
#         print("体温异常")

"""
演示特殊字面量None
"""

# 无return语句的函数返回值
# def say_hi():
#     print("你好啊！")
#
# result = say_hi()
# print(result)
# print(type(result))

# 主动返回None
# def say_hi():
#     print("你好啊！")
#     return(None)

"""
演示对函数进行文档说明
"""

# 定义函数，对文档进行说明
# def add(x, y):
#     """
#     add函数可以接收两个参数，进行两个数的相加减
#     :param x: 形参x表示相加中的一个数
#     :param y: 形参y表示相加中的一个数
#     :return: 返回值是两个数相加的结果
#     """
#     result = x + y
#     print(f"两数相加的结果为：{result}")
#
# add(5, 6)

# 演示嵌套调用函数

# 定义函数fanc_b
# def fanc_b():
#     print("--2--")
# # 定义函数fanc_a，并在内部调用fanc_a
# def fanc_a():
#     print("--1--")
#
#     # 嵌套调用fanc_b
#     fanc_b()
#     print("--3--")
# # 调用函数fanc_a
# fanc_a()

# ATM机
"""
定义一个全局变量: money，用来记录银行卡余额（默认5000000)定义一个全局变量: name，用来记录客户姓名（启动程序时输入)
定义如下的函数:
查询余额函数·存款函数·取款函数·主菜单函数
要求:
程序启动后要求输入客户姓名
查询余额、存款、取款后都会返回主菜单
存款、取款后，都应显示一下当前余额
客户选择退出或输入错误，程序会退出，否则一直运行
"""

# 定义全局变量money和name
# money = 5000000
# # 输入客户名字
# name = input("请输入您的名字：")
#
# # 查询余额
# def yue_1():
#     print(f"您当前余额为：{money}")
#     # 返回主菜单
#     input("按回车键回到主菜单")
#
# # 存款
# def cunkuan_1():
#     # 定义并输入存款数额
#     money_1 = int(input("请输入您存款的数额："))
#     # 定义全局变量money
#     global money
#     money += money_1
#     # 显示余额
#     yue_1()
#
# # 取款
# def qukuan_1():
#     # 定义并输入存款数额
#     money_2 = int(input("请输入您取款的数额："))
#     # 定义全局变量money
#     global money
#     money -= money_2
#     # 显示余额
#     yue_1()
#
# # 主菜单函数
# def zhucaidan():
#     # 显示主菜单显示选项
#     print("查询余额请输入1")
#     print("存款请输入2")
#     print("取款请输入3")
#     print("退出请输入4")
#
# # 定义变量num_6为服务选项
# num_6 = None
#
# # 设定循环
# while True:
#     # 回到主菜单
#     zhucaidan()
#     # 输入您要选择的服务
#     num_6 = int(input("请输入您选择的服务："))
#     # 查余额
#     if num_6 == 1:
#         yue_1()
#         continue
#     # 存款
#     elif num_6 == 2:
#         cunkuan_1()
#         continue
#     # 取款
#     elif num_6 == 3:
#         qukuan_1()
#         continue
#     # 退出
#     elif num_6 == 4:
#         print("再见")
#         break
#     # 退出程序
#     else:
#         print("您输入错误，自动退出程序。")
#         break
