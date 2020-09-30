from time import sleep
from gagahi.find_element import Element
from gagahi.dataLoad import dataLoading

# 类实例化
actions = Element()
actions.id("dl").click()
sleep(3)
actions.class_name("inp.txt-name").clear()
# 类中方法调用
a = dataLoading.login_data("./gagahi/pc数据.xlsx")

actions.class_name("inp.txt-name").send_keys(a[0]['账号'])
actions.class_name("inp.txt-pwd").clear()
actions.class_name("inp.txt-pwd").send_keys(a[0]['密码'])
actions.id("log-bnt").click()
sleep(5)
actions.id("leftSixinIndexText").click()
sleep(3)
actions.xpth('//*[@id="mCSB_2_container"]/div[3]/ul/li[1]').click()

# 当前窗口发送图片
# 全路径是铁定行
# driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div[1]/div[2]/div[1]/ul/li[2]/div[2]/input').send_keys(file_path)
file_path = "/Users/mac/Documents/图片截图/IMG_wodeshouyi.jpg"
actions.class_name("webuploader-element-invisible").send_keys(file_path)
sleep(3)
actions.class_name('sendBtn').click()
sleep(5)
b = dataLoading.message_data("./gagahi/pc数据.xlsx")
for i in b:
    actions.id('inputBox').send_keys(i)
    actions.class_name('sendBtn').click()
    sleep(2)
sleep(5)
actions.qu()
