# import pytest
# @pytest.fixture()
# @pytest.usefixtures('funcname')
# @pytest.mark.skip(condition=1,reason='xxx')
# @pytest.mark.xfail(condition=2,reason='xx')
# @pytest.mark.parametrize("a,b"'[1,2]')
# @pytest.mark.run(ordering=1)
# def aa():
#     print('aaa')
# # adb shell dumpsys window windows | findstr mFocusedApp
#
# from appium import webdriver
# desired_caps={}
# desired_caps['deviceName']="xx"
# desired_caps['platformName']="Android"
# desired_caps['appPackage']="cc"
# desired_caps['appActivity']='xx'
# desired_caps['unicodekeyboard']=True
# desired_caps['resetkeyboard']=True
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#
# def bublesort(a):
#     l = len(a)
#     for i in range(1,l):
#         for j in range(1,l):
#             if a[j-1]>a[j]:
#                 r = a[j-1]
#                 a[j-1]=a[j]
#                 a[j]=r
#     print(a)
#
# def nineXnine():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print("%d * %d = %d"%(j,i,i*j),end=' ')
#         print()
# from appium import webdriver
# import threading
# def more_devices(port):
#     desired_caps = {}
#     desired_caps['deviceName']='xx'
#     desired_caps['platformName']='Android'
#     desired_caps['appPackage']='xxx'
#     desired_caps['appActivity']='xx'
#     desired_caps['unicodeKeyboard']=True
#     desired_caps['resetKeyboard']=True
#     desired_caps['uiautomationName']='Uiautomator2' """ 获取totast消息"""
#     driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port),desired_caps)
# if __name__=='__main__':
#     port_list=['4723','4725']
#     thread_list=[]
#     for i in port_list:
#         th = threading.Thread(target=more_devices,args=(i,))
#         th.start()
#         thread_list.append(th)
#     for o in thread_list:
#         o.join()


# import pymysql
# conn = pymysql.connect(host='192.168.56.101',port=3306,user='root',password='123456',database='student',charset='utf8')
# cur = conn.cursor()
# query_sql = "select * from tablename limit 5"
# cur.execute(query_sql)
# print(cur.fetchall)
# cur.close()
# conn.close()

# import pymysql
# conn = pymysql.connect(host='xxx',port=3306,user='uname',password='pwd',database='DBname',charset='utf8')
# cur = conn.cursor()
# insert_sql = "insert into tablename vlaues(xx,xx)"
# cur.execute(insert_sql)
# conn.commit()
# cur.close()
# conn.close()



