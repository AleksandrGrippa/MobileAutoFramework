from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement():
    def __init__(self, driver, locator, timeout = 10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
    
    def find(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((self.locator)))
    
    def click(self):
        self.find().click()

    def text(self):
        return self.find().text
    
    def is_displayed(self):
        return self.find().is_displayed()
    
    def is_enabled(self):
        return self.find().is_enabled()