# 练习8-12：三明治 　编写一个函数，它接受顾客要在三明治中添加的一系列食
# 材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一
# 条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数
# 量的实参。


def make_sandwich(*items):
    """使用指定的食材制作三明治。"""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f" ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 练习8-13：用户简介 　复制前面的程序user_profile.py，在其中调用
# build_profile() 来创建有关你的简介。调用这个函数时，指定你的名和
# 姓，以及三个描述你的键值对。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# 练习8-14：汽车 　编写一个函数，将一辆汽车的信息存储在字典中。这个函数
# 总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：提
# 供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能
# 够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。


def make_car(manufacturer, model_name, **kwargs):
    """创建一个表示汽车的字典。"""
    car_dict = {
        "manufacturer": manufacturer.title(),
        "model_name": model_name,
    }
    for option, value in kwargs.items():
        car_dict[option] = value

    return car_dict


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 注：*是个列表 **是个字典
