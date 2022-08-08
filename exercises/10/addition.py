# 练习10-6：加法运算 　提示用户提供数值输入时，常出现的一个问题是，用户
# 提供的是文本而不是数。在此情况下，当你尝试将输入转换为整数时，将引发
# ValueError 异常。编写一个程序，提示用户输入两个数，再将其相加并打印
# 结果。在用户输入的任何一个值不是数时都捕获ValueError 异常，并打印一
# 条友好的错误消息。对你编写的程序进行测试：先输入两个数，再输入一些文
# 本而不是数。
"""try:
num_1 = input("Enter a number")
num_2 = input("ENter a number")
num_1 = int(num_1)
num_2 = int(num_2)
except ValueError:
print("Sorry, I really needed a number.")
else:
print(num_1+num_2)"""

# 练习10-7：加法计算器 　将为完成练习10-6而编写的代码放在一个while 循
# 环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。
while True:
    try:
        num_1 = input("Enter a number")
        num_2 = input("ENter a number")
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:

        print("Sorry, I really needed a number.")
    else:
        print(num_1+num_2)

