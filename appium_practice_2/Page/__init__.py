from selenium.webdriver.common.by import By

"""
首页
"""
#我的按钮
my_btn_xpath = (By.XPATH,"//*[contains(@resource-id,'com.tpshop.malls:id/tab_txtv') and contains(@text,'我的')]")

"""
用户信息输入页     
"""
# 登录注册
login_reg_id = (By.ID,"com.tpshop.malls:id/nickname_txtv")
#输入用户名
username_id = (By.ID,"com.tpshop.malls:id/edit_phone_num")
#输入密码
userpwd_id = (By.ID,"com.tpshop.malls:id/edit_password")
#登录按钮
login_btn_id = (By.ID,"com.tpshop.malls:id/btn_login")
#关闭用户信息输入页
close_login_page = (By.ID,'com.tpshop.malls:id/titlebar_back_imgv')

"""
个人中心页
"""
#设置
personal_set= (By.ID,'com.tpshop.malls:id/setting_btn')

"""
设置页
"""
# 安全退出
security_logout = (By.XPATH,'//*[contains(@text,"安全退出")]')