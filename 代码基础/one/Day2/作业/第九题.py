# 有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
# 定义字符串abcdef
str1 = "abcdef"
# 定义空字符串用来接收到倒序字符串
str2 = ""
# 定义空列表将字符串str1逐个追加到列表中
list1 = []
# 将字符串str1逐个追加到列表中
for i in str1:
    list1.append(i)
# 将列表数据首位相换
for n in range(len(list1) // 2):
    list1[n], list1[-n - 1] = list1[-n - 1], list1[n]
# 列表数据添加到空字符串中
for j in list1:
    str2 += j
print(str2)
