# 第一题：人和电脑的石头剪刀布
"""
1、人是human，输入的，石头是1、剪刀是2、布是3
2、电脑是computer，电脑随机出，使用random模块
3、比较出是人赢还是电脑赢
    3.1如果人是1电脑是2或者人是2电脑3或者人是3电脑是1则是人赢
    3.2如果人等于电脑，则是平局
    3.3 其他的是电脑赢
"""
from random import randint

# 1、人是human，输入的，石头是1、剪刀是2、布是3
human = int(input("请输入：石头是1、剪刀是2、布是3："))
# 2、电脑是computer，电脑随机出，使用random模块
computer = randint(1, 3)
print(computer)
# 3、比较出是人赢还是电脑赢
# 3.1如果人是1电脑是2或者人是2电脑3或者人是3电脑是1则是人赢
if (human == 1 and computer == 2) or (human == 2 and computer == 3) or (human == 3 and computer == 1):
    print("人类赢了")
# 3.2如果人等于电脑，则是平局
elif human == computer:
    print("平局")
# 3.3 其他的是电脑赢
else:
    print("电脑赢了")