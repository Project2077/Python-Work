# 练习9-8：权限 　编写一个名为Privileges 的类，它只有一个属性
# privileges ，其中存储了练习9-7所述的字符串列表。将方法
# show_privileges() 移到这个类中。在Admin 类中，将一个Privileges
# 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges()
# 来显示其权限。
from restaurant import User


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """显示当前管理员的权限。"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
 'can reset passwords',
 'can moderate discussions',
 'can suspend accounts',
 ]

# Privileges()方法的属性  实例作为属性 要得到是属性(实例)的属性  ..
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
