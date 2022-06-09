# 第十题：有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
# 定义字符砖aabbbcddef
str1 = "aabbbcddef"
# 定义空字符串用来接收去重后的数据
str2 = ""
# 将字符创str1循环
for i in str1:
    # 判断如果字符在str2中就不添加，反之添加
    if i in str2:
        continue
    else:
        str2 += i
print(str2)
