"""
定义一个空集合
通过for循环遍历列表
在for循环中将列表的元素添加至集合
最终得到元素去重后的集合对象，并打印输出
"""

# 定义一个列表
my_list = ["zi", "yu", "xuan", "yu", "yu", "zi", "xuan"]
my_set = set()
# 通过for循环遍历列表
for element in my_list:
    # print(element)

# 在for循环中将列表的元素添加至集合
    my_set.add(element)
print(my_set)
