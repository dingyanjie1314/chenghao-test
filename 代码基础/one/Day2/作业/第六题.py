# 有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
# 定义空的字符串用来接收不重复的数据
str1 = ""
# 定义字符串
str2 = "aabbbcddef"
# 循环字符串
for i in str2:
    # 判断每个字符如果大于1就是重复的,其他的直接添加到空的字符串中
    if str2.count(i) > 1:
        continue
    else:
        str1 += i

print(str1)
