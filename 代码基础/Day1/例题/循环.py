# while循环
# 需求：初始值是0次，终点是5次，重复做的事情输出“媳妇⼉， 我错了”
i = 0
while i < 5:
    print("媳妇，我错了")
    i += 1
# 需求：1-100的累加和，即1 + 2 + 3 + 4 +….，即前两个数字的相加结果 + 下⼀个数字( 前⼀个数字 +1)
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)
# 需求：1-100的偶数相加
# 方法1
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)
# 方法2
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(result)

# break应用:终止循环
i = 1
while i < 5:
    if i == 3:
        print(f"这是第{i}个苹果，吃饱了不吃了")
        break
    print(f"这是第{i}个苹果")
    i += 1
# contniue:退出当前循环继续下一次循环
i = 1
while i < 5:
    if i == 3:
        print(f"这是第{i}个苹果，有虫子不吃了")
        i += 1
        continue
    print(f"这是第{i}个苹果")
    i += 1

# while 嵌套
i = 0
while i < 3:
    j = 0
    while j < 3:
        print("媳妇我错了")
        j += 1
    print("刷碗")
    print("一套惩罚结束----")
    i += 1
# 星号正方形
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("*", end=" ")
        j += 1
    print()
    i += 1
# 星号打印三角形
i = 1
while i < 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}", end='\t')
        j += 1
    print()
    i += 1

#for循环
str1="hello"
for i in str1:
    print(i)
#for循环值break
str2="hello"
for i in str2:
    if i=="e":
        print("遇到e退出循环")
        break
    print(i)
#for循环值continue
str2="hello"
for i in str2:
    if i=="e":
        print("遇到e不打印，退出本次循环")
        continue
    print(i)

#while...else
i=0
while i<5:
    print("媳妇我错了")
    i+=1
else:
    print("媳妇原谅我了")

#while...else...break
i=0
while i<5:
    if i==3:
        print("道歉不真诚")
        break
    print("媳妇我错了")
    i+=1
else:
    print("媳妇原谅我了")

#while...else...continue
i=0
while i<5:
    if i==3:
        print("道歉不真诚")
        i+=1
        continue
    print("媳妇我错了")
    i+=1
else:
    print("媳妇原谅我了")

#for...else
str1="hello"
for i in str1:
    print(i)
else:
    print("循环完执行的代码")
#for...else...break
str1="hello"
for i in str1:
    if i=="e":
        print("遇到e停止循环")
        break
    print(i)
else:
    print("循环完执行的代码")

#for...else...continue
str1="hello"
for i in str1:
    if i=="e":
        print("遇到e终止本次循环")
        continue
    print(i)
else:
    print("循环完执行的代码")
