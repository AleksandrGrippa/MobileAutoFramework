from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class FlowPageLocator(BaseLocator):
    
    NEXT_BUTTON_BY_ID = (By.ID, "com.minar.birday:id/next")
    
    DONE_BUTTON_BY_ID = (By.ID, "com.minar.birday:id/done")
    
    TITLE_FLOW_BY_ID = (By.ID, "com.minar.birday:id/title")
    
    