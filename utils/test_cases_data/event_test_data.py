from utils.data_generator import DataGenerator
import datetime
from typing import NamedTuple

class EventDTO(NamedTuple):
        event_type: str
        name: str
        surname: str
        date: datetime

    # def get_event_creation_test_case(self):
    #     return (self.event_type, self.name, self.surname, self.date)