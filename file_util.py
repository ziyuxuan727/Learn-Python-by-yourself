"""
字符串相关模块
"""

# 对字符串进行切片
def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s: 将被反转的字符串
    :return: 返回反转后的字符串
    """
    # result = s[::-1]
    # return result
    return s[::-1]

# 按照下标x和y，对字符串进行切片
def subsrt(s, x, y):
    """
    功能是将字符串完成切片
    :param s: 进行切片的字符串
    :param x: 字符串起始下标
    :param y: 字符串终止下标
    :return: 返回切片得到的字符串
    """
    # result = s[x:y:1]
    # return result
    return s[x:y:1]

if __name__ == '__main__':

# 测试str_reverse(s)函数
    result_1 = str_reverse("123456")
    print(result_1)

# 测试substr(s, x, y)函数
    result_2 = subsrt("123456",2,5)
    print(result_2)
