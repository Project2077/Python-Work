# 练习8-15：打印模型 　将示例printing_models.py中的函数放在一个名为
# printing_functions.py的文件中。在printing_models.py的开头编写一条
# import 语句，并修改该文件以使用导入的函数。
import printing_functions as pf


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


# 练习8-16：导入 选择一个你编写的且只包含一个函数的程序，将该函数放在
# 另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# 练习8-17：函数编写指南 　选择你在本章中编写的三个程序，确保它们遵循了
# 本节介绍的函数编写指南。


