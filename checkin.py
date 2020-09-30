from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from dataLoad import dataLoading
from find_element import Element

actions = Element()
actions.id("dl").click()
sleep(3)
actions.class_name("inp.txt-name").clear()
# 类中方法调用
a = dataLoading.login_data("pc数据.xlsx")

actions.class_name( "inp.txt-name").send_keys(a['账号'])
actions.class_name("inp.txt-pwd").clear()
actions.class_name("inp.txt-pwd").send_keys(a['密码'])
actions.id("log-bnt").click()
sleep(3)
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

actions.qu()
