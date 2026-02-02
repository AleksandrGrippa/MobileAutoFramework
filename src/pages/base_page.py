from appium import webdriver

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def hide_keyboard_if_shown(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass
        
    def capture_screenshot(self):
        return self.driver.get_screenshot_as_png()