"""
文件处理相关模块
"""

# 接受传入文件路径，打印文件的全部内容
def print_file_info(file_name):
    """
    功能是接收传入文件路径，打印文件的全部内容
    :param file_name: 传入的文件路径
    :return: None
    """

    f = None
    f = open(file_name, "r", encoding="UTF-8")        # 打开文件
    my_file = f.read()        # 读取文件
    print(my_file)      # 打印文件全部内容
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except  Exception as e:
        print(f"文件不存在,捕获的异常为：{e}")          # 捕获异常，提示文件不存在
    finally:
        if f:               # 如果f为None，即为Flase，否则为True，关闭文件
            f.close()           # 关闭文件

# 接收文件路径以及传入数据，将数据追加写入到文件中
def append_to_file(file_name, data):
    """
    功能是接收传入文件路径，将数据追加写入到文件中
    :param file_name: 传入的文件路径
    :param data: 追加的数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':

# 测试
    print_file_info("D:/word.txt")
    # append_to_file("D:/word.txt","\n晚上加班咯")
