import random
from random import randint, choice
# 练习9-13：骰子 　创建一个Die 类，它包含一个名为sides 的属性，该属性
# 的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之
# 间的随机数。创建一个6面的骰子再掷10次。

# 创建一个10面的骰子和一个20面的骰子，再分别掷10次。


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# die = Die()
#
# i = 0
# while i < 10:
#     die.roll_die()
#     i += 1
# 创建一个 6 面的骰子，再掷 10 次并显示结果。
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sided die:")
print(results)

d10 =Die(10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print("\n10 rolls of a 10-sided die:")
print(results)


# 练习9-14：彩票 　创建一个列表或元组，其中包含10个数和5个字母。从这个
# 列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4
# 个数或字母，就中大奖了。

# 可以放一块
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

# 中奖组合中不能包含重复的数或字母，因此使用了 while 循环。
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # 仅当摇出的数字或字母不在组合中时，才将其添加到组合中。
    if pulled_item not in winning_ticket:
        print(f" We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)






