# 继承

# 编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，
# 可使用继承 。一个类继承 另一个类时，将自动获得另一个类的所有属性和方法。
# 原有的类称为父类 ，而新类称为子类 。子类继承了父类的所有属性和方法，同时
# 还可以定义自己的属性和方法。

# 子类的方法__init__()

# 在既有类的基础上编写新类时，通常要调用父类的方法__init__() 。这将初始化
# 在父类__init__() 方法中定义的所有属性，从而让子类包含这些属性。

# 例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此可在前面创建的Car
# 类的基础上创建新类ElectricCar 。这样就只需为电动汽车特有的属性和行为编写代码。
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
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


# 首先是Car 类的代码
# 创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 定义子类时，必须在圆括号内指定父类的名称。方法__init__() 接受创建Car 实例所需的信息
# class ElectricCar(Car) def __init__(self, make, model, year)

# super() 是一个特殊函数，让你能够调用父类的方法。这行代码让Python调
# 用Car 类的方法__init__() ，让ElectricCar 实例包含这个方法中定义的所
# 有属性。父类也称为超类 （superclass），名称super 由此而来

# 给子类定义属性和方法
# 让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。
# 下面来添加一个电动汽车特有的属性（电瓶），以及一个描述该属性的方法。我们
# 将存储电瓶容量，并编写一个打印电瓶描述的方法
class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 对于ElectricCar 类的特殊程度没有任何限制。模拟电动汽车时，可根据所需的
# 准确程度添加任意数量的属性和方法。如果一个属性或方法是任何汽车都有的，而
# 不是电动汽车特有的，就应将其加入到Car 类而非ElectricCar 类中。这样，使
# 用Car 类的人将获得相应的功能，而ElectricCar 类只包含处理电动汽车特有属
# 性和行为的代码。

# 重写父类的方法

# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写。为此，
# 可在子类中定义一个与要重写的父类方法同名的方法。这样，Python将不会考虑这
# 个父类方法，而只关注你在子类中定义的相应方法。

# 假设Car 类有一个名为fill_gas_tank() 的方法，它对全电动汽车来说毫无意
# 义，因此你可能想重写它。下面演示了一种重写方式
# class ElectricCar(Car):
#     --snip--
#     def fill_gas_tank(self):
#         """电动汽车没有油箱。"""
#         print("This car doesn't need a gas tank!")

# 将实例用作属性

# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清
# 单以及文件都越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一
# 个独立的类。可以将大型类拆分成多个协同工作的小类。

# 例如，不断给ElectricCar 类添加细节时，我们可能发现其中包含很多专门针对
# 汽车电瓶的属性和方法。在这种情况下，可将这些属性和方法提取出来，放到一个
# 名为Battery 的类中，并将一个Battery 实例作为ElectricCar 类的属性
class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=85):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 85:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
              初始化父类的属性。
              再初始化电动汽车特有的属性。
            """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 在ElectricCar 类中，添加了一个名为self.battery 的属性
# 这行代码让Python创建一个新的Battery 实例（因为没有指定容量，所以为默认值85），
# 并将该实例赋给属性self.battery 。每当方法__init__() 被调用时，都将执
# 行该操作，因此现在每个ElectricCar 实例都包含一个自动创建的Battery 实例。


# 下面再给Battery 类添加一个方法，它根据电瓶容量
# 报告汽车的续航里程 getrange()

# 模拟实物
# 模拟较复杂的物件（如电动汽车）时，需要解决一些有趣的问题。续航里程是电瓶
# 的属性还是汽车的属性呢？如果只描述一辆汽车，将方法get_range() 放在
# Battery 类中也许是合适的，但如果要描述一家汽车制造商的整个产品线，也许应
# 该将方法get_range() 移到ElectricCar 类中。在这种情况下，get_range()
# 依然根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。也可以这样
# 做：仍将方法get_range() 留在Battery 类中，但向它传递一个参数，如
# car_model 。在这种情况下，方法get_range() 将根据电瓶容量和汽车型号报告续航里程。

# 这让你进入了程序员的另一个境界：解决上述问题时，从较高的逻辑层面（而不是
# 语法层面）考虑；考虑的不是Python，而是如何使用代码来表示实物。达到这种境
# 界后，你会经常发现，对现实世界的建模方法没有对错之分。有些方法的效率更
# 高，但要找出效率最高的表示法，需要经过一定的实践。只要代码像你希望的那样
# 运行，就说明你做得很好！即便发现自己不得不多次尝试使用不同的方法来重写
# 类，也不必气馁。要编写出高效、准确的代码，都得经过这样的过程。


