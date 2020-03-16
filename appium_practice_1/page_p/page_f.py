from comm_p.comm_f import comm_c
import page_p
class page_opt(comm_c):
    def __init__(self,driver):
        comm_c.__init__(self,driver)
    def click_login(self):
        self.click_element(page_p.click_login)
    def login_opt(self,username,pwd):
        self.input_element(page_p.uid,username)
        self.input_element(page_p.pwd,pwd)
        self.click_element(page_p.login)
