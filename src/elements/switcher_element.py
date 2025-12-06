from elements.base_element import BaseElement

class SwitcherElement(BaseElement):
        
    def is_on(self):
        return self.find().get_attribute("checked")