# 练习10-11：喜欢的数 　编写一个程序，提示用户输入喜欢的数，并使用
# json.dump() 将这个数存储到文件中。再编写一个程序，从文件中读取这个
# 值，并打印如下所示的消息。
# I know your favorite number! It's _____.
import json


def favorite_number():
    num_prompt = "What's your favorite number? "
    number = input(num_prompt)
    number = int(number)
    with open("favorite_number.json", "w") as fn:
        json.dump(number, fn)

    print("Thanks! I'll remember that.")


def show_favorite_number():
    with open("favorite_number.json") as fn:
        num = json.load(fn)
        print(f"I know your favorite number! It's {num}.")


# favorite_number()
# show_favorite_number()


# 练习10-12：记住喜欢的数 　将练习10-11中的程序合二为一。如果存储了用户
# 喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件
# 中。运行这个程序两次，看看它能否像预期的那样工作。
def check_favorite_number():
    try:
        with open("favorite_number.json") as fn:
            num = json.load(fn)

    except FileNotFoundError:
        number = input("What's your favorite number? ")
        with open('favorite_number.json', 'w') as f:
            json.dump(number, f)
        print("Thanks, I'll remember that.")
    else:
        print(f"I know your favorite number! It's {num}.")


# check_favorite_number

# 练习10-13：验证用户 　最后一个remember_me.py版本假设用户要么已输入用
# 户名，要么是首次运行该程序。我们应该修改这个程序，以防当前用户并非上
# 次运行该程序的用户。

# 为此，在greet_user() 中打印欢迎用户回来的消息前，询问他用户名是否正
# 确。如果不对，就调用get_new_username() 让用户输入正确的用户名。

def get_stored_username():
    """获取存储的用户名——如果存储了。"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """基于用户名问候用户。"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        # else:
        #     username = get_new_username()
        #     print(f"We'll remember you when you come back, {username}!")
    # else:
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


greet_user()

# 你可能注意到了，在这个版本的 greet_user() 中，有两个相同的 else 代码块。要整
# 理这个函数，一种方法是使用空的 return 语句。空的 return 语句让 Python 离开当前函
# 数，不执行后面的代码。
# if username:
#   correct = input(f"Are you {username}? (y/n) ")
#   if correct == 'y':
#       print(f"Welcome back, {username}!")
#       return

# username = get_new_username()
# print(f"We'll remember you when you come back, {username}!")
