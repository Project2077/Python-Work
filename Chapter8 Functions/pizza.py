# 传递任意数量的实参
# 有时候，预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中
# 收集任意数量的实参。

# 例如，来看一个制作比萨的函数，它需要接受很多配料，但无法预先确定顾客要多
# 少种配料。下面的函数只有一个形参*toppings ，但不管调用语句提供了多少实
# 参，这个形参会将它们统统收入囊中
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参
# 放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 注意 　你经常会看到通用形参名*args ，它也收集任意数量的位置实参。




