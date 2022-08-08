# 下面的练习比第2章的练习要复杂些，但让你有机会以前面介绍过的各种方式使用列表。

# 练习3-4：嘉宾名单 　如果你可以邀请任何人一起共进晚餐（无论是在世的还
# 是故去的），你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请
# 的人，然后使用这个列表打印消息，邀请这些人来与你共进晚餐。
guests = ['mike', 'jojo', 'karen']
print(f"I want to have a dinner with my best friends, Do you have any time? {guests[0].title()}")
print(f"and {guests[1].title()}, How about you")
print(f"Maybe {guests[2].title()} also have time for this")

# 练习3-5：修改嘉宾名单 　你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，
# 指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print(f"I have spoke with {guests[2].title()}, unfortunately,She have something important to deal with")
guests[2] = "jill"
print(f"So I invited {guests[2].title()}")

# 添加嘉宾 　你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想
# 想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条
# print 语句，指出你找到了一个更大的餐桌。
print(f"\nI found a bigger table, Maybe we can invite more friends")
# 使用insert() 将一位新嘉宾添加到名单开头。
guests.insert(0, "Jean Valjean")
# 使用insert() 将另一位新嘉宾添加到名单中间。
guests.insert(1, "Einstein")
# 使用append() 将最后一位新嘉宾添加到名单末尾。
guests.append("milulu")
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
for guest in guests:
    message = f"Do you have time for a dinner, {guest}"
    print(message)

# 练习3-7：缩减名单 　你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条
# 你只能邀请两位嘉宾共进晚餐的消息。
print("\nbecause of Newly purchased tables cannot be delivered in time, I'm afraid only two guests can be invited")
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名
# 单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
poped_guests = []
print(len(guests))
while len(guests) > 2:
    """
    通过循环不断剔除嘉宾
    直到嘉宾列表只剩两人
    """
    uninvited = guests.pop()
    poped_guests.append(uninvited)
    print(f"Sorry {uninvited}, I can't invite you")

print(poped_guests)
print(guests)
# 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
for guest in guests:
    print(f"{guest}, you can still join the dinner")
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，
# 核实程序结束时名单确实是空的。
while guests:
    del guests[-1]

print(guests)


