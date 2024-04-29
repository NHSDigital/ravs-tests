from datetime import datetime, timedelta

class BaseDatetimeHelper:
    @staticmethod
    def current_datetime():
        return datetime.now()

    @staticmethod
    def format_datetime(dt, format="%Y-%m-%d %H:%M:%S"):
        return dt.strftime(format)

    @staticmethod
    def parse_datetime(date_string, format="%Y-%m-%d %H:%M:%S"):
        return datetime.strptime(date_string, format)

    @staticmethod
    def add_days(dt, days):
        return dt + timedelta(days=days)

    @staticmethod
    def subtract_days(dt, days):
        return dt - timedelta(days=days)

class DatetimeHelper(BaseDatetimeHelper):
    pass