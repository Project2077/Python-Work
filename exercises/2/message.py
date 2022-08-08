# Chapter2 练习

# 练习2-1：简单消息 　将一条消息赋给变量，并将其打印出来。
message = 'Hello World!'
print(message)
# 练习2-2：多条简单消息 　将一条消息赋给变量，并将其打印出来；
# 再将变量的值,修改为一条新消息，并将其打印出来。
message = 'Hello Python World!'
print(message)

# 练习2-3：个性化消息 　用变量表示一个人的名字，并向其显示一条消息。显示的
# 消息应非常简单，下面是一个例子。
# Hello Eric, would you like to learn some Python today?
name = 'Eric'
print(f"Hello {name}, would you like to learn some Python today?")
# 练习2-4：调整名字的大小写 　用变量表示一个人的名字，再以小写、大写和首字
# 母大写的方式显示这个人名。
print(name.lower())
print(name.upper())
print(name.title())
# 练习2-5：名言 　找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出
# 应类似于下面这样（包括引号）。
# Albert Einstein once said, “A person who never made a mistake nevertried anything new.”
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")
# 练习2-6：名言2 　重复练习2-5，但用变量famous_person 表示名人的姓名，再
# 创建要显示的消息并将其赋给变量message ，然后打印这条消息。
famous_person = 'Albert Einstein'
message = f"{famous_person} once said, “A person who never made a mistake never tried anything new.”"
print(message)
# 练习2-7：剔除人名中的空白 　用变量表示一个人的名字，并在其开头和末尾都包
# 含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、
# rstrip() 和strip() 对人名进行处理，并将结果打印出来。
name = '          \n\tAlbert Einstein       '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 练习2-8：数字8 　编写四个表达式，分别使用加法、减法、乘法和除法运算，但结
# 果都是数字8。为使用函数调用print() 来显示结果，务必将这些表达式用圆括号
# 括起来。也就是说，你应该编写四行类似于下面的代码：
# print(5+3)  输出应为四行，其中每行都只包含数字8。
print(2+6)
print(9-1)
print(2*4)
print(int(16/2))
# 练习2-9：最喜欢的数 　用一个变量来表示你最喜欢的数，再使用这个变量创建一
# 条消息，指出你最喜欢的数是什么，然后将这条消息打印出来。
favorite_number = 1
print(f"My favorite number is {favorite_number}")

# 练习2-10：添加注释 　选择你编写的两个程序，在每个程序中至少添加一条注释。
# 如果程序太简单，实在没有什么需要说明的，就在程序文件开头加上你的姓名和当
# 前日期，再用一句话阐述程序的功能。
# 获得用户输入的最喜欢的数并将其输出 输入q退出
while True:
    message = 'What is your favorite number?'
    message += '\nif your want exit,just enter q'
    favorite_number = input(message)
    if favorite_number == 'q':
        break
    else:
        print(f"My favorite number is {favorite_number}")
# 练习2-11：Python之禅 　在Python终端会话中执行命令import this ，并粗略
# 地浏览一下其他的指导原则。
import this



