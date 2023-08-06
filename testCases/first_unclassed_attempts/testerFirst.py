import pdb
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # importing locators to search by ID or CSS selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_conditions
from selenium.webdriver.common.keys import Keys  # Enter pressing simulation
import urllib.parse

PATH = r"C:\Program Files (x86)\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = PATH
driver_browser = webdriver.Chrome(options=chrome_options)
try:
    driver_browser.get(r"https://yandex.com/")  # -----------------------------------------
    # inside this block we will perform actions from test
    time.sleep(15)
    search_filed_detection = driver_browser.find_element("id", "text")

    if search_filed_detection.is_displayed():

        search_filed_detection.send_keys("Тензор")

        wait = WebDriverWait(driver_browser, 10)  # we are waiting for suggestion field to appear

        suggestion_field = wait.until(
            exp_conditions.visibility_of_element_located((
                By.XPATH,
                "//ul[@class='mini-suggest__popup-content']"))
            # class="mini-suggest__popup-content" yandex suggest field class name
        )
        if suggestion_field.is_displayed():
            print('Yup there is the suggestion field')
            print(suggestion_field)
        else:
            print('No suggestion_field')

        search_filed_detection.send_keys(Keys.ENTER)  # pressing Enter anyway either suggestion field appeared or not
        # time.sleep(100)
        # class="main__content"
        try:
            search_page_appearance = wait.until(
                exp_conditions.presence_of_element_located((
                    By.ID,
                    "search-result"))
            )
        except TimeoutError as te:
            print(te)
        if search_page_appearance.is_displayed():
            expected_url = "https://tensor.ru/"
            first_result = search_page_appearance.find_element(By.XPATH, ".//li[1]//a")
            first_link_url = first_result.get_attribute("href")
            print("URL of the first search result:", first_link_url)
            if expected_url == first_link_url:
                print(f'URL matches the tensor.ru site')
        else:
            print('No result page found')
    else:
        print(f'there is no search field')
    time.sleep(10)
except TimeoutError as te:
    pdb.set_trace()
finally:
    driver_browser.quit()  # -----------------------------------------
