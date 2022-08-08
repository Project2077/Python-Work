# 使用任意数量的关键字实参
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信
# 息。在这种情况下，可将函数编写成能够接受任意数量的键值对——调用语句提供
# 了多少就接受多少。一个这样的示例是创建用户简介：你知道将收到有关用户的信
# 息，但不确定会是什么样的信息。在下面的示例中，函数build_profile() 接受名和姓，还接受任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# 形参**user_info 中的两个星号让Python创建一个名为user_info
# 的空字典，并将收到的所有名称值对都放到这个字典中。


# 编写函数时，能以各种方式混合使用位置实参、关键字实参和任意数量的实参。知
# 道这些实参类型大有裨益，因为阅读别人编写的代码时经常会见到它们。要正确地
# 使用这些类型的实参并知道其使用时机，需要经过一定的练习。就目前而言，牢记
# 使用最简单的方法来完成任务就好了。继续往下阅读，你就会知道在各种情况下哪
# 种方法的效率最高。

# 注意 　你经常会看到形参名**kwargs ，它用于收集任意数量的关键字实参。 keywords arguments
