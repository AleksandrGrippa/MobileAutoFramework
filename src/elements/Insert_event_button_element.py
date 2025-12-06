# from elements.base_element import BaseElement
# from locators.home_page_locator import HomePageLocator
# from elements.event_element import EventElement

# class InsertEventButtonElement(BaseElement):
#     def __init__(self, driver, locator: Locator , timeout=10):
#         super().__init__(driver, locator, timeout)
    
#     def click(self, **kwargs):
#         if self.is_enabled():
#             HomePageLocator.EVENTS['{}'.format(len(EventElement.EVENTS)+1)] = kwargs
#             self.find().click()
#         else:
#             self.find().click()
