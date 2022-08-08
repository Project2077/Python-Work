# 练习5-8：以特殊方式跟管理员打招呼 　创建一个至少包含5个用户名的列表，
# 且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都
# 打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
users = ['admin', 'asd', 'dfd', 'eafsd', 'gfgd']

# 如果用户名为'admin' ，就打印一条特殊的问候消息，如下所示。
# Hello admin, would you like to see a status report?
# 否则，打印一条普通的问候消息，如下所示。
# Hello Jaden, thank you for logging in again.
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# 练习5-9：处理没有用户的情形 　在为完成练习5-8编写的程序中，添加一条
# if 语句，检查用户名列表是否为空。
# 如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有用户名，确定将打印正确的消息。
while users:
    users.pop()
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")


# 练习5-10：检查用户名 　按下面的说明编写一个程序，模拟网站如何确保每位
# 用户的用户名都独一无二。

# 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
current_users = ['admin', 'asd', 'dfd', 'DGDFD', 'gfgd']
current_users_lower = [current_user.lower() for current_user in current_users]
print(current_users_lower)
# 再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中
# 有一两个用户名也包含在列表current_users 中。
new_users = ['admin', 'asd', 'alien', 'james', 'mike']
# 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使
# 用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一
# 条消息，指出这个用户名未被使用。
for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")
# 确保比较时不区分大小写。换句话说，如果用户名'John' 已被使用，应
# 拒绝用户名'JOHN' 。（为此，需要创建列表current_users 的副本，
# 其中包含当前所有用户名的小写版本。）

# 练习5-11：序数 　序数表示位置，如1st和2nd。序数大多以th结尾，只有1、2
# 和3例外。
# 在一个列表中存储数字1～9。
numbers = range(1, 10)
# 遍历这个列表。
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输
# 出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th" ，但每个序
# 数都独占一行。


# 练习5-12：设置if 语句的格式 审核你在本章编写的程序，确保正确地设置
# 了条件测试的格式。

"""
练习5-13：自己的想法 　与刚拿起本书时相比，现在你是一名能力更强的程序
员了。鉴于你对如何在程序中模拟现实情形有了更深入的认识，可以考虑使用
程序来解决一些问题了。随着编程技能不断提高，你可能想解决一些问题，请
将这方面的想法记录下来。想想你可能想编写的游戏、想研究的数据集以及想
创建的Web应用程序。

"""
