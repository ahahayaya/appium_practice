from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        """
        :param driver:初始化driver属性
        """
        self.driver = driver
    def search_element(self,loc,timeout=15,poll=0.5):
        """

        :param loc:(By.id,'idvalue')
        :param timeout: 传给WebDriverWait，超时时间
        :param poll: 传给WebDriverWait,搜索频率
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))
    def search_elements(self,loc,timeout=15,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))
    def click_element(self,loc):
        self.search_element(loc).click()
    def input_element(self,loc,text):
        e = self.search_element(loc)
        e.clear()
        e.send_keys(text)
    def click_elements(self,loc):
        self.search_element(loc)