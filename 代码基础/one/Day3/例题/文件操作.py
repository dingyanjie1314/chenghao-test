import os
# 文件操作
# 打开文件：. w和a模式: 如果文件不存在则创建该文件; 如果文件存在, w模式先清空再写入, a模式直接末尾追加
# f = open("test.txt", "w", encoding="utf-8")
f = open("test.txt", "r", encoding="utf-8")
# 文件写入内容
# f.write("hello world")
# read（num）：num表示要从文件中读取的数据的长度(单位是字节), 如果没有传入num,那么就表示读取文件中所有的数据
# print(f.read())
# readlines()：可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
# print(f.readlines())
#readline()一次读取一行内容
print(f"第一行为：{f.readline()}")
print(f"第二行为：{f.readline()}")

#seek():用来移动文件指针,文件对象.seek(偏移量,起始位置)
#起始位置：0文件开头，1当前位置，2文件结尾
#注意: 只有文件起始位置为0时,偏移量才能为非0整数
f.seek(0,2)
#tell(): 用来查看文件指针位置
print(f.tell())
# 关闭文件
f.close()
#文件备份
old_name="test.txt"
index=old_name.find(".")
new_name=old_name[:index]+"[备份]"+old_name[index:]
print(new_name)

old_f=open(old_name,"rb")
new_f=open(new_name,"wb")
while True:
    con=old_f.read()
    if len(con)==0:
        break
    new_f.write(con)
old_f.close()
new_f.close()

#文件和文件夹的操作
#文件重命名
# os.rename("name.txt","new_name.txt")
#删除文件
# os.remove("new_name.txt")
#创建文件夹
# os.mkdir("name_dir")
#删除文件夹
# os.rmdir("name_dir")
#获取当前目录
print(os.getcwd())
#改变文件默认目录
# os.chdir("../")
# print(os.getcwd())
#获取目录列表
print(os.listdir())
#获取文件所在目录:os.path.dirname( __file__ ):查看当前文件所属目录
print(os.path.dirname(__file__))