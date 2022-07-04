from selenium_task_5.pages_for_task5 import PageForButtonClick5


class TestsForSelTask5:

    def test_checkbox(self, setup):
        page = PageForButtonClick5(setup)

        page.get_checkbox_click()
        page.get_remove_btn()
        assert page.get_its_gone_text() == "It's gone!", \
            f"Expected text is It's gone!, actual is {page.get_its_gone_text()}"
        assert page.validate_checkbox_is_disappeared() is True, 'Checkbox is not disappeared'

    def test_input_field(self, setup):
        page = PageForButtonClick5(setup)

        assert page.get_input_field().get_attribute("disabled") == "true", \
            "Input field does not have 'disabled' attribute"

        page.get_enable_btn()
        assert page.get_its_enabled_text() == "It's enabled!", \
            f"Expected text is It's enabled, actual is {page.get_its_enabled_text()}"

        assert page.get_input_field().get_attribute("disabled") is None, f"Input field is disabled"



