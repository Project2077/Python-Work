# 练习9-6：冰激凌小店 　冰激凌小店是一种特殊的餐馆。编写一个名为
# IceCreamStand 的类，让它继承为完成练习9-1或练习9-4而编写的
# Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那
# 个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰激凌组
# 成的列表。编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实
# 例，并调用这个方法。
from restaurant import Restaurant, User


class IceCreamStand(Restaurant):
    """冰淇淋小店 是 餐馆 的 一个子类"""

    def __init__(self, name, cuisine_type='ice_cream'):
        """初始化冰激凌小店。"""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """显示出售的冰激凌品种。"""
        print('\nWe have the following flavors available:')

        f = self.flavors
        for flavor in f:
            print(f"- {flavor.title()}")


Tom_home = IceCreamStand("Tom home")
# 直接 赋值
Tom_home.flavors = ['vanilla', 'chocolate', 'black cherry']
# 调用父类方法
Tom_home.describe_restaurant()
# show flavors
Tom_home.show_flavors()

# 练习9-7：管理员 　管理员是一种特殊的用户。编写一个名为Admin 的类，让
# 它继承为完成练习9-3或练习9-5而编写的User 类。添加一个名为
# privileges 的属性，用于存储一个由字符串（如"can add post" 、"can
# delete post" 、"can ban user" 等）组成的列表。编写一个名为
# show_privileges() 的方法，显示管理员的权限。创建一个Admin 实例，
# 并调用这个方法。
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []


    def show_privileges(self):
        """显示当前管理员的权限。"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
 'can reset passwords',
 'can moderate discussions',
 'can suspend accounts',
 ]
eric.show_privileges()



