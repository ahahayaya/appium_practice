import time
import allure
from comm.init_driver import get_driver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class comm:
    def __init__(self,driver):
        self.driver = get_driver()
    def search_element(self,loc):
        return WebDriverWait(self.driver,timeout=50,poll_frequency=1).until(lambda x:x.find_element(*loc))
    def click_element(self,loc):
        self.search_element(loc).click()
    def input_element(self,loc,text):
        e = self.search_element(loc)
        e.click()
        e.clear()
        return e.send_keys(text)
    def get_toast(self,message):
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            message_text = self.search_element((By.XPATH,xpath),10,1)
            return message_text
        except Exception as e:
            return False
    def get_screen(self):
        image_name = "./screens/%d.png" % int(time.time())
        self.driver.get_screenshot_as_file(image_name)
        with open(image_name,"rb") as f:
            allure.attach("截图名字",f.read(),allure.attachment_type.png)




