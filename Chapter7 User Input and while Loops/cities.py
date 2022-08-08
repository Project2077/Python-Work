# 使用break 退出循环

# 要立即退出while 循环，不再运行循环中余下的代码，也不管条件测试的结果如
# 何，可使用break 语句。break 语句用于控制程序流程，可用来控制哪些代码行
# 将执行、哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。

# 例如，来看一个让用户指出他到过哪些地方的程序。在这个程序中，可在用户输
# 入'quit' 后使用break 语句立即退出while 循环：

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# 注意 　在任何Python循环中都可使用break 语句。例如，可使用break 语句
# 来退出遍历列表或字典的for 循环。