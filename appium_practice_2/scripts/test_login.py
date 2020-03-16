import pytest,sys,os
sys.path.append(os.getcwd())
from Base.GET_DRIVER import GET_DRIVER
from Page.Page import Page_login

class Test_login:
    def setup_class(self):
        self.p_obj = Page_login(GET_DRIVER("com.tpshop.malls",".SPMainActivity"))
        self.p_obj.click_my_btn()
        self.p_obj.click_login_btn()
    def teardown_class(self):
        self.p_obj.driver.quit()
    @pytest.mark.parametrize('username,pwd',[('15881036627','123456')])
    def test_1(self,username,pwd):
        self.p_obj.user_login(username,pwd)

