# 查找
# 下标查找
list1 = ["tom", "lily", "rose"]
print(list1[0])
print(list1[1])
print(list1[2])
# index(): 返回指定数据所在位置的下标,不存在就报错
list1 = ["tom", "lily", "rose"]
print(list1.index("rose"))
# count(): 统计指定数据在当前列表中出现的次数
list1 = ["tom", "lily", "rose", "tom"]
print(list1.count("tom"))
# len(): 访问列表长度,即列表中数据的个数
list1 = ["tom", "lily", "rose", "tom"]
print(len(list1))
# in: 判断指定数据在某个列表序列,如果在返回True,否则返回False
list1 = ["tom", "lily", "rose", "tom"]
print("tom" in list1)
print("toms" in list1)
# not in: 判断指定数据不在某个列表序列,如果不在返回True, 否则返回False
print("tom" not in list1)
print("toms" not in list1)
# 需求: 查找用户输入的名字是否已经存在
list1 = ["tom", "lily", "rose", "tom"]
# name=input("请输入要查找的名字：")
# if name in list1:
#     print(f"输入的名字为{name}，存在")
# else:
#     print(f"输入的名字为{name}，不存在")

# 增加
# append(): 列表结尾追加数据,如果append()追加的数据是一个序列, 则追加整个序列到列表
list1 = ["tom", "lily", "rose", "tom"]
list1.append("jie")
print(list1)
list1.append([1, 2, 3])
print(list1)
# extend():列表结尾追加数据, 如果数据是一个序列,则将这个序列的数据逐一添加到列表
list1.extend("abc")
print(list1)
list1.extend([4, 5, 6])
print(list1)
# insert(): 指定位置新增数据
list1 = ["tom", "lily", "rose", "tom"]
list1.insert(0, "ding")
print(list1)
# 删除
# del ：加列表名字删除列表，加下标删除列表中的某个数据
del list1[1]
print(list1)
# pop(): 删除指定下标的数据(默认为最后一个),并返回该数据
list1 = ["tom", "lily", "rose", "tom"]
del_list = list1.pop()
print(del_list)
print(list1)
# remove(): 移除列表中某个数据的第一个匹配项
list1 = ["tom", "lily", "rose", "tom"]
list1.remove("tom")
print(list1)
# clear(): 清空列表
list1 = ["tom", "lily", "rose", "tom"]
list1.clear()
print(list1)
# 修改指定下标数据
list1 = ["tom", "lily", "rose", "tom"]
list1[3] = "tom1"
print(list1)
# 逆置: reverse()修改原始数据
list1 = [1, 2, 3, 6, 5]
list1.reverse()
print(list1)
# 逆置: reversed()此方法不会改变原始数据,获得结果为一个对象,需进行数据类型转化从而获得想要的数据类型
list1 = [1, 2, 3, 6, 5]
list2 = list(reversed(list1))
print(list1)
print(list2)
# 排序: sort()reverse表示排序规则, reverse=True降序, reverse = False升序(默认),此方法修改原始数据
list1 = [2, 6, 4, 3, 8, 6, 7]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
# 排序:sorted()此方法不会修改原始数据
list1 = [2, 6, 4, 3, 8, 6, 7]
list2 = sorted(list1, reverse=True)
print(list1)
print(list2)
# 复制copy（）
list1 = ["tom", "lily", "rose", "tom"]
list2 = list1.copy()
print(list1)
print(list2)
# 列表遍历
# while
list1 = ["tom", "lily", "rose", "tom"]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
# for
list1 = ["tom", "lily", "rose", "tom"]
for i in list1:
    print(i)
# 列表嵌套
name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
print(name_list[2][1])
