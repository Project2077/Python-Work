# 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 下面的修改让你能存储年龄
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
# 在函数定义中，新增了一个可选形参age ，并将其默认值设置为特殊值None （表
# 示变量没有值）。可将None 视为占位值。在条件测试中，None 相当于False 。
# 如果函数调用中包含形参age 的值，这个值将被存储到字典中。在任何情况下，这
# 个函数都会存储人的姓名，但可进行修改，使其同时存储有关人的其他信息。


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# 结合使用函数和while 循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无限循环！
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# 但这个while 循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，
# 该在什么地方提供退出途径呢？要让用户能够尽可能容易地退出，因此每次提示用
# 户输入时，都应提供退出途径。每次提示用户输入时，都使用break 语句提供退出循环的简单途径
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
