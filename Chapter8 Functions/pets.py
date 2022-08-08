# 传递实参

# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递
# 实参的方式很多：可使用位置实参 ，这要求实参的顺序与形参的顺序相同；也可使
# 用关键字实参 ，其中每个实参都由变量名和值组成；还可使用列表和字典。下面依次介绍这些方式。

# 位置实参
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形
# 参。为此，最简单的关联方式是基于实参的顺序。这种关联方式称为位置实参 。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
# 多次调用
describe_pet('dog', 'willie')

# 位置实参的顺序很重要
# 使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料
describe_pet("ami", "cat")

# 关键字实参
# 关键字实参 是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所
# 以向函数传递实参时不会混淆

# 关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
describe_pet(animal_type='hamster', pet_name='harry')


# 默认值
# 编写函数时，可给每个形参指定默认值 。在调用函数中给形参提供了实参时，
# Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认
# 值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地
# 指出函数的典型用法。

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
describe_pet('willie', 'cat')
# 注意 　使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有
# 默认值的实参。这让Python依然能够正确地解读位置实参。 pet_name, animal_type='dog' not animal_type='dog', pet_name

# 等效的函数调用
# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式
def describe_pet(pet_name, animal_type='dog'):
    # 一条名为Willie的小狗。
    describe_pet('willie')
    describe_pet(pet_name='willie')
    # 一只名为Harry的仓鼠。
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')
# 注意 　使用哪种调用方式无关紧要，只要函数调用能生成你期望的输出就行。
# 使用对你来说最容易理解的调用方式即可。  以上调用结果没差别

# 避免实参错误
# 等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多
# 于或少于函数完成工作所需的信息时，将出现实参不匹配错误。
