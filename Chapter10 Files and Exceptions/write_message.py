# 写入文件

# 保存数据的最简单的方式之一是将其写入文件中。通过将输出写入文件，即便关闭
# 包含程序输出的终端窗口，这些输出也依然存在：可以在程序结束运行后查看这些
# 输出，可以与别人分享输出文件，还可以编写程序来将这些输出读取到内存中并进行处理。

# 写入空文件
# 要将文本写入文件，你在调用open() 时需要提供另一个实参，告诉Python你要写
# 入打开的文件。为明白其中的工作原理，我们来将一条简单的消息存储到文件中，
# 而不是将其打印到屏幕上
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# 第一个实参也是要打开的文件的名称。
# 第二个实参（'w' ）告诉Python，要以写入模式 打开这个文件。
# 打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或
# 读写模式 （'r+' ）。如果省略了模式实参，Python将以默认的只读模式打开文件。

# 如果要写入的文件不存在，函数open() 将自动创建它。然而，以写入模式（'w'
# ）打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件的内容。

# 使用文件对象的方法write() 将一个字符串写入文件。这个程序没有终端
# 输出，但如果打开文件programming.txt，将看到其中包含如下一行内容 I love programming

# 相比于计算机中的其他文件，这个文件没有什么不同。你可以打开它、在其中输入
# 新文本、复制其内容、将内容粘贴到其中，等等。

"""
注意 　Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，
必须先使用函数str() 将其转换为字符串格式。

"""

# 写入多行
# 函数write() 不会在写入的文本末尾添加换行符，因此如果写入多行时没有指定换
# 行符，文件看起来可能不是你希望的那样：
filename = 'programming.txt'
with open(filename, 'w') as file_object:
     file_object.write("I love programming.")
     file_object.write("I love creating new games.")
# I love programming.I love creating new games. 两行内容挤在一起
# 要让每个字符串都单独占一行，需要在方法调用write() 中包含换行符：
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件
# 如果要给文件添加内容，而不是覆盖原有的内容，可以以附加模式 打开文件。以附
# 加模式打开文件时，Python不会在返回文件对象前清空文件的内容，而是将写入文
# 件的行添加到文件末尾。如果指定的文件不存在，Python将为你创建一个空文件。
with open(filename,"a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
# 内容附加到文件末尾，而不是覆盖文件原来的内容
