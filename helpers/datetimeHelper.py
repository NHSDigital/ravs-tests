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

    @staticmethod
    def format_date(date, browser):
        try:
            parsed_date = datetime.strptime(date, '%d/%m/%Y')
            if browser == "safari" or browser == "mobile":
                return parsed_date.strftime('%m/%d/%Y')
            else:
                return parsed_date.strftime('%d/%m/%Y')
        except ValueError:
            try:
                parsed_date = datetime.strptime(date, '%Y-%m-%d')
                if browser == "safari" or browser == "mobile":
                    return parsed_date.strftime('%m/%d/%Y')
                else:
                    return parsed_date.strftime('%d/%m/%Y')
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date, '%Y.%m.%d')
                    if browser == "safari" or browser == "mobile":
                        return parsed_date.strftime('%m/%d/%Y')
                    else:
                        return parsed_date.strftime('%d/%m/%Y')
                except ValueError:
                    raise ValueError("Invalid date format. Date should be in the format dd/mm/yyyy, yyyy-mm-dd, or yyyy.%m.%d.")

    @staticmethod
    def get_date_value(date):
        if "today" in date.lower():
            parts = date.split("-")

            if len(parts) > 1:
                offset = int(parts[1].strip())
            else:
                offset = 0

            return (datetime.today() - timedelta(days=offset)).date()
        else:
            return datetime.strptime(date, "%Y-%m-%d").date()

    @staticmethod
    def standardize_date_format(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, '%d/%m/%Y')
            return parsed_date.strftime('%d/%m/%Y')
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, '%m/%d/%Y')
                # Format the parsed date to '%d/%m/%Y'
                return parsed_date.strftime('%d/%m/%Y')
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str

class DatetimeHelper(BaseDatetimeHelper):
    def __init__(self):
        super().__init__()
