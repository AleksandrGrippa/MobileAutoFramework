from elements.base_element import BaseElement
from elements.event_selector_element import EventSelectorElement
from elements.input_element import InputElement 
from elements.switcher_element import SwitcherElement
from pages.base_page import BasePage
from locators.insert_event_page_locator import InsertEventPageLocator
import datetime
from utils.data_generator import DataGenerator


class InsertEventPage(BasePage):
    
    @property
    def event_type_selector(self):
        return EventSelectorElement(self.driver, InsertEventPageLocator.EVENT_TYPE_SELECTOR_BY_ID)
    
    @property
    def first_name_input(self):
        return InputElement(self.driver, InsertEventPageLocator.FIRST_NAME_INPUT_BY_ID)
    
    @property
    def last_name_input(self):
        return InputElement(self.driver, InsertEventPageLocator.LAST_NAME_INPUT_BY_ID)

    @property
    def date_input(self):
        return InputElement(self.driver, InsertEventPageLocator.DATE_INPUT_BY_ID)
    
    @property
    def consider_the_year_switcher(self):
        return SwitcherElement(self.driver, InsertEventPageLocator.CONSIDER_THE_YEAR_SWITCHER_BY_ID)
    
    @property
    def create_event_button(self):
        return BaseElement(self.driver, InsertEventPageLocator.CREATE_EVENT_BUTTON_BY_ID)
    
    @property
    def cancel_import_contact_button(self):
        return BaseElement(self.driver, InsertEventPageLocator.CANCEL_IMPORT_CONTACT_BUTTON_BY_ID)
    
    def fill_event_form(self, event_type, name, surname, date: datetime.date, enable_switcher = True):
        self.event_type_selector.click()
        self.event_type_selector.select(event_type)
        self.event_type_selector.click()
        self.first_name_input.click()
        self.first_name_input.input_value(name)
        self.last_name_input.input_value(surname)
        date_as_str = DataGenerator.get_date_as_str(date)
        self.date_input.input_value(date_as_str)
        if enable_switcher:
            pass
        else: 
                self.consider_the_year_switcher.click()
        