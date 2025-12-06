from datetime import date
import datetime
import random

class DataGenerator():
    
    months = {
        1: 'Jan',
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
        
    }    
    
    @staticmethod
    def get_date_as_str(date: datetime.date):
        return "{month} {day}, {year}".format(month = DataGenerator.months[date.month], day = date.day, year = date.year)
    
    @staticmethod
    def get_random_date() -> datetime.date:
        start_date = date(1900, 1, 1)
        end_date = date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        return start_date + datetime.timedelta(days=random_number_of_days)
        # return start_date + datetime.timedelta(days=random_number_of_days)