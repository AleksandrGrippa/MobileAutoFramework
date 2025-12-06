from elements.base_element import BaseElement

class InputElement(BaseElement):
    
    def input_value(self, value: str):
        self.find().send_keys(value)
        
    def is_focused(self):
        return self.find().get_property('focused')