# 创建一个名为test_cities.py的程序，对刚才编写的函数进行测试（别忘了，
# 需要导入模块unittest 和要测试的函数）。编写一个名为
# test_city_country() 的方法，核实使用类似于'santiago' 和'chile'
# 这样的值来调用前述函数时，得到的字符串是正确的。运行test_cities.py，
# 确认测试test_city_country() 通过了。
import city_functions as cf
import unittest


# 你需要一段时间才能习惯创建测试用例的语法，但创建测试用例之后，再添加针对
# 函数的单元测试就很简单了。
class CitiesTestCase(unittest.TestCase):
    """测试 city_functions.py。"""

    def test_city_country(self):
        """核实使用类似于'santiago' 和'chile,
        这样的值来调用前述函数时，得到的字符串是正确的。'"""
        santiago = cf.city_country('santiago', 'chile')
        self.assertEqual(santiago, 'Santiago, Chile')

    def test_city_country_population(self):
        santiago = cf.city_country('santiago', 'chile', 5000000)
        self.assertEqual(santiago, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()

# 练习11-2：人口数量 　修改前面的函数，加上第三个必不可少的形参
# population ，并返回一个格式为 City , Country – population xxx
# 的字符串，如Santiago, Chile – population 5000000 。运行
# test_cities.py，确认测试test_city_country() 未通过。

# 修改上述函数，将形参population 设置为可选的。再次运行
# test_cities.py，确认测试test_city_country() 又通过了。

# 再编写一个名为test_city_country_population() 的测试，核实可以使
# 用类似于'santiago' 、'chile' 和'population=5000000' 这样的值来
# 调用这个函数。再次运行test_cities.py，确认测试
# test_city_country_population() 通过了。
