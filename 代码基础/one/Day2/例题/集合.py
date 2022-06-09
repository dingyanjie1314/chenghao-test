# 创建集合
s1 = {"a", 1, 6, 8, 6, 7}
s2 = set("a123456")
# 空集合
s3 = set()
print(s1)
print(s2)
print(s3)
# 添加数据：add（）
# 集合有去重功能,  当向集合内追加的数据是当前集合已有数据的话, 则不进行任何操作。
s1 = {10, 20, 30}
s1.add(40)
s1.add(20)
print(s1)
# update():追加的是序列
s1 = {10, 20}
s1.update([100, 200])
s1.update('abc')
print(s1)
# 删除数据
# remove(), 删除集合中的指定数据,如果数据不存在则报错
s1 = {100, 'b', 200, 10, 'c', 'a', 20}
s1.remove("a")
print(s1)
# discard(), 删除集合中的指定数据, 如果数据不存在也不会报错
s1 = {100, 'b', 200, 10, 'c', 'a', 20}
s1.discard("a")
s1.discard(1000)
print(s1)
# pop(), 随机删除集合中的某个数据, 并返回这个数据
s1 = {100, 'b', 200, 10, 'c', 'a', 20}
s1_pop = s1.pop()
print(s1_pop)
print(s1)
# 判断
# in: 判断数据在集合序列
# not in: 判断数据不在集合序列
s1 = {100, 'b', 200, 10, 'c', 'a', 20}
print(100 in s1)
print(100 not in s1)
