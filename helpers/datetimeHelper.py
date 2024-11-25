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
            parsed_date = datetime.strptime(date, "%d/%m/%Y")
            if browser == "safari" or browser == "mobile":
                return parsed_date.strftime("%m/%d/%Y")
            else:
                return parsed_date.strftime("%d/%m/%Y")
        except ValueError:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                if browser == "safari" or browser == "mobile":
                    return parsed_date.strftime("%m/%d/%Y")
                else:
                    return parsed_date.strftime("%d/%m/%Y")
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date, "%Y.%m.%d")
                    if browser == "safari" or browser == "mobile":
                        return parsed_date.strftime("%m/%d/%Y")
                    else:
                        return parsed_date.strftime("%d/%m/%Y")
                except ValueError:
                    raise ValueError(
                        "Invalid date format. Date should be in the format dd/mm/yyyy, yyyy-mm-dd, or yyyy.%m.%d."
                    )

    @staticmethod
    def get_date_value(date):
        if "today" in date.lower():
            if "-" in date.lower():
                parts = date.split("-")
            elif "+" in date.lower():
                parts = date.split("+")
            else:
                parts = date.lower()

            if len(parts) != 5:
                offset = int(parts[1].strip())
            else:
                offset = 0

            if "-" in date.lower():
                return (datetime.today() - timedelta(days=offset)).date()
            elif "+" in date.lower():
                return (datetime.today() + timedelta(days=offset)).date()
            else:
                return datetime.today().date()
        else:
            return datetime.strptime(date, "%Y-%m-%d").date()

    @staticmethod
    def standardize_date_format(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str

        # Manually format the date to ensure no leading zeros on the day
        day = parsed_date.day
        month = parsed_date.strftime('%m')
        year = parsed_date.year

        return f"{day}/{month}/{year}"

    @staticmethod
    def date_format_with_age(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str

        today = datetime.today()
        age = today.year - parsed_date.year - ((today.month, today.day) < (parsed_date.month, parsed_date.day))

        day = parsed_date.day  # Day without leading zero
        month = parsed_date.strftime('%B')  # Full month name
        year = parsed_date.year  # Full year

        return f"{day} {month} {year} (aged {age})"

    @staticmethod
    def date_format_with_day_of_week(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str

        # Manually format the date to include the day of the week without leading zero for the day
        day_of_week = parsed_date.strftime('%A')
        day = parsed_date.day
        month = parsed_date.strftime('%B')
        year = parsed_date.year

        return f"{day_of_week} {day} {month} {year}"

    @staticmethod
    def date_format_with_name_of_month(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str.strftime("%d %B %Y")

        day = parsed_date.day
        month = parsed_date.strftime('%B')
        year = parsed_date.year
        return f"{day} {month} {year}"

    @staticmethod
    def date_format_with_name_of_month_shortened(date_str):
        try:
            # Try parsing the date as '%d/%m/%Y'
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            try:
                # If parsing fails, try parsing as '%m/%d/%Y'
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                # If parsing as both formats fails, return the original string
                return date_str.strftime("%d %b %Y")

        day = parsed_date.day
        month = parsed_date.strftime('%b')
        year = parsed_date.year
        return f"{day} {month} {year}"

class DatetimeHelper(BaseDatetimeHelper):
    def __init__(self):
        super().__init__()
