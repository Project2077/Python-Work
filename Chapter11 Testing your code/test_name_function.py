"""
                    单元测试和测试用例
Python标准库中的模块unittest 提供了代码测试工具。单元测试 用于核实函数的
某个方面没有问题。测试用例 是一组单元测试，它们一道核实函数在各种情形下的
行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所
有这些情形的测试。全覆盖 的测试用例包含一整套单元测试，涵盖了各种可能的函
数使用方式。对于大型项目，要进行全覆盖测试可能很难。通常，最初只要针对代
码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。

"""

# 可通过的测试
# 你需要一段时间才能习惯创建测试用例的语法，但创建测试用例之后，再添加针对
# 函数的单元测试就很简单了。要为函数编写测试用例，可先导入模块unittest 和
# 要测试的函数，再创建一个继承unittest.TestCase 的类，并编写一系列方法对函数行为的不同方面进行测试。

# 下面的测试用例只包含一个方法，它检查函数get_formatted_name() 在给定名和姓时能否正确工作

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()


# 这个类可以随意命名，但最好让它看起来
# 与要测试的函数相关并包含Test 字样。这个类必须继承unittest.TestCase
# 类，这样Python才知道如何运行你编写的测试。

# NamesTestCase 只包含一个方法，用于测试get_formatted_name() 的一个方
# 面。将该方法命名为test_first_last_name() ，因为要核实的是只有名和姓的  test_what
# 姓名能否被正确格式化。运行test_name_function.py时，所有以test_ 打头的方
# 法都将自动运行。在这个方法中，调用了要测试的函数。在本例中，使用实
# 参'janis' 和'joplin' 调用get_formatted_name() ，并将结果赋给变量formatted_name

# unittest 类最有用的功能之一：断言 方法。断言方法核实得到的结果是否与期望的结果一致。
# 在这里，我们知道get_formatted_name() 应返回
# 名和姓首字母大写且之间有一个空格的姓名，因此期望formatted_name 的值为
# Janis Joplin 。为检查是否确实如此，我们调用unittest 的方法
# assertEqual() ，并向它传递formatted_name 和'Janis Joplin' 。

# 代码行self.assertEqual(formatted_name, 'Janis Joplin')
# 的意思是：“将formatted_name 的值与字符串'Janis Joplin' 比较。如果它
# 们相等，那么万事大吉；如果它们不相等，就告诉我一声！”

# 我们将直接运行这个文件，但需要指出的是，很多测试框架都会先导入测试文件再
# 运行。导入文件时，解释器将在导入的同时执行它。
# 最后的if 代码块检查特殊变量
# __name__ ，这个变量是在程序执行时设置的。
# ！！！ 如果这个文件作为主程序执行，变量__name__ 将被设置为'__main__' 。

# 在这里，调用unittest.main() 来运
# 行测试用例。！！！如果这个文件被测试框架导入，变量__name__ 的值将不
# 是'__main__' ，因此不会调用unittest.main() 。


# 添加新测试
class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
