"""
升职加薪
并通过for循环，对所有级别为1的员工，级别上升一级，薪水增加1000元
"""

# 定义字典
name_score = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 1
    }
}
print(type(name_score))
print(name_score["周杰伦"])
print(type(name_score["周杰伦"]))
print(name_score["周杰伦"]["部门"])
# 遍历name_score
# 方法一
keys = name_score.keys()
for x in keys:
    print(x)
    print(name_score[x])
    if name_score[x]["级别"] == 1:
        name_score[x]["级别"] += 1
        name_score[x]["工资"] += 1000
        print(name_score[x])
        print("nice")
print(keys)
print(type(keys))

# 通过for循环，对所有级别为1的员工，级别上升一级，薪水增加1000元
for level in name_score:
    print(type(level))
    print(level)
    print(name_score[level])
    if name_score[level]["级别"] == 2:
        name_score[level]["工资"] += 1000
        name_score[level]["级别"] += 1
        print(name_score[level])
