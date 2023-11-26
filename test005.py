import random
num_n = random.randint(1, 10)

num_m = random.randint(1, 10)

"""
演示布尔类型的定义
以及比较运算符的应用
"""
# 定义变量存储布尔类型的数据?
"""
公司要发礼物，条件是：
1、必须是大于等于18岁小于30岁的成年人
2、同时入职时间需满足大于两年，或者级别大于3才可领取
"""
age_1 = int(input("请输入你的年龄："))
if age_1 <= 18:
    print("抱歉，您不符合要求无法领取礼物。")
elif age_1 < 30:
    print("请问您入职几年：")
    if int(input()) > 2:
        print("恭喜，您符合公司要求，可以领取礼物。")
    elif int(input("请问您的级别是多少：")) > 3:
        print("恭喜，您符合公司要求，可以领取礼物。")
    else:
        print("抱歉，您不符合要求无法领取礼物。")
else:
    print("抱歉，您不符合要求无法领取礼物。")

'''
定义一个数字（1~10随机产生），通过三次判断来猜出数字
要求：
1、随机数字产生，范围1~10
2、有3次机会猜测数字，通过3层嵌套判断实现
3、每次猜不中会提示大了小了
'''
# 先定义一个变量num_m，产生随机数字
# import random
# num_m = random.randint(1,10)
num_1 = int(input("请输入您猜的第一个数字："))
if num_1 != num_m:
    print("可惜，您猜错了。")
    if num_1 < num_m:
        print("您猜的数字小了")
        num_2 = int(input("请输入您猜的第二个数字："))
        if num_2 != num_m:
            print("可惜，您猜错了。")
            if num_2 < num_m:
                print("您猜的数字小了")
                num_3 = int(input("请输入您猜的三个数字："))
                if num_3 != num_m:
                    print("可惜，您猜错了。")
                    if num_3 < num_m:
                        print("您猜的数字小了")
                    else:
                        print("您猜的数字大了")
                else:
                    print("恭喜你，猜中了!")
            else:
                print("您猜的数字大了")
        else:
            print("恭喜你，猜中了!")
    else:
        print("您猜的数字大了")
else:
    print("恭喜你，猜中了!")

# 上述这个是我写的屎山代码，下面这个我重新开始编写改进


'''
定义一个数字（1~10随机产生），通过三次判断来猜出数字
要求：
1、随机数字产生，范围1~10
2、有3次机会猜测数字，通过3层嵌套判断实现
3、每次猜不中会提示大了小了
'''

# 首先，定义一个变量，取（1~10）的随机数字
# import random
# num_n = random.randint(1,10)

num_1 = int(input("请输入您猜的第一个数字："))
if num_1 == num_n:
    print("恭喜您第一次猜对了！")
else:
    if num_1 < num_n:
        print("您猜的数字小了")
    else:
        print("您猜的数字大了")
    num_1 = int(input("请输入您猜的第二个数字："))
    if num_1 == num_n:
        print("恭喜您第二次猜对了！")
    else:
        if num_1 < num_n:
            print("您猜的数字小了")
        else:
            print("您猜的数字大了")
        num_1 = int(input("请输入您猜的第三个数字："))
        if num_1 == num_n:
            print("恭喜您第三次猜对了！")
        else:
            print("不好意思，您三次机会都猜错了。")
# 查看num_n的值
print(num_n)
