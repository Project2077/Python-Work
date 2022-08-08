# 在函数中修改列表

# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修
# 改都是永久性的，这让你能够高效地处理大量数据。

# 来看一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列
# 表中，打印后将移到另一个列表中。下面是在不使用函数的情况下模拟这个过程的代码

# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 为重新组织这些代码，可编写两个函数，每个都做一件具体的工作。大部分代码与
# 原来相同，只是效率更高。第一个函数负责处理打印设计的工作，第二个概述打印了哪些设计
def print_models(unprinted_designs, completed_models):
    """
     模拟打印每个设计，直到没有未打印的设计为止。
     打印每个设计后，都将其移到列表completed_models中。
     """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他
# 设计，只需再次调用print_models() 即可。如果发现需要对打印代码进行修
# 改，只需修改这些代码一次，就能影响所有调用该函数的地方。与必须分别修改程
# 序的多个地方相比，这种修改的效率更高。

# 该程序还演示了这样一种理念：每个函数都应只负责一项具体的工作。第一个函数
# 打印每个设计，第二个显示打印好的模型。这优于使用一个函数来完成这两项工
# 作。编写函数时，如果发现它执行的任务太多，请尝试将这些代码划分到两个函数
# 中。别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分
# 成一系列步骤。


# 禁止函数修改列表
# 有时候，需要禁止函数修改列表。
# 为解决这个问题，可向函数传递列表的副本而非原件。这样，函数所做的任何修改都只影响副本，而原件丝毫不受影响。
# function_name(list_name_[:]) 利用切片创建该列表的副本
# 切片表示法[:] 创建列表的副本。在printing_models.py中，如果不想清空未打印
# 的设计列表，可像下面这样调用print_models()
print_models(unprinted_designs[:], completed_models)

# 虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由，否则还
# 是应该将原始列表传递给函数。这是因为让函数使用现成的列表可避免花时间和内
# 存创建副本，从而提高效率，在处理大型列表时尤其如此。

