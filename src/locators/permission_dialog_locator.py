from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class DialogPermissionLocator(BaseLocator):
    
    DIALOG_PERMISSION_BY_ID = (By.ID, "com.android.permissioncontroller:id/grant_dialog")
    
    DIALOG_PERMISSION_MESSAGE_BY_ID = (By.ID, "com.android.permissioncontroller:id/permission_message")
    
    DIALOG_PERMISSION_ALLOW_BUTTON_BY_ID = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    
    DIALOG_PERMISSION_DONT_ALLOW_BUTTON_BY_ID = (By.ID, "com.android.permissioncontroller:id/permission_deny_button")