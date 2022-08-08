# 练习9-15：彩票分析 　可以使用一个循环来明白前述彩票大奖有多难中奖。为
# 此，创建一个名为my_ticket 的列表或元组，再编写一个循环，不断地随机
# 选择数或字母，直到中大奖为止。请打印一条消息，报告执行循环多少次才中了大奖。
from random import choice


def get_winning_ticket(possibilities):
    """摇出中奖组合。"""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # 仅当摇出的数字或字母不在组合中时，才将其添加到组合中。
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # 检查彩票的每个数字或字母，只要有一个不在中奖组合中，就返回 False。
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    # 如果代码执行到这里，就说明中奖了！
    return True


def make_random_ticket(possibilities):
    """随机地生成彩票。"""
    ticket = []
    # 彩票不能包含重复的数字或字母，因此使用了 while 循环。
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        # 仅当随机生成的数字或字母不在彩票中时，才将其添加到彩票中。
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)


plays = 0
won = False

# 为避免程序执行时间太长，设置最多随机生成多少张彩票。
max_tries = 1_000_000

while not won:
     new_ticket = make_random_ticket(possibilities)
     won = check_ticket(new_ticket, winning_ticket)
     plays += 1
     if plays >= max_tries:
        break

if won:
     print("We have a winning ticket!")
     print(f"Your ticket: {new_ticket}")
     print(f"Winning ticket: {winning_ticket}")
     print(f"It only took {plays} tries to win!")
else:
     print(f"Tried {plays} times, without pulling a winner. :(")
     print(f"Your ticket: {new_ticket}")
     print(f"Winning ticket: {winning_ticket}")

# 练习9-16：Python Module of the Week 　要了解Python标准库，一个很不错
# 的资源是网站Python Module of the Week。请访问该网站并查看其中的目录，
# 找一个你感兴趣的模块进行探索。从模块random 开始可能是个不错的选择。
