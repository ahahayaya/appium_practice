import pytest,os,sys
sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.Set_Page import Set_page
class Test_more:
    def setup_class(self):
        self.sp_obj= Set_page(get_driver())
        self.sp_obj.click_more()
        self.sp_obj.click_move_net()

    def teardow_class(self):
        self.sp_obj.driver.quit()
    def test_1(self):
        self.sp_obj.click_first_net()
        self.sp_obj.click_Two()
    @pytest.mark.run(order=1)
    def test_2(self):
        self.sp_obj.click_first_net()
        self.sp_obj.click_three()