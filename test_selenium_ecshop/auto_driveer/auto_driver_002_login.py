from selenium import webdriver
from time import sleep
fp=webdriver.FirefoxProfile(r"C:\Users\THINK\AppData\Roaming\Mozilla\Firefox\Profiles\nc2c6nsu.default")
driver=webdriver.Firefox(fp)
# driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(3)
# 添加Cookie     登录百度的方法 ，绕过验证米，利用cookie直接登录  需要先登录百度，点击退出的话会使cookie变化
driver.add_cookie({'name':'BDUSS', 'value':'TVXdXliUG9oV2swS2MwOWJKcGVtZmI1RjB1YVU3UG1iaX5GQ3BPfjA4WVpGYVpiQUFBQUFBJCQAAAAAAAAAAAEAAADnBAo2eHZubWVuZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmIflsZiH5bT'})
# 刷新页面
driver.refresh()
sleep(5)
driver.quit()