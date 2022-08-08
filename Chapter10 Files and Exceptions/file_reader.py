# 文件和异常
# 从文件中读取数据
# 读取整个文件
# 要读取文件，需要一个包含几行文本的文件。下面首先创建一个文件 pi_digits.txt
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
# print(contents.rstrip())

# 在这个程序中，第一行代码做了大量的工作。我们先来看看函数open() 。
# 要以任何方式使用文件，那怕仅仅是打印其内容，都得先打开 文件，才能访问它。函数
# open() 接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
# 函数open() 返回一个表示文件的对象。

# 关键字with 在不再需要访问文件后将其关闭。
# 在这个程序中，注意到我们调用了
# open() ，但没有调用close() 。也可以调用open() 和close() 来打开和关闭
# 文件，但这样做时，如果程序存在bug导致方法close() 未执行，文件将不会关
# 闭。这看似微不足道，但未妥善关闭文件可能导致数据丢失或受损。如果在程序中
# 过早调用close() ，你会发现需要使用文件时它已关闭 （无法访问），这会导致
# 更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前
# 面所示的结构，可让Python去确定：你只管打开文件，并在需要时使用它，Python
# 自会在合适的时候自动将其关闭。

# 使用方法read() 读取这个文件的全部内容，并将其作为一个长长的字符串赋给变量contents

# 相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空
# 行呢？因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出
# 来时就是一个空行。要删除多出来的空行，可在函数调用print() 中使用
# rstrip()


# 文件路径
# 将类似于pi_digits.txt的简单文件名传递给函数open() 时，Python将在当前执行
# 的文件（即.py程序文件）所在的目录中查找。
# 有时可能要打开不在程序文件所属目录中的文件。
with open('text_files/filename2.txt') as file_object2:
    contents = file_object2.read()
    print(contents)
# 注意 　显示文件路径时，Windows系统使用反斜杠（\ ）而不是斜杠（/ ），
# 但在代码中依然可以使用斜杠。

# 相对路径
# 绝对路径
# 相对文件路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。 如文件夹text_files位于文件夹python_work中
# 还可以将文件在计算机中的准确位置告诉Python，这样就不用关心当前运行的程序
# 存储在什么地方了。这称为绝对文件路径 。在相对路径行不通时，可使用绝对路径。
file_path = 'E:/python_work/text_files/filename2.txt'   # 绝对路径通常比相对路径长，因此将其赋给一个变量，再将该变量传递给open()会有所帮助
with open(file_path) as file_object3:
    contents = file_object3.read()
    print(contents)

# file_path = '/home/ehmatthes/other_files/text_files/_filename_.txt'
# with open(file_path) as file_object:
# 通过使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法
# 是，要么将数据文件存储在程序文件所在的目录，要么将其存储在程序文件所在目
# 录下的一个文件夹（如text_files）中。
# 注意 　如果在文件路径中直接使用反斜杠，将引发错误，因为反斜杠用于对字
# 符串中的字符进行转义。例如，对于路径"C:\path\to\file.txt" ，其中
# 的\t 将被解读为制表符。如果一定要使用反斜杠，可对路径中的每个反斜杠都
# 进行转义，如"C:\\path\\to\\file.txt" 。

# 逐行读取
# 读取文件时，常常需要检查其中的每一行：可能要在文件中查找特定的信息，或者
# 要以某种方式修改文件中的文本。例如，你可能要遍历一个包含天气数据的文件，
# 并使用天气描述中包含sunny字样的行。在新闻报道中，你可能会查找包含标签
# <headline> 的行，并按特定的格式设置它。

# 要以每次一行的方式检查文件，可对文件对象使用for 循环：
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        # print(line)
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
# 使用关键字with 时，open() 返回的文件对象只在with 代码块内可用。如果要
# 在with 代码块外访问文件的内容，可在with 代码块内将文件的各行存储在一个列
# 表中，并在with 代码块外使用该列表：可以立即处理文件的各个部分，也可以推迟到程序后面再处理。
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# 方法readlines() 从文件中读取每一行，并将其存储在一个列表中。接下
# 来，该列表被赋给变量lines 。在with 代码块外，依然可使用这个变量。



