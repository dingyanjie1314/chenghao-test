# 第二题：求100以内能被3整除的数，并将作为列表输出
# 定义一个空列表
list1 = []
# 循环
for i in range(1, 101):
    # 判断取余为0追加到列表中
    if i % 3 == 0:
        list1.append(i)
print(list1)
