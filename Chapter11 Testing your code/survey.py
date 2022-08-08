# 测试类
# 在本章前半部分，你编写了针对单个函数的测试，下面来编写针对类的测试。很多
# 程序中都会用到类，因此证明你的类能够正确工作大有裨益。如果针对类的测试通
# 过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。

# 各种断言方法
# Python在unittest.TestCase 类中提供了很多断言方法。前面说过，断言方法检
# 查你认为应该满足的条件是否确实满足。如果该条件确实满足，你对程序行为的假
# 设就得到了确认，可以确信其中没有错误。如果你认为应该满足的条件实际上并不满足，Python将引发异常。

# 6个常用的断言方法:
# assertEqual(a, b)        核实a == b
# assertNotEqual(a, b)     核实a != b
# assertTrue(x)            核实x 为True
# assertFalse(x)           核实x 为False
# assertIn(item , list )   核实 item 在 list 中
# assertNotIn(item , list )核实 item 不在 list 中


# 一个要测试的类
# 类的测试与函数的测试相似，你所做的大部分工作是测试类中方法的行为。不过还是存在一些不同之处.
class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷。"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷。"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷。"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

# 这个类首先存储了一个调查问题，并创建了一个空列表，用于存储答案。

