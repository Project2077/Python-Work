# 导入类
# 随着不断给类添加功能，文件可能变得很长，即便妥善地使用了继承亦如此。为遵
# 循Python的总体理念，应让文件尽可能整洁。Python在这方面提供了帮助，允许将
# 类存储在模块中，然后在主程序中导入所需的模块。

# 导入单个类 from 类所存储的模块的名字 import 类名
from car_2 import Car2

my_new_car = Car2('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 在一个模块中存储多个类
# 见car_2的3个类

from car_2 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 从一个模块中导入多个类 用逗号分隔了各个类
from car_2 import Car2, ElectricCar

my_beetle = Car2('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# 导入整个模块
# 还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方式很简单，代
# 码也易于阅读。因为创建类实例的代码都包含模块名，所以不会与当前文件使用的任何名称发生冲突。
import car_2
my_beetle = car_2.Car2('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# 导入模块中的所有类
# 不推荐
# 第一，如果只看文件开头的import 语句，
# 就能清楚地知道程序使用了哪些类，将大有裨益。然而这种导入方式没有明确地指
# 出使用了模块中的哪些类。第二，这种方式还可能引发名称方面的迷惑。如果不小
# 心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
# from module_name import *   from car_2 import *

# 在一个模块中导入另一个模块
# 下面将Car 类存储在一个模块中，并将ElectricCar 类和Battery 类存储在另
# 一个模块中。将第二个模块命名为electric_car.py（这将覆盖前面创建的文件
# electric_car.py），并将Battery 类和ElectricCar 类复制到这个模块中

# electric_car.py
# """一组可用于表示电动汽车的类。"""
# from car import Car
# class Battery:
#     --snip--
# class ElectricCar(Car):
#     --snip--

# car.py
# """一个可用于表示汽车的类。"""
# class Car:
#     --snip--

# 现在可以分别从每个模块中导入类，以根据需要创建任何类型的汽车了：
# my_cars.py
# from car import Car
# from electric_car import ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())


# 使用别名
# 第8章说过，使用模块来组织项目代码时，别名大有裨益。导入类时，也可为其指定别名。
# 例如，要在程序中创建大量电动汽车实例，需要反复输入ElectricCar ，非常烦
# 琐。为避免这种烦恼，可在import 语句中给ElectricCar 指定一个别名：
from electric_car import ElectricCar as EC
my_tesla = EC('tesla', 'roadster', 2019)

"""
                        自定义工作流程
    如你所见，在组织大型项目的代码方面，Python提供了很多选项。熟悉所有这些选
项很重要，这样你才能确定哪种项目组织方式是最佳的，并能理解别人开发的项
目。
    一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一
切都能正确运行后，再将类移到独立的模块中。如果你喜欢模块和文件的交互方
式，可在项目开始时就尝试将类存储到模块中。先找出让你能够编写出可行代码的
方式，再尝试改进代码。

"""





