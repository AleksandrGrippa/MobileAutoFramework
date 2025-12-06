from appium.webdriver.common.appiumby import AppiumBy
from elements.base_element import BaseElement
from pages.base_page import BasePage
from locators.permission_dialog_locator import DialogPermissionLocator

class DialogPermission(BasePage):
    
    @property
    def dialog_permission_message (self):
        return BaseElement(self.driver, DialogPermissionLocator.DIALOG_PERMISSION_MESSAGE_BY_ID)
    
    @property
    def allow_permission_button (self):
        return BaseElement(self.driver, DialogPermissionLocator.DIALOG_PERMISSION_ALLOW_BUTTON_BY_ID)
    
    @property
    def dont_allow_permission_button (self):
        return BaseElement(self.driver, DialogPermissionLocator.DIALOG_PERMISSION_DONT_ALLOW_BUTTON_BY_ID)