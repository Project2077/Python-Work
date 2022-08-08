# 用户输入和while 循环

# 大多数程序旨在解决最终用户的问题，为此通常需要从用户那里获取一些信息。


# 函数input() 的工作原理
# 函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python
# 将其赋给一个变量，以方便你使用。
message = input("Tell me something, and I will repeat it back to you:")
print(message)

# 函数input() 接受一个参数——要向用户显示的提示 （prompt）或说明，让用户
# 知道该如何做。

# 在本例中，Python运行第一行代码时，用户将看到提示Tell me
# something, and I will repeat it back to you:
# 程序等待用户输
# 入，并在用户按回车键后继续运行。输入被赋给变量message ，接下来的
# print(message) 将输入呈现给用户

# 注意 　Sublime Text等众多编辑器不能运行提示用户输入的程序。你可以使用
# Sublime Text来编写提示用户输入的程序，但必须从终端运行它们。详情请参阅1.5节。
