# 练习10-1：Python学习笔记 　在文本编辑器中新建一个文件，写几句话来总结
# 一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。
# 将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程
# 序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三
# 次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时
# 将各行存储在一个列表中，再在with 代码块外打印它们。

filename = 'learning_python.txt'
print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
    print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())


# 练习10-2：C语言学习笔记 　可使用方法replace() 将字符串中的特定单词
# 都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的'dog'
# 替换为'cat' ：
# 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换
# 为另一门语言的名称，比如C。将修改后的各行都打印到屏幕上。
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
with open(filename) as f:
    lines = f.readlines()
# 方法readlines() 从文件中读取每一行，并将其存储在一个列表中。
for line in lines:
    # 删除行尾的换行符，再将 Python 替换为 C。
    line = line.rstrip()
    print(line.replace('Python', 'C'))


# 练习10-3：访客 　编写一个程序，提示用户输入名字。用户做出响应后，将其
# 名字写入文件guest.txt中。
msg = "What is your name? "
username = input(msg)

with open("guest.txt", "w") as gu:
    gu.write(username)

# 练习10-4：访客名单 　编写一个while 循环，提示用户输入名字。用户输入
# 名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件
# guest_book.txt中。确保这个文件中的每条记录都独占一行。
while True:
    msg = "What is your name，bro? "
    msg += "Enter 'quit' when you are finished."
    username = input(msg)
    if username == "quit":
        break
    print(f"Welcome,{username}")

    with open("guest_book.txt", "a") as gu:
        gu.write(f"Hi {username}, you've been added to the guest book.\n")


# 练习10-5：调查 　编写一个while 循环，询问用户为何喜欢编程。每当用户
# 输入一个原因后，都将其添加到一个存储所有原因的文件中。
answers = []
while True:
    question = "Why do you like programming? "

    answer = input(question)
    answers.append(answer)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != "y":
        break

with open("programming_poll.txt", "a") as p:
    for answer in answers:
        p.write(f"{answer}\n")




