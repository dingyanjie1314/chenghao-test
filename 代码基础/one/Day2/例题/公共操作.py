# 运算符
# 加
# 字符串
str1 = "a"
str2 = "b"
str3 = str1 + str2
print(str3)
# 列表
list1 = [1, 2]
list2 = ["a", "b"]
list3 = list1 + list2
print(list3)
# 元组
t1 = (1, 2)
t2 = ("a", "aa")
t3 = t1 + t2
print(t3)

# *
# 字符串
print("a" * 10)
# 列表
list1 = [1, 2]
print(list1 * 10)
# 元组
t1 = ("a", 2)
print(t1 * 10)

# in or not in
# 字符串
print("a" in "abc")
print("a" not in "abc")
# 列表
list1 = ["a", "b", "c"]
print("a" in list1)
print("a" not in list1)
# 元组
t1 = ("a", "b", "c")
print("a" in t1)
print("a" not in t1)

# len() 获取长度
# 字符串
str1 = "asdfghg"
print(len(str1))
# 列表
list1 = [1, 2, 3, 6, 4, 8]
print(len(list1))
# 元组
t1 = (1, 3, 5, 9, 4, 6)
print(len(t1))
# 集合
s1 = {1, 6, 8, 5, 3, 5, 8, 5}
print(len(s1))
# 字典
d1 = {"a": "a", "b": "b"}
print(len(d1))
t1 = (1, 3, 5, 9, 4, 6)

# del()
# 字符串
str1 = "asd"
del str1
# print(str1[1])报错  删除了
# 列表
list1 = [5, 6, 8, 5, 9, 5, 6, 8, 4, 6]
del list1[0]
print(list1)
# 集合
s1 = {1, 6, 8, 5, 5, 8}
s1.remove(6)
print(s1)

# max() 最大
str1 = "sadffdh"
print(max(str1))
list1 = [2, 8, 9, 6, 3, 77, 99]
print(max(list1))

# min() 最小
str1 = "sadffdh"
print(min(str1))
list1 = [2, 8, 9, 6, 3, 77, 99]
print(min(list1))

# range
for i in range(1, 10, 1):
    print(i)
for i in range(1, 10, 2):
    print(i)
for i in range(10):
    print(i)

#enumerate(),enumerate(可遍历对象,start=0),start参数用来设置遍历数据的下标的起始值, 默认为0
list1=[1,3,6,9,8,7,5,9]
for i in enumerate(list1):
    print(i)
for i,k in enumerate(list1):
    print(f"下标是{i}，对应数据为{k}")

#数据转换
#将序列转换成元组
list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}
print(tuple(list1))
print(tuple(s1))
#将序列转换成列表
t1 = ('a', 'b', 'c', 'd', 'e')
s1 = {100, 200, 300, 400, 500}
print(list(t1))
print(list(s1))
#将序列转成集合
list1 = [10, 20, 30, 40, 50, 20]
t1 = ('a', 'b', 'c', 'd', 'e')
print(set(list1))
print(set(t1))

