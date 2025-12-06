from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class InsertEventPageLocator(BaseLocator):
    
    EVENT_TYPE_SELECTOR_BY_ID = (By.ID, "com.minar.birday:id/typeEvent")
    
    FIRST_NAME_INPUT_BY_ID = (By.ID, "com.minar.birday:id/nameEvent")
    
    LAST_NAME_INPUT_BY_ID = (By.ID, "com.minar.birday:id/surnameEvent")
    
    DATE_INPUT_BY_ID = (By.ID, "com.minar.birday:id/dateEvent")
    
    CONSIDER_THE_YEAR_SWITCHER_BY_ID = (By.ID, "com.minar.birday:id/countYearSwitch")
    
    CREATE_EVENT_BUTTON_BY_ID = (By.ID, "com.minar.birday:id/positiveButton")
    
    CANCEL_IMPORT_CONTACT_BUTTON_BY_ID = (By.ID, "com.minar.birday:id/importContactsCancelButton")