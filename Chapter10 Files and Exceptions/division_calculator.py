# 异常
# Python使用称为异常 的特殊对象来管理程序执行期间发生的错误。每当发生让
# Python不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的
# 代码，程序将继续运行；如果未对异常进行处理，程序将停止并显示traceback，其
# 中包含有关异常的报告。

# 异常是使用try-except 代码块处理的。try-except 代码块让Python执行指定
# 的操作，同时告诉Python发生异常时怎么办。使用try-except 代码块时，即便出
# 现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的
# traceback。

# 处理ZeroDivisionError 异常
# 下面来看一种导致Python引发异常的简单错误。你可能知道，不能用数除以0，但还是让Python这样做
# print(5/0)
# ZeroDivisionError: division by zero

# 使用try-except 代码块
# 当你认为可能会发生错误时，可编写一个try-except 代码块来处理可能引发的异
# 常。你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常该怎么办。
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 将导致错误的代码行print(5/0) 放在一个try 代码块中。如果try 代码块中的
# 代码运行起来没有问题，Python将跳过except 代码块；如果try 代码块中的代码
# 导致了错误，Python将查找与之匹配的except 代码块并运行其中的代码。

# 使用异常避免崩溃
# 发生错误时，如果程序还有工作尚未完成，妥善地处理错误就尤其重要。这种情况
# 经常会出现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就
# 能再提示用户提供有效输入，而不至于崩溃。

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

a = True

while a:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    a = False
# 该程序没有采取任何处理错误的措施，因此在执行除数为0的除法运算时，它将崩溃
# 程序崩溃可不好，但让用户看到traceback也不是个好主意。不懂技术的用户会被搞
# 糊涂，怀有恶意的用户还会通过traceback获悉你不想他知道的信息。例如，他将知
# 道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的
# 攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。

# else 代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# 让Python尝试执行try 代码块中的除法运算，这个代码块只包含可能导致
# 错误的代码。依赖try 代码块成功执行的代码都放在else 代码块中。

# except 代码块告诉Python，出现ZeroDivisionError 异常时该如何办
# 如果try 代码块因除零错误而失败，就打印一条友好的消息，告诉用户如何
# 避免这种错误。程序继续运行，用户根本看不到traceback

"""
try-except-else 代码块的工作原理大致如下。Python尝试执行try 代码块中的
代码，只有可能引发异常的代码才需要放在try 语句中。有时候，有一些仅在try
代码块成功执行时才需要运行的代码，这些代码应放在else 代码块中。except
代码块告诉Python，如果尝试运行try 代码块中的代码时引发了指定的异常该怎么
办。
通过预测可能发生错误的代码，可编写健壮的程序。它们即便面临无效数据或缺少
资源，也能继续运行，从而抵御无意的用户错误和恶意的攻击。
"""





