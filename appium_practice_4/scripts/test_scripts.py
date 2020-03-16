import sys,os,allure

import pytest

sys.path.append(os.getcwd())
from comm.comm import comm
from page.login import Login_opt
from comm.init_data import get_data
from comm.init_driver import get_driver

def got_data():
    data_list = []
    data = get_data('data.yaml').read_yaml().get('login_data')
    for i in data:
        for o in i.keys():
            data_list.append((o,i.get(o).get("uid"),i.get(o).get("passwd")))
    return data_list
class Test_login:
    def setup_class(self):
        self.p_obj = Login_opt(got_data())
        self.p_obj.click_login_func()
    def teardown_class(self):
        self.p_obj.driver.quit()
    @pytest.mark.parametrize("case_num,uid,pwd",got_data())
    def test_logincase(self,case_num,uid,pwd):
        self.p_obj.login_func(uid,pwd)
