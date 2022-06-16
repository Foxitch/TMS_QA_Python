import unittest
from functions import Validator

class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.validate = Validator()

    def test_validate_name_positive(self):
        name = self.validate.validate_name('Kristina Jigimont')
        assert name is None,\
            f'Expected validate_name_message is None, actual is {name}'

        name = self.validate.validate_name('Anton Ginko')
        assert name is None,\
            f'Expected validate_name_message is None, actual is {name}'

    @unittest.expectedFailure
    def test_validate_name_negative(self):
        name = self.validate.validate_name('')
        assert name is None, \
            f'Expected message is "You did not enter the name. ", actual is {name}'

        name = self.validate.validate_name('Anton    Ginko')
        assert name is None, \
            f'Expected message is "Name should not have more than one whitespace.", actual is {name}'

    def test_validate_age_positive(self):
        age = self.validate.validate_age(16)
        assert age is None,\
            f'Expected validate_age_message is None, actual is {age}'

        age = self.validate.validate_age(36)
        assert age is None, \
            f'Expected validate_age_message is None, actual is {age}'

    @unittest.expectedFailure
    def test_validate_age_negative(self):
        age = self.validate.validate_age('')
        assert age == '',\
            f'Expected validate_age_message is None, actual is {age}'

        age = self.validate.validate_age(-36)
        assert age == -36, \
            f'Expected validate_age_message is None, actual is {age}'

    def test_give_advice_positive(self):
        advice = self.validate.give_advice(16)
        assert advice == 'Do not forget to get your first passport. ',\
            f'Expected advice_message is "Do not forget to get your first passport. ", actual is {advice}'

        advice = self.validate.give_advice(45)
        assert advice == 'Do not forget to update your passport. ', \
            f'Expected advice_message is "Do not forget to update your passport. ", actual is {advice}'

    @unittest.expectedFailure
    def test_give_advice_negative(self):
        advice = self.validate.give_advice('')
        assert advice == 'Do not forget to get your first passport. ',\
            f'Expected advice_message is "Do not forget to get your first passport. ", actual is {advice}'

        advice = self.validate.give_advice(-45)
        assert advice == 'Do not forget to get your first passport. ', \
            f'Expected advice_message is "Do not forget to update your passport. ", actual is {advice}'


if __name__ == '__main__':
    unittest.TestCase()

