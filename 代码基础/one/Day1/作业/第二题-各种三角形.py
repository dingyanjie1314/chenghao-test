# 第二题：正方形,三角形,九九乘法表
# while输出正方形
"""
1、使用input定义几行的正方形
2、定义初始值
3、循环条件
4、循环体：星号乘以定义的行数
5、循环加
"""
# 1、使用input定义几行的正方形
row = int(input("请输入要几行的正方形："))
# 2、定义初始值
i = 1
# 3、循环条件
while i <= row:
    # 4、循环体：星号乘以定义的行数
    print("*" * row)
    # 5、循环加
    i += 1
# for循环输出正方形
"""
1、使用input定义几行的正方形
2、for循环
3、星号乘以定义的行数
"""
# 1、使用input定义几行的正方形
row = int(input("请输入要几行的正方形："))
# 2、for循环
for i in range(row):
    # 3、星号乘以定义的行数
    print("*" * row)

# 三角形-左对齐
"""
*
**
***
****
规律：每行输出的为星号乘以行数
1、定义初始值1
2、循环体
3、每行输出的为星号乘以行数
4、循环加
"""
# while
# 1、定义初始值1
i = 1
# 2、循环体
row = int(input("输入几行左对齐三角形："))
while i <= row:
    # 3、每行输出的为星号乘以行数
    print("*" * i)
    # 4、循环加
    i += 1
# for
row = int(input("输入几行左对齐三角形："))
for i in range(1, row + 1):
    print("*" * i)

# 右对齐三角形
"""
   *
  **
 ***
****
规律：每行输出的为-空格*（总行数-第几行）+第几行*星号
1、定义初始值1
2、循环体
3、每行输出的为：空格*（总行数-第几行）+第几行*星号
4、循环加
"""
# while
# 1、定义初始值1
i = 1
# 2、循环体
row = int(input("输入几行右对齐三角形："))
while i <= row:
    # 3、每行输出的为：空格*（总行数-第几行）+第几行*星号
    print(" " * (row - i) + i * "*")
    # 4、循环加
    i += 1
# for
row = int(input("输入几行右对齐三角形："))
for i in range(1, row + 1):
    print(" " * (row - i) + i * "*")

# 三角形
"""
   *
  ***
 *****
*******
规律：每行输出的为-空格*（总行数-第几行）+（第几行*2*星号-1）
1、定义初始值1
2、循环体
3、每行输出的为：空格*（总行数-第几行）+（第几行*2-1)*星号
4、循环加

"""
# while
# 1、定义初始值1
i = 1
# 2、循环体
row = int(input("输入几行居中三角形："))
while i <= row:
    # 3、每行输出的为：空格*（总行数-第几行）+（第几行*2-1)*星号
    print(" " * (row - i) + (i * 2 - 1) * "*")
    # 4、循环加
    i += 1
# for
row = int(input("输入几行居中三角形："))
for i in range(1, row + 1):
    print(" " * (row - i) + (i * 2 - 1) * "*")

# 输出居中倒三角
row = int(input("输入几行居中倒三角形："))
for i in range(row, 0, -1):
    print(" " * (row - i) + (i * 2 - 1) * "*")
