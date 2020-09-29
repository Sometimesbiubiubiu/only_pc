from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from dataLoad import dataLoading

driver = webdriver.Chrome()
file_path = "/Users/mac/Documents/图片截图/IMG_wodeshouyi.jpg"
url = "http://10.11.0.91:8080/gaga_sns_web/"
driver.get(url)
driver.find_element(By.ID, "dl").click()
sleep(3)
driver.find_element(By.CLASS_NAME, "inp.txt-name").clear()
# 类中方法调用
a = dataLoading.login_data("pc数据.xlsx")

driver.find_element(By.CLASS_NAME, "inp.txt-name").send_keys(a['账号'])
driver.find_element_by_class_name("inp.txt-pwd").clear()
driver.find_element_by_class_name("inp.txt-pwd").send_keys(a['密码'])
driver.find_element_by_id("log-bnt").click()
sleep(3)
driver.find_element_by_id("leftSixinIndexText").click()
sleep(3)
driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/div[3]/ul/li[1]').click()
# 全路径是铁定行
# driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div[1]/div[2]/div[1]/ul/li[2]/div[2]/input').send_keys(file_path)
driver.find_element_by_class_name("webuploader-element-invisible").send_keys(file_path)
sleep(3)
driver.find_element_by_class_name('sendBtn').click()
sleep(5)

driver.quit()
# 看下这个还有变化么
