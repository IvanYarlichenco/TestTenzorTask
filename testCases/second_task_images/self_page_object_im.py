from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_conditions
from selenium.webdriver.support.ui import WebDriverWait


# def raise_error_and_where(function):
#     NE = NoSuchElementException
#     print('Error has occurred  at {function().__name__} :{NE}')


class HomePage:
    """
    On the start menu page
    """

    def __init__(self, driver):
        self.driver = driver

    def on_input_field_click(self):
        """
        detecting search field appearance on the page
        :return:
            True if displayed or False if not
        """
        search_field = self.driver.find_element(
            By.ID,
            "text"
        )
        search_field.click()

    def all_menu_click(self):

        more_menu_detector = WebDriverWait(self.driver, 10).until(exp_conditions.element_to_be_clickable(
            self.driver.find_element(
                By.CLASS_NAME,
                "services-suggest__item-more"))
        )
        if more_menu_detector:
            more_menu_detector.click()
            print('there is menu in deed')

    def open_yandex(self):

        self.driver.get("https://ya.ru/")
        # self.driver.get("https://yandex.com/")
        WebDriverWait(self.driver, 10)

    def is_image_menu_appeared(self):
        """
        This function collects information on suggesting a list
        it's displayed on the start page on yandex
        we are detecting if there is a class which represents this menu exists on page

        :return:
            web element that contains class with items on the suggesting menu

        """
        try:
            menu_appearance = self.driver.find_element(
                By.XPATH,
                "//ul[@class='services-suggest__list']"
            )
            return menu_appearance
        except NoSuchElementException as no_element:
            return f"{no_element}"

    def pop_up_menu_detector(self):
        """
        here we will be detecting popup menu after pressing All
        and try to find images menu
        :return:
            Web Element
        """
        more_popup_menu = WebDriverWait(self.driver, 10).until(
            exp_conditions.presence_of_element_located((
                By.CLASS_NAME,
                "services-more-popup__section-content")))
        return more_popup_menu

    def click_menu_images(self):
        """
        This function simply clicks on suggesting menu item by id
        on input we are getting function is_image_menu_appeared,
        so we can check if there is menu at all we are getting
        :return:
            No returns static function
        """

        on_menu_appeared = self.pop_up_menu_detector()
        # we should specify the name of category in case it's a different browser language
        desired_aria_label = "Картинки"  # IMPORTANT!!!
        # desired_aria_label = "Images"
        xpath_expression = f"//a[@aria-label='{desired_aria_label}']"
        images_menu = WebDriverWait(self.driver, 10).until(
            exp_conditions.element_to_be_clickable(on_menu_appeared.find_element(
                By.XPATH,
                xpath_expression

            )))
        if self.image_menu_proper_link(images_menu):
            images_menu.click()
            print('We are on the yandex image page')

    def image_menu_proper_link(self, element_with_link):
        """
        comparing images URL in case we need to compare if we are on image site
        :return:
            True or False if they are match or not
        """

        expected_url = r"https://ya.ru/images/"
        # expected_images_first_link_url = element_with_link
        expected_images_first_link_url = element_with_link.get_attribute("href")
        if expected_url in expected_images_first_link_url:
            return True

    def switched_window_detector(self):
        """
        Here we are letting the driver instructions to change the tab we're currently going to on
        :return:
            No
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])


class ImagePage:
    """
    On the image menu page
    """

    def __init__(self, driver):
        self.driver = driver



    def comparing_names_of_input_and_category_name(self, first_category_name):
        """
        Here we must compare image category name and text that appeared on input field
        it's for the sake of checking if we are on the right category that we are expecting
        :param first_category_name:
        :return:
            returns True if names are matching or False if they don't
        """
        input_menu_text_checker = self.driver.find_element(
            By.CLASS_NAME,
            r"input__control")
        input_menu_text_checker_text = input_menu_text_checker.get_attribute("value")
        if input_menu_text_checker_text == first_category_name:
            return True

    def is_suggested_image_category_appeared(self):
        """
        When we are clicking on category we are checking
        if there are images appeared below the input field
        :return:
            Web element  that contains all  elements on the page that appeared
        """
        try:
            suggested_image_category = self.driver.find_element(
                By.CLASS_NAME,
                "PopularRequestList"
            )
            return suggested_image_category
        except NoSuchElementException as no_element:
            return f"{no_element}"

    def get_first_suggested_image_category_name(self):
        """
        From all images that have been suggested we must extract the first one
        extracting by taking first block from web element
        :return:
            text that is the name of first element on the page
        """
        suggested_image_category = self.driver.find_element(
            By.CLASS_NAME,
            "PopularRequestList")
        first_images_category_suggested = suggested_image_category.find_element(
            By.XPATH,
            "./div[1]")
        return first_images_category_suggested.text

    def click_first_suggested_image_category(self):
        """
        after we get the web element we must proceed to the image by clicking on it
        here we are copy pasting code and not using the find elements
        by PopularRequestList and div[1] so we aren't depending on parameters
        :return:
            No return simply static clicker
        """
        suggested_image_category = self.driver.find_element(
            By.CLASS_NAME,
            "PopularRequestList")
        first_images_category_suggested = suggested_image_category.find_element(
            By.XPATH,
            "./div[1]")
        first_images_category_suggested.click()


class ImageViewerPage:
    """
    On the image viewer page
    """

    def __init__(self, driver):
        self.driver = driver

    def is_image_viewer_displayed(self):
        """
        we are want to get the result if there is indeed imgae from category we need the first one
        collecting by class name
        :return:
         Web element that is the first image of category
        """
        try:
            waiter_of_images_from_first_category = WebDriverWait(self.driver, 10).until(
                exp_conditions.presence_of_element_located((
                    By.CLASS_NAME,
                    "serp-item_pos_0"))
            )
            return waiter_of_images_from_first_category
        except NoSuchElementException as no_element:
            return f"{no_element}"

    def click_on_image_viewer_displayed(self):
        """
        simply click on what we want to
        in this case is result of the is_image_viewer_displayed function
        :return:
            No returns simply clicker
        """
        click_on_item = self.is_image_viewer_displayed()
        click_on_item.click()

    def get_image_source(self):
        """
        Inside this function we are collecting the src of images
        and some more we are performing right click because i have found
        some strange behaviour: when we are clicking right click we are
        getting the absolute src and not temporary which is collecting if we are
        not performing right click
        :return:
            String which is SRC of image
        """
        action_chains = ActionChains(self.driver)
        action_chains.context_click(self.driver.find_element(
            By.CLASS_NAME,
            "MMImage-Origin")).perform()
        first_image_source = self.driver.find_element(
            By.CLASS_NAME,
            "MMImage-Origin").get_attribute("src")
        return first_image_source

    def click_next_button(self):
        """
        finding the button which is arrow on image viewer on yandex view page
        NEXT one
        :return:
            No simply clicker
        """
        next_button_definition = self.driver.find_element(
            By.CLASS_NAME,
            "CircleButton_type_next")
        next_button_definition.click()

    def click_previous_button(self):
        """
         finding the button which is arrow on image viewer on yandex view page
         PREVIOUS one
        :return:
            NO simply clicker
        """
        previous_button_definition = self.driver.find_element(
            By.CLASS_NAME,
            "CircleButton_type_prev")
        previous_button_definition.click()
