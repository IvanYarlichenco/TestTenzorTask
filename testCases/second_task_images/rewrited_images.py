import time
import unittest

from selenium import webdriver

from self_page_object_im import *

PATH = r"C:\Program Files (x86)\chromedriver.exe"


class TestImageViewer(unittest.TestCase):
    """
    main cals to Test a task
    """

    def setUp(self):
        """
        setting up driver properties
        :return:
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = PATH
        self.driver = webdriver.Chrome(options=chrome_options)
        self.home_page = HomePage(self.driver)
        self.images_page = ImagePage(self.driver)
        self.image_viewer_page = ImageViewerPage(self.driver)



    def test_image_viewer_navigation(self):
        """
        main execution of a task I have received
        :return:
        """
        try:

            self.home_page.open_yandex()  # Tested - done
            time.sleep(10)  # time sleeps for captcha and speed of evoking control
            self.home_page.on_input_field_click()
            self.home_page.all_menu_click()
            time.sleep(5)
            self.home_page.click_menu_images()
            # switched window here
            self.home_page.switched_window_detector()
            if self.home_page.is_image_menu_appeared():
                if self.images_page.is_suggested_image_category_appeared():  # Tested - done
                    # grabbing the name of category, so we can compare to an input field text
                    first_category_name = self.images_page.get_first_suggested_image_category_name()
                    self.images_page.click_first_suggested_image_category()
                    if self.images_page.comparing_names_of_input_and_category_name(
                            first_category_name
                    ):  # Tested - done
                        print("Category of the name we have chosen has matched ")
                    # print(2)
                    time.sleep(5)
                    if self.image_viewer_page.is_image_viewer_displayed():  # Tested - done
                        print("Image has opened")
                        self.image_viewer_page.click_on_image_viewer_displayed()

                        # here we are starting to collect src, so we can detect changing of images
                        first_image_source = self.image_viewer_page.get_image_source()  # Tested - done
                        print("First Image Source:", first_image_source)
                        time.sleep(5)
                        # print(3)
                        # changing photo
                        self.image_viewer_page.click_next_button()  # Tested - done

                        WebDriverWait(self.image_viewer_page.driver, 10).until(
                            # lambda so images aren't the same since we have swept them
                            lambda driver: self.image_viewer_page.get_image_source() != first_image_source
                        )
                        # second image src collector
                        swapped_image_src_rememberer = self.image_viewer_page.get_image_source()
                        # Tested - done
                        print("Second First Image Source:", swapped_image_src_rememberer)
                        time.sleep(5)
                        if swapped_image_src_rememberer != first_image_source:
                            print("The image has swept")
                            # done checking changing of image, and coming back to the first
                            self.image_viewer_page.click_previous_button()  # Tested - done

                            WebDriverWait(self.image_viewer_page.driver, 30).until(
                                # waits, so we have changed to the previous image
                                lambda dr: self.image_viewer_page.get_image_source() == first_image_source
                            )
                            # indicating the current state of image
                            current_image_source = self.image_viewer_page.get_image_source()  # Tested - done
                            print("Current Image Source: ", current_image_source)
                            if current_image_source == first_image_source:

                                print("We're back to the first image we saw")
                                time.sleep(5)
                            else:
                                print("This is not the image we've been expecting")

                        else:
                            print("Image hasn't been swept")
            else:
                print("We are not on the image menu page")

        except Exception as e:
            print("Error occurred:", str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
