import time
from selenium_task_2.page_for_task2 import PageForTask2
import pytest
from selenium.webdriver.support.ui import Select


@pytest.mark.regression
@pytest.mark.functional
class TestSelTask3:

    @pytest.mark.functional
    def test_select_fields(self, setup):
        task = PageForTask2(self.driver)

        task.get_select_value_field().click()
        task.get_group_1_option_2_value()

        task.get_select_one_field()
        task.get_dr_value()

        old_style_select_value = Select(task.get_old_style_field())
        old_style_select_value.select_by_index(3)

        standard_multi_field = Select(task.get_standard_multi_field())
        standard_multi_field.select_by_value('saab')
