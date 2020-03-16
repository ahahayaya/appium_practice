from appium import webdriver
def GET_DRIVER(pac,act):
    desired_caps = {}
    # 平台 - 必填
    desired_caps['platformName'] = 'Android'
    # 系统版本 - 非必填，填写就必须正确
    desired_caps['platformVersion'] = '5.1'
    # 设备名称
    desired_caps['deviceName'] = 'sun'
    # desired_caps['app'] = 'apk绝对路径'
    # app包名
    desired_caps['appPackage'] = pac
    # app启动名
    desired_caps['appActivity'] = act
    # 设置中文输入
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    #获取toast消息
    desired_caps['automationName']='Uiautomator2'
    # 接口地址：http://127.0.0.1:4723/wd/hub  POST
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)