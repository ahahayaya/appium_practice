from time import sleep

from comm.comm import comm
import page,allure
class Login_opt(comm):
    def __init__(self,driver):
        comm.__init__(self,driver)
    @allure.step(title="点击登录")
    def click_login_func(self):
        self.click_element(page.agreen)
        self.click_element(page.click_login)
    @allure.step(title='输入用户名密码')
    def login_func(self,uname,passwd):
        self.input_element(page.uid,uname)
        self.input_element(page.pwd,passwd)
        sleep(5)
        self.click_element(page.login)
        sleep(5)
    @allure.step(title="登录结果")
    def got_message(self):
        assert self.search_element(page.message_text)


