# 返回值

# 函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数
# 返回的值称为返回值 。在函数中，可使用return 语句将值返回到调用函数的代码
# 行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

# 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
# 并非所有的人都有中间名，但如果调用这个函数时只提供了名和姓，它将不能正确运行。
# 为了让中间名变成可选的，可给形参middle_name 指定一个空的默认值，
# 并在用户没有提供中间名时不使用这个形参。为让get_formatted_name() 在没
# 有提供中间名时依然可行，可将形参middle_name 的默认值设置为空字符串，并
# 将其移到形参列表的末尾


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
# 如果没有提供中间名，middle_name 将为空字符串，导致if 测试
# 未通过，进而执行else 代码块

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john',  'hooker', 'lee')
print(musician)
