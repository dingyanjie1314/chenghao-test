# 变量作用于
# 局部变量:变量a是定义在testA函数内部的变量,在函数外部访问则立即报错
def testA():
    a = 100
    print(a)


testA()
# NameError: name 'a' is not defined
# print(a)
# 全局变量:函数体内、外都能生效的变量
a = 200


def testA():
    print(a)


def testB():
    print(a)


testA()
testB()
# 需求：testB函数需求修改变量a的值为200
a = 100


def testA():
    print(a)


def testB():
    a = 200
    print(a)


testA()
testB()
print(f"全局变量为{a}")

# 需求：如何在函数体内部修改全局变量
a = 100


def testA():
    print(a)


def testB():
    global a
    a = 200
    print(a)


testA()
testB()
print(f"全局变量为{a}")

# 多函数程序执行流程
# 共用全局变量
# 定义全局变量
glo_num = 0


def testA():
    # 修改全局变量
    global glo_num
    glo_num = 200


def testB():
    # 调用testA中修改后的全局变量
    print(glo_num)


#  调用testA函数，执行函数内部代码：声明和修改全局变量
testA()
#  调用testB函数，执行函数内部代码：打印
testB()


# 返回值作为传递参数
def test1():
    return 200


def test2(num):
    print(num)


result = test1()
test2(result)


# 函数的返回值
# 多返回值
def return_num():
    return 1, 2


result = return_num()  # 默认元组
print(result)


# 函数的参数
# 位置参数： 调用函数时根据函数定义的参数位置来传递参数，传递和定义参数的顺序及个数必须一致
# 注意：函数调用时,如果有位置参数时, 位置参数必须在关键字参数的前面, 但关键字参数之间不存在先后顺序
def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20, '男')


# 关键字参数：函数调用, 通过"键=值"形式加以制定
def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('Rose', age=20, gender='女')
user_info('小明', gender='男', age=16)


# 缺省参数：缺省参数也叫默认参数,用于定义函数, 为参数提供默认值, 调用函数时可不传该默认参数的值(注意: 所有位置参数必须出现在默认参数前, 包括函数定义和调用)
# 注意：函数调用时,如果为缺省参数传值则修改默认参数值; 否则使用这个默认值
def user_info(name, age, gender='男'):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20)
user_info('Rose', 18, '女')


# 不定长参数：不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时,可用包裹(packing)位置参数,或者包裹关键字参数, 来进行参数传递, 会显得非常方便
# 传进的所有参数都会被args变量收集, 它会根据传进参数的位置合并为一个元组(tuple),args是元组类型, 这就是包裹位置传递
# 包裹位置传递
def user_info(*args):
    print(args)


user_info('TOM')
user_info('TOM', 18)
list1 = [1, 2, 3]
user_info(*list1)


# 包裹关键字传递
def user_info(**kwargs):
    print(kwargs)


user_info(name='TOM', age=18, id=110)
dict1 = {'name': 'TOM', 'age': 18, 'id': 110}
## 传入字典必须带**
user_info(**dict1)


# 拆包和交换变量值
# 拆包：元组
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)
print(num2)


# 拆包：字典
def d1():
    dict1 = {'name': 'TOM', 'age': 18}
    a, b = dict1
    return a, b


# 对字典进行拆包，取出来的是字典的key
a, b = d1()
print(a)  # name
print(b)  # age
print(dict1[a])  # TOM
print(dict1[b])  # 18
