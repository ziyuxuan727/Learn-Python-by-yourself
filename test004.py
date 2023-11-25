numb1 = 2023
numb2 = 11.25
print("今年是%4.2f年，今天是%5.2f" % (numb1, numb2))


print("1*1的结果是：%d" % (1 * 1))
print(f"1*1的结果是: {1 * 1}")

# 公司名
name = "传智播客"
# 当前股价
stock_price = 19.99
# 股票代码
stock_code = "003032"
# 股票每日增长系数
stock_price_daily_growth_factor = 1.2
# 增长天数
growth_days = 7
print(f"公司：{'传智播客'}，股票代码：{'003032'}，当前股价：{19.99}")
print("公司：%s，股票代码：%s，当前股价：%.2f" % (name, stock_code, stock_price))
print(f"每日增长系数是：{1.2}，经过{7}天的增长后，股价达到了：{19.99*7**1.2}")
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, (19.99*7**1.2)))
stock_price = 19.99*7**1.2
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price))
