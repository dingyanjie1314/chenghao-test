# 格式化输出
"""
格式符号（常用）：
    %s：字符串
    %d：十进制整数，%06d，表示输出的整数显示位数，不不⾜足以0补全，超出当前位数则原样输出
    %f：浮点型%.2f，表示⼩小数点后显示的⼩小数位数
"""
age = 18
name = 'TOM'
weight = 75.5
student_id = 1
# 我的名字是TOM
print('我的名字是%s' % name)
# 我的学号是0001
print('我的学号是%04d' % student_id)
print('我的学号是%d' % student_id)
# 我的体重是75.50公⽄
print('我的体重是%.2f公⽄' % weight)
print('我的体重是%f' % weight)
# 我的名字是TOM，今年年18岁了
print('我的名字是%s，今年年%d岁了' % (name, age))
#f表达式输出
#我的名字是TOM，明年年19岁了
print(f'我的名字是{name}, 明年年{age + 1}岁了')