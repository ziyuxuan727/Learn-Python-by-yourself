# """
# 演示地图可视化的基本使用
# """
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# # 准备地图对象
# map = Map()
# # 准备数据
# data = [
#     ("北京市", 99),
#     ("上海市", 199),
#     ("湖南省", 299),
#     ("台湾省", 399),
#     ("广东省", 499)
# ]
# # 添加数据
# map.add("测试地图", data, "china")
#
# # 设置全局选项
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,          # 进行分段
#         pieces=[
#             {"min": 1, "max": 9,"label": "1-9", "color": "#CCFFFF"},
#             {"min": 10, "max": 99,"label": "10-99", "color": "#FF6666"},
#             {"min": 100, "max": 500,"label": "100-500", "color": "#990033"}
#         ]
#     )
# )
#
# # 生成图表
# map.render()

"""
基本柱状图
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 构建柱状图对象
bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# x与y轴反转
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线对象
timeline = Timeline(
    {"theme": ThemeType.CHALK}
)
# 在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
# 要使用时间线绘图，而不是用图表绘图

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图
timeline.render("基础时间线柱状图.html")

