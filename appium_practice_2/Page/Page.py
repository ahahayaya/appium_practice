from Base.BASE import BASE
from Base import GET_DRIVER
import Page

class Page_login(BASE):
    def __init__(self,driver):
        BASE.__init__(self,driver)
    #点击我的
    def click_my_btn(self):
        self.click_element(Page.my_btn_xpath)
    # 点击登录/注册页
    def click_login_btn(self):
        self.click_element(Page.login_reg_id)
    #用户登录操作
    def user_login(self,username,pwd):
        self.input_element(Page.username_id,username)
        self.input_element(Page.userpwd_id,pwd)
        self.click_element(Page.login_btn_id)
    def user_logout(self):
        self.click_element(Page.security_logout)
    def close_login(self):
        self.click_element(Page.close_login_page)
