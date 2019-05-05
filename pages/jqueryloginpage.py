from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *


class Jquery_LoginPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.draggable = "//div[@id='draggable']"
        self.droppable = "//div[@id='droppable']"
        self.iframe = "iframe"
        self.src = "//div[@id='draggable']"
        self.dest = "//div[@id='droppable']"
        global wb
        wb = WebGeneric(driver)

    def drag_and_drop(self):
        self.switch_to_frame_custom("tagname",self.iframe)
        self.move_src_dest("xpath",self.src,"xpath",self.dest)