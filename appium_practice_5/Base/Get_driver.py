from appium import webdriver
def Get_driver():
    desired_caps={}
    desired_caps['deviceName']='xxx'
    desired_caps['platformName']='Android'
    desired_caps['appPackage']='com.android.mms'
    desired_caps['appActivity']='.ui.ConversationList'
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)