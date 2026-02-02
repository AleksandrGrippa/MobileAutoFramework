from elements.base_element import BaseElement

class SwitcherElement(BaseElement):
        
    def is_on(self):
        el = self.find()
        return el.get_attribute("checked")