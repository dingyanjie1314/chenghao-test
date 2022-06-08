# float（），转换成浮点
num1 = 1
print(float(num1))
print(type(float(num1)))

# str（）转换成字符串
num = 1
print(str(num))
print(type(str(num)))

# tuple()转成成元组
list1 = [1, 2, 3, 4]
print(tuple(list1))
print(type(tuple(list1)))

# list()转成列表
tuple1 = (1, 2, 3, 4)
print(list(tuple1))
print(type(list(tuple1)))

# eval 将字符串串中的数据转换成Python表达式原本类型
str1 = "1"
str2 = "[1,2,3]"
str3 = "(1,2,3)"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
