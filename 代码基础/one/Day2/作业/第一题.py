from random import randint

# 第一题:有三个办公室，8位老老师，8位老师随机分配到3个办公室
# 定义8个老师
teacher = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8"]
# 定义三个空教室
classroom = [[], [], []]
# 循环老师
for i in teacher:
    # 获取随机教室
    classroom_random = randint(0, len(classroom) - 1)
    # 依次将老师分配至随机教室
    classroom[classroom_random].append(i)
print(classroom)
