# 列表推导式
# 创建一个0-10的列表
list1 = [i for i in range(11)]
print(list1)
# 创建0-10的偶数列表
list1 = [i for i in range(11) if i % 2 == 0]
print(list1)
# 创建一下列表[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)

# 字典推导式
# 两个列表合并成一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)
# 提取字典中的目标数据
# 需求：counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}，提取上述电脑数量大于等于200的字典数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count1 = {k: v for k, v in counts.items() if v >= 200}
print(count1)


#集合推导式
#创建一个集合,数据为下方列表的2次方，list1 = [1, 1, 2]
list1 = [1, 1, 2]
set1={i**2 for i in list1}
print(set1)
