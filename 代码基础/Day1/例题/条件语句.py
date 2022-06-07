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
