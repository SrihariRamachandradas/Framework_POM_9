from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *

class LoginPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        # self.driver = driver
        self.un = "j_username"
        self.pwd = "j_password"
        self.login = "Submit"
        global wb
        wb = WebGeneric(driver)

    def enter_un(self):
        # self.driver.find_element_by_name(self.un).send_keys(UN)
        # wb.enter(self.un, UN)
        un = select_cell_val("Login.xlsx", "setup", "Un")
        wb.enter('id', self.un, un)

    def enter_pwd(self):
        # self.driver.find_element_by_name(self.pwd).send_keys(PWD)
        # wb.enter(self.pwd, PWD)
        pwd = select_cell_val("Login.xlsx", "setup", "Pwd")
        wb.enter('name', self.pwd, pwd)

    def click_login(self):
        # self.driver.find_element_by_xpath("//*[text()='Login ']").click()
        # wb.click(self.login)
        wb.click('name', self.login)
        wb.report_pass_fail("A", "A")
