from appium import webdriver
def get_driver():
    desired_caps={}
    desired_caps['platformName']='Android'
    desired_caps['deviceName']='xx'
    desired_caps['appPackage']='com.android.settings'
    desired_caps['appActivity']='.Settings'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)