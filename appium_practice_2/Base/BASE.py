from selenium.webdriver.support.wait import WebDriverWait


class BASE:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    def search_element(self,tru):
        return self.wait.until(lambda x:x.find_element(*tru))
    def search_elements(self,tru):
        return self.wait.until(lambda x:x.find_elements(*tru))
    def click_element(self,tru):
        self.search_element(tru).click()
    def input_element(self,tru,text):
        input_e = self.search_element(tru)
        input_e.clear()
        input_e.send_keys(text)
