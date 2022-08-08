# 练习7-4：比萨配料 　编写一个循环，提示用户输入一系列比萨配料，并在用
# 户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，指
# 出我们会在比萨中添加这种配料。
message = "What do you want to add in your pizza? "
message += "\nif you want to quit,just enter 'quit'"

while True:
    pizza_c = input(message)
    if pizza_c == 'quit':
        break
    else:
        print(f"Thank for you order, the {pizza_c} will add to your pizza.")

# 练习7-5：电影票 　有家电影院根据观众的年龄收取不同的票价：不到3岁的观
# 众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。请编写一个
# 循环，在其中询问用户的年龄，并指出其票价。
active = ""

while True:
    age = input("How old are you? ")
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("free")
        elif age <12:
            print("10$")
        else:
            print("15$")

# 练习7-6：三种出路 　以不同的方式完成练习7-4或练习7-5，在程序中采取如下做法。

# 在while 循环中使用条件测试来结束循环。
# 使用变量active 来控制循环结束的时机。 ？
# 使用break 语句在用户输入'quit' 时退出循环。

# 练习7-7：无限循环 　编写一个没完没了的循环，并运行它（要结束该循环，
# 可按Ctrl + C，也可关闭显示输出的窗口）。
while True:
    print("I'm getting in!!!!!")


