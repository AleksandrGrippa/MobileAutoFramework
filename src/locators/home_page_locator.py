from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class HomePageLocator(BaseLocator):
    def __init__(self):
        pass

    INSERT_EVENT_BUTTON_ID = (By.ID, 'com.minar.birday:id/fab')
    
    def get_EVENT_BY_XPATH_by_index(self, index):
        if index > 1:
            return (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.minar.birday:id/eventRecycler"]/android.view.ViewGroup{}'.format(index))
        else:
            return (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.minar.birday:id/eventRecycler"]/android.view.ViewGroup')
    
    