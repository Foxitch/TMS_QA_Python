import pytest
from homework_9.functions import Validator


@pytest.mark.regression
class TestFunctions:

    def __init__(self):
        self.validate = Validator()

    @pytest.mark.regression
    @pytest.mark.positive
    def test_validate_value_name_positive(self):
        name = self.validate.validate_name('Kristina Jigimont')
        assert name is None,\
            f'Expected validate_name_message is None, actual is {name}'

    @pytest.mark.regression
    @pytest.mark.negative
    def test_validate_value_name_negative(self):
        name = self.validate.validate_name('')
        assert name is None, \
            f'Expected message is "You did not enter the name. ", actual is {name}'

    @pytest.mark.regression
    @pytest.mark.positive
    def test_validate_age_positive(self):
        age = self.validate.validate_age(16)
        assert age is None,\
            f'Expected validate_age_message is None, actual is {age}'

    @pytest.mark.regression
    @pytest.mark.negative
    def test_validate_age_negative(self):
        age = self.validate.validate_age('')
        assert age == '',\
            f'Expected validate_age_message is None, actual is {age}'

    @pytest.mark.regression
    @pytest.mark.positive
    def test_give_advice_positive(self):
        advice = self.validate.give_advice(16)
        assert advice == 'Do not forget to get your first passport. ',\
            f'Expected advice_message is "Do not forget to get your first passport. ", actual is {advice}'

    @pytest.mark.regression
    @pytest.mark.negative
    def test_give_advice_negative(self):
        advice = self.validate.give_advice('')
        assert advice == 'Do not forget to get your first passport. ',\
            f'Expected advice_message is "Do not forget to get your first passport. ", actual is {advice}'

