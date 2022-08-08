# 测试AnonymousSurvey 类

# AnonymousSurvey 类可用于进行简单的匿名调查。假设我们将它放在了模块
# survey 中，并想进行改进：让每位用户都可输入多个答案；编写一个方法，只列
# 出不同的答案并指出每个答案出现了多少次；再编写一个类，用于管理非匿名调查。

# 进行上述修改存在风险，可能影响AnonymousSurvey 类的当前行为。例如，允许
# 每位用户输入多个答案时，可能会不小心修改处理单个答案的方式。要确认在开发
# 这个模块时没有破坏既有行为，可以编写针对这个类的测试。

# 下面来编写一个测试，对AnonymousSurvey 类的行为的一个方面进行验证：如果
# 用户面对调查问题只提供一个答案，这个答案也能被妥善地存储。为此，我们将在
# 这个答案被存储后，使用方法assertIn() 来核实它确实在答案列表中

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

# 前述做法的效果很好，但这些测试有些重复的地方。下面使用unittest 的另一项
# 功能来提高其效率。
# 方法setUp()
# 在前面的test_survey.py中，我们在每个测试方法中都创建了一个
# AnonymousSurvey 实例，并在每个方法中都创建了答案。unittest.TestCase
# 类包含的方法setUp() 让我们只需创建这些对象一次，就能在每个测试方法中使
# 用。如果在TestCase 类中包含了方法setUp() ，Python将先运行它，再运行各
# 个以test_ 打头的方法。这样，在你编写的每个测试方法中，都可使用在方法setUp() 中创建的对象。


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""

    def setUp(self):
        """
         创建一个调查对象和一组答案，供使用的测试方法使用。
         """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
