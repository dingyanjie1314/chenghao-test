# 需求：一个函数完成两个数1和2的加法运算
def add_sum():
    result = 1 + 2
    print(result)


add_sum()


# 需求：上述add_num函数只能完成数字1和2的加法运算, 如果想要这个函数变得更灵活,可以计算任何用户指定的两个数字的和
# 定义函数时同时定义了接收用户数据的参数a和b，a和b是形参
def add_sum(a, b):
    result = a + b
    print(result)


# 调用函数时传入数据
add_sum(6, 99)


# 返回值
# 我们去超市购物, 比如买烟, 给钱之后, 是不是售货员会返回给我们烟这个商品, 在函数中,如果需要返回结果给用户需要使用函数返回值
def buy():
    return "烟"


# 使用变量保存函数返回值
return_data = buy()
print(return_data)


# 需求：制作一个计算器, 计算任意两数字之和, 并保存结果
def sum(a, b):
    return a + b


add_sum = sum(10, 30)
print(add_sum)


# 函数说明
def sum_num():
    """这是函数说明文档"""
    return 2 + 5


# help查看函数说明文档
help(sum_num)


# 函数嵌套
def sum_num(a, b):
    """ 求和函数 """
    return a + b


help(sum_num)


def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')


testA()


# 函数应用
# 需求：打印一条横线
def print_line():
    print("-" * 20)


print_line()


# 打印多条横线
def print_line():
    print("-" * 20)


def print_lines():
    i = 0
    while i <= 5:
        print_line()
        i += 1


print_lines()


# 函数计算
# 需求：求三个数之和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(7, 8, 9)
print(result)


# 需求：求三个数平均值
def avg_num(a, b, c):
    result = sum_num(a, b, c)
    return result / 3


avg_result = avg_num(3, 4, 5)
print(avg_result)
