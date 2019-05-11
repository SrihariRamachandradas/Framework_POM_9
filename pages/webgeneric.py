from pages.locgeneric import LocGeneric
import allure

class WebGeneric(LocGeneric):
    def __init__(self, driver):
        LocGeneric.__init__(self, driver)
        global lc
        lc = LocGeneric(driver)

    def enter(self, locator_type, locator_val, input_val):
        e = self.locator(locator_type, locator_val)
        e.send_keys(input_val)

    def click(self, locator_type, locator_val):
        e = self.locator(locator_type, locator_val)
        e.click()

    def report_pass(self):
        pass

    def report_fail(self):
        pass
