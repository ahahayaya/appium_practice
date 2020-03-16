import sys,os,Page,allure,pytest
sys.path.append(os.getcwd())
from Base.Base import Base
class Page_message(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_new(self):
        self.click_element(Page.new_message)
    def input_acceptor(self,acceptor):
        self.input_element(Page.acceptor,acceptor)
    def input_messagetext(self,text):
        self.input_element(Page.input_text,text)
    def click_send(self):
        self.click_element(Page.send_btn)
    def click_back(self):
        self.click_element(Page.back)


