# 有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
# 定义空字符串，用来接收superTest
str1 = ""
# 定义字符串welocme to super&Test
str2 = "welocme to super&Test"
# 用空格进行分割
list1 = str2.split(" ")
# 将list1循环
for i in list1:
    # 判断有&的数据，替换成空。添加到str1中
    if "&" in i:
        str1 = str1 + i.replace("&", "")
print(str1)
