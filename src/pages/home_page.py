from elements.base_element import BaseElement
from pages.base_page import BasePage
from locators.home_page_locator import HomePageLocator
class HomePage(BasePage):

    @property
    def insert_event_button(self):
        return BaseElement(self.driver, HomePageLocator.INSERT_EVENT_BUTTON_ID) 
    
    def event_element(self, index):
        return BaseElement(self.driver, HomePageLocator.get_EVENT_BY_XPATH_by_index(index))

