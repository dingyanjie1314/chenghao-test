# if
# 需求：如果⽤户年龄⼤于等于18岁，即成年，输出"已经成年，可以上网"
age = 19
if age > 18:
    print("已经成年，可以上网")

age = int(input("请输入你的年龄："))
if age > 18:
    print("已经成年，可以上网")
# if....else
# 需求：网吧上⽹的实例，如果成年，允许上网，如果不成年年呢？是不是应该回复⽤户不能上网
age = int(input("请输入你的年龄："))
if age > 18:
    print("已经成年，可以上网")
else:
    print("滚蛋")

# 多重判断：if...elif....elif(可以多个)...else
age = int(input('请输⼊您的年龄： '))
if age < 18:
    print(f'您的年龄是{age},童⼯一枚')
elif 18<=age<=60:
    print(f'您的年龄是{age},合法工龄')
elif age > 60:
    print(f'您的年龄是{age},可以退休')

#if嵌套
"""
1. 如果有钱，则可以上⻋
    2. 上⻋后，如果有空座，可以坐下
        上⻋后，如果没有空座，则站着等空座位
    如果没钱，不不能上⻋车
"""
# 假设⽤ money = 1 表示有钱, money = 0表示没有钱; seat = 1 表示有空座， seat = 0 表示没有空座
money=1
seat=0
if money==1:
    print("有钱请上车")
    if seat==1:
        print("还有座位，请坐下")
    else:
        print("请站着吧")
else:
    print("没钱，下车吧")

#三目运算
a=1
b=2
c= a if a>b else b
print(c)