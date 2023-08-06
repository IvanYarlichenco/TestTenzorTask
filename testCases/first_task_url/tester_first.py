import unittest

from selenium import webdriver

from object_page_input import *

PATH = r"C:\Program Files (x86)\chromedriver.exe"


class TestYandexSearch(unittest.TestCase):
    """
    main action performance
    """
    def setUp(self):
        """
        setting the web driver settings
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = PATH
        self.driver = webdriver.Chrome(options=chrome_options)
        self.yandex_page = YandexSearchPage(self.driver)  # from object_page_input.py

    def test_search_and_verify_first_result(self):
        """
         sending Тензор to search field and comparing results
         if first result and his link directs to the tensor.ru site we good
        :return:
            Static
        """
        self.yandex_page.navigate_to_yandex()

        if self.yandex_page.is_search_field_displayed():
            print("There is search field")
            self.yandex_page.enter_search_query("Тензор")
            suggestion_field = self.yandex_page.wait_for_suggestion_field()
            if suggestion_field.is_displayed():
                print('Yup there is the suggestion field')
                print(suggestion_field)
            else:
                print('No suggestion_field')

            self.yandex_page.press_enter()
            time.sleep(10)

            try:
                search_page_appearance = self.yandex_page.wait_for_search_results()
            except TimeoutError as timeout_ex:
                print(timeout_ex)

            if search_page_appearance.is_displayed():
                print("result page appeared")
                expected_url = "https://tensor.ru/"
                first_link_url = self.yandex_page.get_first_search_result_url()
                print("URL of the first search result:", first_link_url)
                if expected_url == first_link_url:
                    print('URL matches the tensor.ru site')
                else:
                    print(r"The ffirst page isn't matching the tensor site limk")
            else:
                print('No result page found')
        else:
            print('there is no search field')

    def tearDown(self):
        """
        tearing driver work
        :return:
            No
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
