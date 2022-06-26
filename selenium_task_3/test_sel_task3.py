import time
from selenium_task_3.page_for_task3 import PageForTask3
import pytest


@pytest.mark.regression
@pytest.mark.functional
class TestSelTask3:

    @pytest.mark.functional
    def test_input_fields_and_click_submit_btn(self, setup):
        first_name = 'Nataly'
        last_name = 'Smirnova'
        phone = '+375254455325'
        email = 'n.smirnova@mail.com'

        address = 'Main Street 123'
        city = 'NY'
        state = 'NY'
        postal_code = '12345'

        user_name = 'Smirnova'
        password = 'qweasd123'
        confirm_password = 'qweasd123'

        task = PageForTask3(self.driver)
        task.get_first_name_input_field().send_keys(first_name)
        task.get_last_name_input_field().send_keys(last_name)
        task.get_phone_input_filed().send_keys(phone)
        task.get_email_input_field().send_keys(email)

        task.get_address_input_filed().send_keys(address)
        task.get_city_input_field().send_keys(city)
        task.get_state_input_filed().send_keys(state)
        task.get_postal_code_input_value().send_keys(postal_code)

        task.get_user_name_input_field().send_keys(user_name)
        task.get_password_input_value().send_keys(password)
        task.get_confirm_password_input_value().send_keys(confirm_password)
        task.get_submit_btn()

        first_last_name_result = task.get_result_first_last_name().text
        user_name_result = task.get_result_user_name().text

        assert first_last_name_result == f'Dear {first_name} {last_name},',\
            f"Expected first_last_name text is 'Dear {first_name} and {last_name},' actual is {first_last_name_result}"

        assert user_name_result == f'Note: Your user name is {user_name}.',\
            f"Expected user_name text is ' Note: Your user name is {user_name}.', actual is {user_name_result}"
