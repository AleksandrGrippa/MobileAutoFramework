from utils.test_cases_data.data import*
from utils.test_cases_data.event_test_data import *
from utils.data_generator import DataGenerator

class EventCreationTestCases():
    @staticmethod
    def get_event_test_case_with_correct_data():
        event = EventDTO(event_type='Birthday', name='Sasha', surname='Grippa', date=DataGenerator.get_random_date())
        return (event.event_type, event.name, event.surname, event.date)
    
    @staticmethod
    def get_event_test_case_with_empty_surname():
       event = EventDTO(event_type='Birthday', name='Sasha', surname='', date=DataGenerator.get_random_date())
       return (event.event_type, event.name, event.surname, event.date)

    @staticmethod
    def get_event_test_case_with_empty_name():
       event = EventDTO(event_type='Birthday', name='', surname='Grippa', date=DataGenerator.get_random_date())
       return (event.event_type, event.name, event.surname, event.date)
    
    @staticmethod
    def get_event_test_case_with_empty_date():
       event = EventDTO(event_type='Birthday', name='Sasha', surname='Grippa', date="")
       return (event.event_type, event.name, event.surname, event.date)