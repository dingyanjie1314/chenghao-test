# 算数运算符：加减乘除整除取余指数小括号
# 加
jia = 1 + 2
print(jia)
# 减
jian = 3 - 1
print(jian)
# 乘
cheng = 3 * 2
print(cheng)
# 除
chu = 9 / 3
print(chu)
# 整除-取整
zhengchu = 9 // 2
print(zhengchu)
# 取余
quyu = 9 % 2
print(quyu)
# 指数-次方
zhishu = 2 ** 3
print(zhishu)
# 小括号-用来提高优先级
kuohao = (1 + 2) * 2
print(kuohao)

# 赋值运算：多个赋值
a, b, c = 1, 66, 99
print(a, b, c)
print(c)

# 复合赋值运算符
# +=：加法赋值运算符，c += a 等价于 c = c + a
a = 1
a += 2
print(a)
# -=:减法赋值运算符，c -= a 等价于 c = c - a
a = 5
a -= 1
print(a)
# *= 乘法赋值运算符 c *= a 等价于 c = c * a
a = 5
a *= 2
print(a)
# /= 除法赋值运算符 c /= a 等价于 c = c / a
a = 9
a /= 3
print(a)
# //= 整除赋值运算符 c //= a 等价于 c = c // a
a = 9
a //= 2
print(a)
# %= 取余赋值运算符 c %= a 等价于 c = c % a
a = 9
a %= 2
print(a)
# **= 幂赋值运算符 c ** = a 等价于 c = c ** a
a = 5
a **= 2
print(a)

# 比较运算符，用来判断，输出布尔值
# ==：判断相等。如果两个操作数的结果相等，则条件结果为真(True)，否则条件结果为假(False)
a, b = 3, 3
c, d = 3, 4
print(a == b)
print(c == d)
# !=不等于 。如果两个操作数的结果不相等，则条件为真(True)，否则条件结果为假(False)
aa, bb = 5, 6
cc, dd = 5, 5
print(aa != bb)
print(cc != dd)
# >运算符左侧操作数结果是否⼤于右侧操作数结果，如果⼤于，则条件为真，否则为假
aaa, bbb = 6, 5
ccc, ddd = 5, 5
print(aaa > bbb)
print(ccc > ddd)
# <运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假
aaaa, bbbb = 1, 2
cccc, dddd = 2, 1
print(aaa < bbbb)
print(cccc < dddd)

# >=运算符左侧操作数结果是否⼤大于等于右侧操作数结果，如果⼤大于，则条件为真，否则为假
a, b = 2, 1
c, d = 2, 2
e, f = 4, 5
print(a >= b)
print(c >= d)
print(e >= f)
# <=运算符左侧操作数结果是否⼩小于等于右侧操作数结果，如果⼩小于，则条件为真，否则为假
a, b = 1, 2
c, d = 5, 5
e, f = 5, 4
print(a <= b)
print(c <= d)
print(e <= f)

# 逻辑运算符：and or not
a = 1
b = 2
c = 3
# and：布尔"与"：x and y,如果 x 为 False， x and y 返回False，否则它返回 y 的值
print((a < b) and (b < c))
# or:布尔"或"：x or y,如果 x 是 True，它返回 True，否则它返回 y 的值
print((a > b) or (b < c))
# not：布尔"⾮非"：not x 如果 x 为 True，返回 False 。如果 x为 False，它返回 True
print(not (a > b))

a = 0
b = 1
c = 2
# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1
# or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or b)  # 1
print(a or c)  # 2
print(b or c)  # 1
