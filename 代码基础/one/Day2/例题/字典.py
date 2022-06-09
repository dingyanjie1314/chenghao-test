# 字典
# 有数据
dict1 = {"name": "jie", "age": 25, "gender": "男"}
# 空字典
dict2 = {}
dict3 = dict()
print(dict1, dict2, dict3)
# 字典新增数据：如果key存在则修改这个key对应的值; 如果key不存在则新增此键值对
dict1 = {"name": "jie", "age": 25, "gender": "男"}
dict1["name"] = "ding"
dict1["id"] = 100
print(dict1)
# 删除：del()/del: 删除字典或删除字典中指定键值对
dict1 = {"name": "jie", "age": 25, "gender": "男"}
del dict1["age"]
print(dict1)
# clear(): 清空字典
dict1 = {"name": "jie", "age": 25, "gender": "男"}
dict1.clear()
print(dict1)
# 查找
# key查找
dict1 = {"name": "jie", "age": 25, "gender": "男"}
print(dict1["name"])
# get()
dict1 = {"name": "jie", "age": 25, "gender": "男"}
print(dict1.get("name"))
print(dict1.get("genderq", "没找到"))
# key（）
dict1 = {"name": "jie", "age": 25, "gender": "男"}
print(dict1.keys())
print(list(dict1.keys()))
# values()
print(dict1.values())
print(list(dict1.values()))
# items（）
print(dict1.items())
# 字符串遍历
# 遍历key
dict1 = {"name": "jie", "age": 25, "gender": "男"}
for i in dict1.keys():
    print(i)
# 遍历value
dict1 = {"name": "jie", "age": 25, "gender": "男"}
for i in dict1.values():
    print(i)
# 遍历字典元素
dict1 = {"name": "jie", "age": 25, "gender": "男"}
for i in dict1.items():
    print(i)
# 遍历字典键值对
dict1 = {"name": "jie", "age": 25, "gender": "男"}
for k, v in dict1.items():
    print(f"{k}={v}")
    print(k)
    print(v)
