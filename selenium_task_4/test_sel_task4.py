import time
from selenium_task_4.pages_for_task4 import PageForButtonClick4, PageForFeedBack4


class TestButtonClick:

    def test_button_click(self, setup):
        button_click = PageForButtonClick4(setup)

        button_click.open_url('https://ultimateqa.com/complicated-page/')
        button_click.get_click_button()


class TestFeedBackForm:

    def test_full_form(self, setup):
        form = PageForFeedBack4(setup)

        NAME = 'Alessya'
        MESSAGE = 'What is up, guys?'

        form.open_url('https://ultimateqa.com/filling-out-forms/')
        form.get_name_input_field().send_keys(NAME)
        form.get_message_input_field().send_keys(MESSAGE)
        time.sleep(3)
        form.get_submit_btn()
        text = form.get_successful_text().text
        assert text == 'Thanks for contacting us', f'Expected text is "Thanks for contacting us", actual is {text}'

    def test_name_only(self, setup):
        form = PageForFeedBack4(setup)

        NAME = 'Alessya'

        form.open_url('https://ultimateqa.com/filling-out-forms/')
        form.get_name_input_field().send_keys(NAME)
        time.sleep(3)
        form.get_submit_btn()
        text = form.get_please_fill().text
        assert text == 'Please, fill in the following fields:', \
            f'Expected text is "Please, fill in the following fields:", actual is {text}'

        color = form.get_message_input_field().value_of_css_property('border')
        assert color == '1px solid rgb(255, 0, 0)', \
            f'Expected messages input field is "1px solid rgb(255, 0, 0)", actual is {color}'

    def test_message_only(self, setup):
        form = PageForFeedBack4(setup)

        MESSAGE = 'What is up, guys?'

        form.open_url('https://ultimateqa.com/filling-out-forms/')
        form.get_message_input_field().send_keys(MESSAGE)
        time.sleep(3)
        form.get_submit_btn()
        text = form.get_please_fill().text
        assert text == 'Please, fill in the following fields:', \
            f'Expected text is "Please, fill in the following fields:", actual is {text}'

        color = form.get_name_input_field().value_of_css_property('border')
        assert color == '1px solid rgb(255, 0, 0)', \
            f'Expected messages input field is "1px solid rgb(255, 0, 0)", actual is {color}'




