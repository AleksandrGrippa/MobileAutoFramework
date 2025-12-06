from elements.base_element import BaseElement

class EventSelectorElement(BaseElement):
    input_values = {
        'Birthday' : 'Birthday',
        'Anniversary' : 'Anniversary',
        'Death anniversary' : "Death anniversary",
        'Name day' : 'Name day',
        'Other' : "Other"
    }
    
    def select(self, value: str):
        self.find().send_keys(value)
    
    