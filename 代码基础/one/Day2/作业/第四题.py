# 第四题：求斐波那契数列 1 1 2 3 5 8 13 ……
"""
1、前两个数固定输出
2、从第三个数据开始为前两个数的和
"""
# 定义空列表用来接收数据
list1 = []
# 循环
for i in range(8):
    # 判断前两次循环直接往列表中追加1
    if i <= 1:
        list1.append(1)
    else:
        # 从第三个数据开始为前两个数的和
        list1.append(list1[len(list1) - 1] + list1[len(list1) - 2])
print(list1)
