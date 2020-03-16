import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Page.Page_message import Page_message
from Base.Get_driver import Get_driver
from Base.read_data import read_yaml


class Test_newmessage:
    def setup_class(self):
        self.pmobj = Page_message(Get_driver())
    def teardown_class(self):
        self.pmobj.driver.quit()

    @pytest.mark.parametrize("acceptor,text",read_yaml('test_message.yaml'))
    @allure.step(title='新增短信')
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_1(self,acceptor,text):
        allure.attach('描述','点击新增按钮')
        self.pmobj.click_new()
        allure.attach('描述','输入联系人')
        self.pmobj.input_acceptor(acceptor)
        allure.attach('描述','输入短信内容')
        self.pmobj.input_messagetext(text)
        allure.attach('描述', '点击发送')
        self.pmobj.click_send()
        allure.attach('描述','点击返回按钮')
        self.pmobj.click_back()

