from selenium.webdriver.common.by import By
agreen = (By.ID,'com.tencent.mobileqq:id/dialogRightBtn')
click_login = (By.XPATH,"//*[contains(@text,'登录')]")
uid = (By.XPATH,"//*[contains(@content-desc,'请输入QQ号码或手机或邮箱')]")
pwd = (By.ID,"com.tencent.mobileqq:id/password")
login = (By.ID,"com.tencent.mobileqq:id/login")
message_text = (By.ID,"com.tencent.mobileqq:id/ivTitleName")