from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator

class HomePageLocator(BaseLocator):
    def __init__(self):
        pass

    INSERT_EVENT_BUTTON_ID = (By.ID, 'com.minar.birday:id/fab')
    
    NO_EVENTS_TEXT_VIEW_BY_ID = (By.ID, 'com.minar.birday:id/noEvents')


    @staticmethod
    def get_EVENT_BY_XPATH_by_index(index):
        """
        Returns locator for an event item in the events RecyclerView by 1-based index.
        When index == 1 we can omit the position predicate, for index > 1 we append
        the index in square brackets.
        """
        base_xpath = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.minar.birday:id/eventRecycler"]/android.view.ViewGroup'
        if index > 1:
            return (By.XPATH, f'{base_xpath}[{index}]')
        else:
            return (By.XPATH, base_xpath)
    
    