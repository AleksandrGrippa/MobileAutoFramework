from elements.base_element import BaseElement
from pages.base_page import BasePage
from locators.flow_page_locator import FlowPageLocator

class FlowPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    @property
    def next_flow_button (self):
        return BaseElement(self.driver, FlowPageLocator.NEXT_BUTTON_BY_ID)
        
    @property
    def done_flow_button (self):
        return BaseElement(self.driver, FlowPageLocator.DONE_BUTTON_BY_ID)
        
    @property
    def title_flow (self):
        return BaseElement(self.driver, FlowPageLocator.TITLE_FLOW_BY_ID)
        
    