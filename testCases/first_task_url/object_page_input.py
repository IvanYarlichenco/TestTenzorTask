"""
time module for the captcha need
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp_conditions
from selenium.webdriver.support.wait import WebDriverWait


class YandexSearchPage:
    """
    driver for yandex page options
    """
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_yandex(self):
        """
        opening the yandex home page
        :return:
            no, simply navigate
        """
        self.driver.get(r"https://ya.ru/")
        time.sleep(5)

    def is_search_field_displayed(self):
        """
        detecting search field appearance on the page
        :return:
            True if displayed or False if not
        """
        search_field = self.driver.find_element(
            By.ID,
            "text"
        )
        return search_field.is_displayed()

    def enter_search_query(self, query):
        """
         taking the search field and sanding it text we want to
        :param query:
            the keys we want to send str or int  e.t.c
        :return:
            Web Element of search field
        """
        search_field = self.driver.find_element(
            By.ID,
            "text"
        )
        search_field.send_keys(query)
        return search_field

    def wait_for_suggestion_field(self):
        """
        expecting the suggestion filed to appear after sending the keys
        :return:
            Web element of field
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            exp_conditions.visibility_of_element_located((
                By.XPATH,
                "//ul[@class='mini-suggest__popup-content']"))
        )

    def press_enter(self):
        """
        Emulating Enter press with using import Keys
        :return:
            No, just sending keys to the field
        """
        search_field = self.driver.find_element(
            By.ID,
            "text"
        )
        search_field.send_keys(Keys.ENTER)

    def wait_for_search_results(self):
        """
        detecting a result of performed search query
        :return:
            Web element with all the results
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(exp_conditions.presence_of_element_located((
            By.ID,
            "search-result"))
        )

    def get_first_search_result_url(self):
        """
        Extracting the first result page and collecting a href link from it
        :return:
            String with href
        """
        search_page_appearance = self.driver.find_element(
            By.ID,
            "search-result"
        )
        first_result = search_page_appearance.find_element(
            By.XPATH,
            ".//li[1]//a"
        )
        return first_result.get_attribute("href")
