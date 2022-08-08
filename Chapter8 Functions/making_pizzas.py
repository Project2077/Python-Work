# 将函数存储在模块中
# 使用函数的优点之一是可将代码块与主程序分离。通过给函数指定描述性名称，可
# 让主程序容易理解得多。你还可以更进一步，将函数存储在称为模块 的独立文件
# 中，再将模块导入 到主程序中。import 语句允许在当前运行的程序文件中使用模
# 块中的代码。     import java里引包

# 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层
# 逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，
# 可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其
# 他程序员编写的函数库。

# 导入整个模块
# 要让函数是可导入的，得先创建模块。模块 是扩展名为.py的文件，包含要导入到
# 程序中的代码。下面来创建一个包含函数make_pizza() 的模块。为此，将文件
# pizza.py中除函数make_pizza() 之外的其他代码删除


import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Python读取这个文件时，代码行import pizza 让Python打开文件pizza.py，并将
# 其中的所有函数都复制到这个程序中。你看不到复制的代码，因为在这个程序即将
# 运行时，Python在幕后复制了这些代码。你只需知道，在making_pizzas.py中，可
# 使用pizza.py中定义的所有函数。

# 导入特定的函数

# 还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数
# from module_name import function_0, function_1, function_2

from pizza import make_pizza


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 使用这种语法时，调用函数时无须使用句点。由于在import 语句中显式地导入了
# 函数make_pizza() ，调用时只需指定其名称即可。

# 使用as 给函数指定别名
# 如果要导入函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指
# 定简短而独一无二的别名 ：函数的另一个名称，类似于外号。要给函数取这种特殊
# 外号，需要在导入它时指定。

from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# 指定别名的通用语法如下：
# from module_name import function_name as fn

# 使用as 给模块指定别名
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 给模块指定别名的通用语法如下：
# import module_name as mn

# 导入模块中的所有函数
# 使用星号（* ）运算符可让Python导入模块中的所有函数
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import 语句中的星号让Python将模块pizza 中的每个函数都复制到这个程序文件
# 中。由于导入了每个函数，可通过名称来调用每个函数，而无须使用句点表示法。
# 然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法。这是因为如
# 果模块中有函数的名称与当前项目中使用的名称相同，可能导致意想不到的结果：
# Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。

# 最佳的做法是，要么只导入需要使用的函数，要么导入整个模块并使用句点表示
# 法。这让代码更清晰，更容易阅读和理解。这里之所以介绍这种导入方法，只是想
# 让你在阅读别人编写的代码时，能够理解类似于下面的import 语句


