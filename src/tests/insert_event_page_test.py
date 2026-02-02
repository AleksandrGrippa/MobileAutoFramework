from base_test import BaseTest
from pages.home_page import HomePage
from pages.insert_event_page import InsertEventPage
from utils.data_generator import DataGenerator
from pages.flow_page import FlowPage
from pages.dialog_permission import DialogPermission
import allure
import pytest
from utils.test_cases_data.event_creation_test_cases import*
from utils.test_cases_data.event_test_data import*

@pytest.mark.smoke
@pytest.mark.regression
class TestInsertEventPage(BaseTest):
    @pytest.mark.positive
    @pytest.mark.parametrize("event_type, name, surname, date", [EventCreationTestCases.get_event_test_case_with_correct_data(), EventCreationTestCases.get_event_test_case_with_empty_surname()])
    def test_homePageIsOpen_addEventWithCorrectData_eventAdded(self, event_type, name, surname, date):
        flow_page = FlowPage(self.driver)
        # dialog_permission = DialogPermission(self.driver)
        insert_event_page = InsertEventPage(self.driver)
        home_page = HomePage(self.driver)

        flow_page.next_flow_button.click()
        flow_page.next_flow_button.click()
        flow_page.done_flow_button.click()
        
        # dialog_permission.dont_allow_permission_button.click()
        # dialog_permission.dont_allow_permission_button.click()
        home_page.insert_event_button.click()
        # dialog_permission.allow_permission_button.click()
        # insert_event_page.cancel_import_contact_button.click()
        insert_event_page.fill_event_form(event_type, name, surname, date)
        insert_event_page.create_event_button.click()
        
        png_bytes = flow_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_test_end_state'.format(self.test_homePageIsOpen_addEventWithCorrectData_eventAdded.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        
        event_displayed = home_page.event_element(1).is_displayed()

        assert event_displayed == True
    
    @pytest.mark.negative
    @pytest.mark.parametrize("event_type, name, surname, date", [EventCreationTestCases.get_event_test_case_with_empty_name(), EventCreationTestCases.get_event_test_case_with_empty_date()] )
    def test_homePageIsOpen_addEventWithoutName_createEventButtonIsNotEnabled(self, event_type, name, surname, date):
        home_page = HomePage(self.driver)
        insert_event_page = InsertEventPage(self.driver)
        flow_page = FlowPage(self.driver)
        # dialog_permission = DialogPermission(self.driver)

        flow_page.next_flow_button.click()
        flow_page.next_flow_button.click()
        flow_page.done_flow_button.click()
        # dialog_permission.dont_allow_permission_button.click()
        # dialog_permission.dont_allow_permission_button.click()
        home_page.insert_event_button.click()
        # dialog_permission.allow_permission_button.click()
        # insert_event_page.cancel_import_contact_button.click()

        insert_event_page.fill_event_form(event_type, name, surname, date)
        
        button_displayed = insert_event_page.create_event_button.is_enabled()
        
        png_bytes = insert_event_page.capture_screenshot()
        allure.attach(
            png_bytes,
            name='screen_{}_test_end_state'.format(
                self.test_homePageIsOpen_addEventWithoutName_createEventButtonIsNotEnabled.__name__
            ),
            attachment_type=allure.attachment_type.PNG,
            extension=".png"
        )
        assert button_displayed == False