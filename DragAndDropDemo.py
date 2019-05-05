from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:/Users/SRIHARI/PycharmProjects/Framework_POM_9/drivers/chromedriver.exe")
driver.get("https://jqueryui.com/droppable")
driver.implicitly_wait(20)
driver.maximize_window()

frame = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(frame)

a = ActionChains(driver)
src_element = driver.find_element_by_xpath("//div[@id='draggable']")
des_element = driver.find_element_by_xpath("//div[@id='droppable']")
a.drag_and_drop(src_element, des_element).perform()