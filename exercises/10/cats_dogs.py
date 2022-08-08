"""练习10-8：猫和狗 　创建文件cats.txt和dogs.txt，在第一个文件中至少存储
三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试
读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except
代码块中，以便在文件不存在时捕获FileNotFound 错误，并显示一条友好的
消息。将任意一个文件移到另一个地方，并确认except 代码块中的代码将正
确执行。"""
# with open("cats.txt", "a") as cats:
#     cats.write("henry\n")
#     cats.write("clarence\n")
#     cats.write("mildred\n")
# with open("dogs.txt", "a") as dogs:
#     dogs.write("willie\n")
#     dogs.write("annahootz\n")
#     dogs.write("summit\n")


# with open("cats.txt", "r") as cats:
#     lines = cats.readlines()
#     for line in lines:
#         print(f"{line.rstrip()}")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as fn:
            print(f"{fn.read()}")
    except FileNotFoundError:
        # print(" Sorry, I can't find that file.")
        pass

# 练习10-9：静默的猫和狗 　修改你在练习10-8中编写的except 代码块，让程
# 序在任意文件不存在时静默失败。


