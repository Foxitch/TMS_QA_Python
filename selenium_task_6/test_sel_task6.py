from selenium_task_6.pages_for_task6 import PageForButtonClick6


class TestsForSelTask6:

    def test_switch_to_frame(self, setup):
        page = PageForButtonClick6(setup)

        page.get_iframe_btn()
        page.switch()
        assert page.get_text() == 'Your content goes here.', \
            f'Expected text is "Your content goes here.", actual is {page.get_text()}'




