from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver
    def search_element(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def search_elements(self,loc,timout=10,poll=0.5):
        return WebDriverWait(self.driver,timout,poll).until(lambda x:x.find_element(*loc))
    def click_element(self,loc):
        self.search_element(loc).click()
    def input_element(self,loc,text):
        e = self.search_element(loc)
        e.clear()
        e.send_keys(text)
