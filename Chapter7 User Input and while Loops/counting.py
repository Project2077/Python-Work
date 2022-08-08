# while 循环简介

# for 循环用于针对集合中的每个元素都执行一个代码块，而while 循环则不断运
# 行，直到指定的条件不满足为止。

# 使用while 循环
# 可使用while 循环来数数。例如，下面的while 循环从1数到5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# 我们在其中定义了一个退出值 ，只要用户输入的不是这个值，程序就将接着运行

# 这个程序很好，唯一美中不足的是，它将单词'quit' 也作为一条消息打印了出
# 来。为修复这种问题，只需使用一个简单的if 测试

# 使用标志 flag

# 在前一个示例中，我们让程序在满足指定条件时执行特定的任务。但在更复杂的程
# 序中，很多不同的事件会导致程序停止运行。在这种情况下，该怎么办呢？
# 例如，有多种事件可能导致游戏结束，如玩家失去所有飞船、时间已用完，或者要
# 保护的城市被全部摧毁。导致程序结束的事件有很多时，如果在一条while 语句中
# 检查所有这些条件，将既复杂又困难。

# 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序
# 是否处于活动状态。这个变量称为标志 （flag），充当程序的交通信号灯。可以让
# 程序在标志为True 时继续运行，并在任何事件导致标志的值为False 时让程序停
# 止运行。这样，在while 语句中就只需检查一个条件：标志的当前值是否为True
# 。然后将所有其他测试（是否发生了应将标志设置为False 的事件）都放在其他地
# 方，从而让程序更整洁。


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # 这个就是flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 在循环中使用continue

# 要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue
# 语句，它不像break 语句那样不再执行余下的代码并退出整个循环。例如，来看一
# 个从1数到10但只打印其中奇数的循环：

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# continue 不执行余下的代码 返回while所在行 继续循环
# 1%2 != 0 故返回 2%2==0 故打印


# 避免无限循环
# 每个while 循环都必须有停止运行的途径，这样才不会没完没了地执行下去。   ！！！会卡死机的
x = 1
while x <= 5:
	print(x)
	x += 1 # 要是不加步长 这个循环就没完了