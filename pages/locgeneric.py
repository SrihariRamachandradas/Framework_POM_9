import moment
import allure
import os
from testdata import data as data

class LocGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_val)
            return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()

    def get_screenshot(self):
        cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        test_name = data.whoami()
        screenshot_name = test_name + "_" + cur_time

        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(
            os.getcwd().replace("\\", "/") + "/screenshots/" + screenshot_name + ".png")
        print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")

    def report_pass_fail(self, actual_val, expected_val):
        self.get_screenshot()
        assert actual_val == expected_val

    def report_fail(self):
        self.get_screenshot()



