from elements.base_element import BaseElement

class InputElement(BaseElement):
    
    def input_value(self, value: str):
        el = self.find()
        el.send_keys(value)
        
    def is_focused(self):
        el = self.find()
        return el.get_property('focused')