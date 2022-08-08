# 为核实get_formatted_name() 像期望的那样
# 工作，我们来编写一个使用该函数的程序。程序names.py让用户输入名和姓，并显示整洁的姓名

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
# 从上述输出可知，合并得到的姓名正确无误。现在假设要修改
# get_formatted_name() ，使其还能够处理中间名。这样做时，要确保不破坏这
# 个函数处理只含有名和姓的姓名的方式。为此，可在每次修改
# get_formatted_name() 后都进行测试：运行程序names.py，并输入像Janis
# Joplin这样的姓名。不过这太烦琐了。所幸Python提供了一种自动测试函数输出的
# 高效方式。倘若对get_formatted_name() 进行自动测试，就能始终确信当提供
# 测试过的姓名时，该函数都能正确工作。
