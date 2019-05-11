from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *


class SelectDemoPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        # self.driver = driver
        self.day = "day"
        self.month = "month"
        self.year = "year"
        global wb
        wb = WebGeneric(driver)

    def select_day(self):
        wb.select_drp_dwn_val_by_visible_text('id', self.day, "10")

    def select_month(self):
        wb.select_drp_dwn_val_by_visible_text('id', self.month, "Feb")

    def select_year(self):
        wb.select_drp_dwn_val_by_visible_text('id', self.year, "1998")