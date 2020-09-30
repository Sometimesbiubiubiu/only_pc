from selenium import webdriver


class Element(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        url = "http://10.11.0.91:8080/gaga_sns_web/"
        self.driver.get(url)

    def id(self, element):
        return self.driver.find_element_by_id(element)

    def class_name(self, element):
        return self.driver.find_element_by_class_name(element)

    def xpth(self, element):
        return self.driver.find_element_by_xpath(element)

    def qu(self):
        return self.driver.quit()
