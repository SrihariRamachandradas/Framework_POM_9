import pytest
from pages.jqueryloginpage import Jquery_LoginPage

@pytest.mark.usefixtures("test_setup")
class TestDragAndDrop:
    def test_drag(self):
        driver = self.driver
        dd = Jquery_LoginPage(driver)
        dd.drag_and_drop()