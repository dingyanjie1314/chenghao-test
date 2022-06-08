# 字符串：单引号、双引号，三引号
name = 'tom'
name1 = "tom"
name2 = '''tom'''
name3 = """tom"""
name4 = "i'm tom"
name5 = 'i\'m tom'
print(name5)
# 下标:从开始
name = "abcde"
print(name[1])
print(name[0])
print(name[2])
# 切片
name = "abcdefg"
print(name[2:5:1])  # cde
print(name[2:5])  # cde
print(name[:5])  # abcde
print(name[1:])  # bcdefg
print(name[:])  # abcdefg
print(name[::2])  # aceg
print(name[:-1])  # abcdef
print(name[-4:-1])  # def
print(name[::-1])  # gfedcba
# 查找
# find():检测某个⼦串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则返回-1
mystr = "hello world and superctest and chaoge and Python"
print(mystr.find('and'))  # 12
print(mystr.find("and", 15, 30))  # 27
print(mystr.find("ands"))  # -1
# index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则报异常
mystr = "hello world and superctest and chaoge and Python"
print(mystr.index('and'))  # 12
print(mystr.index("and", 15, 30))  # 27
# print(mystr.index("ands"))  # 报错
# count()：返回某个⼦串在字符串中出现的次数
mystr = "hello world and superctest and chaoge and Python"
print(mystr.count('and'))  # 3
print(mystr.count("ands"))  # 0
print(mystr.count("and", 0, 20))  # 1

# 修改
# replace（）：替换
mystr = "hello world and superctest and chaoge and Python"
print(mystr.replace("and", "he"))
print(mystr.replace("and", "he", 10))
print(mystr)
# split（）：按照指定字符串分割
mystr = "hello world and superctest and chaoge and Python"
print(mystr.split("and"))
print(mystr.split("and", 2))
print(mystr.split(" "))
print(mystr.split(" ", 2))
# join()：⽤用⼀个字符或⼦串合并字符串，即是将多个字符串合并为一个新的字符串
list1 = ['chao', 'ge', 'test', 'promotion']
t1 = ('aa', 'b', 'cc', 'ddd')
print('_'.join(list1))
print("...".join(t1))
# capitalize()：将字符串第⼀个字符转换成⼤写,其他的大写都转成小写
mystr = "hello world and superctest and chaoge and Python"
print(mystr.capitalize())
# capitalize()：将字符串第⼀个字符转换成大写
mystr = "hello world and superctest and chaoge and Python"
print(mystr.title())
# lower()：将字符串中大写转⼩写
mystr = "hello world and superctest and chaoge and Python"
print(mystr.lower())
# upper()：将字符串中小写转大写
mystr = "hello world and superctest and chaoge and Python"
print(mystr.upper())
# lstrip()：删除字符串左侧空白字符,rstrip()：删除字符串右侧空白字符,strip()：删除字符串两侧空⽩字符
mystr = "   hello world and superctest and chaoge and Python   "
print(mystr.lstrip())
print(mystr.rstrip())
print(mystr.strip())
# ljust()：返回一个原字符串左对齐,并使用指定字符(默认空格)填充⾄对应长度的新字符串,rjust()为右对齐
mystr = "hello"
print(mystr.ljust(10, "."))
print(mystr.ljust(10, ","))
# center()：返回一个原字符串居中对齐,并使用指定字符(默认空格)填充⾄对应长度的新字符串
mystr = "hello"
print(mystr.center(11))
print(mystr.center(11, ","))
# 判断
# startswith()：检查字符串是否是以指定子串开头，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查
mystr = "hello world and superctest and chaoge and Python"
print(mystr.startswith("hello"))
print(mystr.startswith("hello", 5, 20))
# endwith():检查字符串是否是以指定子串结尾，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查
mystr = "hello world and superctest and chaoge and Python"
print(mystr.endswith("Python"))
print(mystr.endswith("python"))
print(mystr.endswith("Python", 2, 20))
# isalpha()：如果字符串⾄至少有一个字符并且所有字符都是字⺟则返回True, 否则返回False
mystr1 = "hello"
mystr2 = "hello132"
mystr3 = "你好"
print(mystr1.isalpha())
print(mystr2.isalpha())
print(mystr3.isalpha())
# isdigit()：如果字符串只包含数字则返回True 否则返回False
mystr1 = "aaa123456"
mystr2 = "123456"
print(mystr1.isdigit())
print(mystr2.isdigit())
# isalnum()：如果字符串⾄至少有⼀个字符并且所有字符都是字⺟或数字则返回True,否则返回False
mystr1 = "aaaa111"
mystr2 = "1111_"
mystr3 = "123456"
print(mystr1.isalnum())
print(mystr2.isalnum())
print(mystr3.isalnum())
# isspace()：如果字符串中只包含空白，则返回True，否则返回False
mystr1 = "1 2 3"
mystr2 = "     "
print(mystr1.isspace())
print(mystr2.isspace())
