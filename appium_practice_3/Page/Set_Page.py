from Base.Base import Base
import Page
class Set_page(Base):
    def __init(self,driver):
        Base.__init__(self,driver)
    def click_more(self):
        self.click_element(Page.more_text)
    def click_move_net(self):
        self.click_element(Page.move_net)
    def click_first_net(self):
        self.click_element(Page.first_choice)
    def click_Two(self):
        self.click_element(Page.two_G)
    def click_three(self):
        self.click_element(Page.three_G)
    
