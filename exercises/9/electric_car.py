# 练习9-9：电瓶升级 　在本节最后一个electric_car.py版本中，给Battery
# 类添加一个名为upgrade_battery() 的方法。该方法检查电瓶容量，如果不
# 是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法
# get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你将看
# 到这辆汽车的续航里程增加了。

class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


my_tesla = ElectricCar('tesla', 'model s', 2019)

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()

# 练习9-10：导入Restaurant 类 　将最新的Restaurant 类存储在一个模块
# 中。在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例并
# 调用Restaurant 的一个方法，以确认import 语句正确无误。
# from restaurant import Restaurant as re
#
# channel_club = re('the channel club', 'steak and seafood')
# channel_club.describe_restaurant()
# channel_club.open_restaurant()

# 练习9-11：导入Admin 类 　以为完成练习9-8而做的工作为基础。将User
# 类、Privileges 类和Admin 类存储在一个模块中，再创建一个文件，在其
# 中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切
# 都能正确运行。
# from privileges import Admin
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.privileges.show_privileges()

# 练习9-12：多个模块 　将User 类存储在一个模块中，并将Privileges 类
# 和Admin 类存储在另一个模块中。再创建一个文件，在其中创建一个Admin
# 实例并对其调用方法show_privileges() ，以确认一切依然能够正确运行。
from privileges import Privileges, Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.privileges.show_privileges()