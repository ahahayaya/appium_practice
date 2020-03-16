import allure
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from comm_p.init_driver import get_driver
import time
class comm_c:
    def __init__(self,driver):
        #初始化driver
        self.driver = get_driver()
    def search_element(self,loc):
        #元素定位
        return WebDriverWait(self.driver,60,1).until(lambda x:x.find_element(*loc))
    def input_element(self,loc,text):
        #输入
        e = self.search_element(loc)
        e.clear()
        return e.send_keys(text)
    def click_element(self,loc):
        #点击
        return self.search_element(loc).click()
    def toast_message(self,content):
        #toast消息
        xpath = (By.XPATH,"//*[contains(@text,'{}')]".format(content))
        got_message = self.search_element(xpath)
        return got_message.text
    def get_screenshot(self):
        #截图
        image_name = "./screen/%d.png"%int(time.time())
        with open(image_name,"rb") as f:
            allure.attach("截图名字",f.read(),allure.attach_type.png)