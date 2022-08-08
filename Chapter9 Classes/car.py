# 使用类和实例
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


# 给属性指定默认值
# 创建实例时，有些属性无须通过形参来定义，可在方法__init__() 中为其指定默认值。
class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值
# 出售时里程表读数为0的汽车不多，因此需要一种方式来修改该属性的值。
# 我们能以三种方式修改属性的值：直接通过实例进行修改，通过方法进行设置，以
# 及通过方法进行递增（增加特定的值）。

# 直接修改属性的值
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 通过方法修改属性的值
class Car1:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # 添加了方法update_odometer()
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。"""
        self.odometer_reading = mileage

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car1('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 现在，update_odometer() 在修改属性前检查指定的读数是否合理。如果新
# 指定的里程（mileage ）大于或等于原来的里程
# （self.odometer_reading ），就将里程表读数改为新指定的里程；否则发出警告，指出不能将里程表往回调
# def update_odometer(self, mileage):
#     """
#      将里程表读数设置为指定的值。
#      禁止将里程表读数往回调。
#      """
#     if mileage >= self.odometer_reading:
#         self.odometer_reading = mileage
#     else:
#         print("You can't roll back an odometer!")


# 通过方法对属性的值进行递增
# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。

# class Car:
#         --snip--
#     def update_odometer(self, mileage):
#         --snip--
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量。"""
#         self.odometer_reading += miles
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# 你可以轻松地修改这个方法，以禁止增量为负值，从而防止有人利用它来回调里程表。

# 注意 　你可以使用类似于上面的方法来控制用户修改属性值（如里程表读
# 数）的方式，但能够访问程序的人都可以通过直接访问属性来将里程表修
# 改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。

