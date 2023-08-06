import pdb
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # importing locators to search by ID or CSS selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_conditions
from selenium.webdriver.common.keys import Keys  # Enter pressing simulation
import urllib.parse
from selenium.common.exceptions import NoSuchElementException

PATH = r"C:\Program Files (x86)\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = PATH
driver_browser = webdriver.Chrome(options=chrome_options)

try:
    driver_browser.get(r"https://yandex.com/")  # -----------------------------------------
    time.sleep(5)
    wait = WebDriverWait(driver_browser, 10)

    menu_appearance = driver_browser.find_element(By.XPATH, r"//ul[@class='services-suggest__list']")
    try:
        if menu_appearance:
            try:
                images_menu = menu_appearance.find_element(By.CSS_SELECTOR, "[data-id='images']")
                EXPECTED_URL = r"https://yandex.com/images"
                expected_images_first_link_url = images_menu.get_attribute("href")
                if EXPECTED_URL in expected_images_first_link_url:
                    print(expected_images_first_link_url)
                    print(EXPECTED_URL)
                    print('Matches perfectly')
                else:
                    print(expected_images_first_link_url)
                    print(EXPECTED_URL)
                    print(r"the links aren't matching")
                # body > main > div.body__content > form > nav > ul > li:nth-child(2) > a
                # [data-id='images']
                # time.sleep(20)
                images_menu.click()
                # time.sleep(20)
                suggested_image_category = driver_browser.find_element(By.CLASS_NAME, r"PopularRequestList")
                # here we got the list of all categories of images
                first_images_category_suggested = suggested_image_category.find_element(By.XPATH, "./div[1]")
                first_images_category_suggested_name = first_images_category_suggested.text  # remembering name of category suggested
                first_images_category_suggested.click()
                # time.sleep(3)
                input_menu_text_checker = driver_browser.find_element(By.CLASS_NAME, r"input__control")
                # time.sleep(3)
                input_menu_text_checker_text = input_menu_text_checker.get_attribute("value")
                if first_images_category_suggested_name == input_menu_text_checker_text:
                    print("Names of category are matching")
                else:
                    pass
                waiter_of_images_from_first_category = wait.until(
                    exp_conditions.presence_of_element_located((
                        By.CLASS_NAME,
                        r"serp-item_pos_0"
                    ))
                )
                # url_remembering_of_first_image = waiter_of_images_from_first_category.find_element(By.CLASS_NAME, "serp-item__link").get_attribute("href")
                waiter_of_images_from_first_category.click()
                if waiter_of_images_from_first_category.is_displayed():
                    first_image_source = driver_browser.find_element(By.CLASS_NAME, "MMImage-Origin").get_attribute(
                        "src")
                    print('Yep it is indeed appeared')
                    time.sleep(5)
                    next_butto_definition = driver_browser.find_element(By.CLASS_NAME, "CircleButton_type_next")
                    next_butto_definition.click()
                    waiter_for_next_image_on_click = wait.until(
                        exp_conditions.presence_of_element_located((
                            By.CLASS_NAME,
                            "MMImage-Origin"
                        ))
                    )
                    swaped_image_url_rememberer = driver_browser.find_element(By.CLASS_NAME,
                                                                              "MMImage-Origin").get_attribute("src")
                    if (swaped_image_url_rememberer != first_image_source):
                        print("The image has swept")
                        previous_button_definition = driver_browser.find_element(By.CLASS_NAME,
                                                                                 "CircleButton_type_prev")
                        previous_button_definition.click()
                        current_image_source = driver_browser.find_element(By.CLASS_NAME,
                                                                           "MMImage-Origin").get_attribute("src")
                        if current_image_source == first_image_source:
                            print("We back to the first image we saw")
                        else:
                            print("This it not the the image we've been expecting")

                    else:
                        print("Image hasn't been swept")
                else:
                    pass

                time.sleep(15)

                #  "//ul[@class='PopularRequestList']" <-- class that contains list of all suggestions
            except NoSuchElementException:
                print('No such element as Images was suggested')
        else:
            raise NoSuchElementException
    except NoSuchElementException:
        print('No images menu has been found')
    # print(menu_appearance.text)

except:
    pass
finally:
    driver_browser.quit()  # -----------------------------------------

    # services-suggest__list
