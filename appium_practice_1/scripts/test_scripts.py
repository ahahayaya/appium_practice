import pytest
import sys,os,allure
sys.path.append(os.getcwd())
from comm_p.init_driver import get_driver
from comm_p.init_data import get_data
from page_p.page_f import page_opt
class test_c:
    def setup_class(self):
        self.p_obj = page_opt(get_driver())
        self.p_obj.click_login()
    def teardown_class(self):
        self.p_obj.driver.quit()
    @pytest.mark.parametrize("caseid,username,pwd",get_data())
    def test_f(self,caseid,username,pwd):
        self.p_obj.login_opt(username,pwd)
