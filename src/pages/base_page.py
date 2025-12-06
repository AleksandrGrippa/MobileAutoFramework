from appium import webdriver

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        
    def capture_screenshot(self):
        return self.driver.get_screenshot_as_png()