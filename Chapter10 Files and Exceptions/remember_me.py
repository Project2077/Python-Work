# 保存和读取用户生成的数据

# 使用json 保存用户生成的数据大有裨益，因为如果不以某种方式存储，用户的信
# 息会在程序停止运行时丢失。下面来看一个这样的例子：提示用户首次运行程序时
# 输入自己的名字，并在再次运行程序时记住他。
import json

username = input("What is your name? ")

filename = "username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")


# 重构
# 你经常会遇到这样的情况：代码能够正确地运行，但通过将其划分为一系列完成具
# 体工作的函数，还可以改进。这样的过程称为重构 。重构让代码更清晰、更易于理解、更容易扩展。

# 要重构remember_me.py，可将其大部分逻辑放到一个或多个函数中。
# remember_me.py的重点是问候用户，因此将其所有代码都放到一个名为
# greet_user() 的函数中

def greet_user():
    """问候用户，并指出其名字。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")


greet_user()


# 考虑到现在使用了一个函数，我们删除原注释，转而使用一个文档字符串来指出程序的作用
# 这个程序更加清晰，但函数greet_user() 所做的不仅仅是问
# 候用户，还在存储了用户名时获取它、在没有存储用户名时提示用户输入。
def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")


greet_user()
