import pandas as pd


# Functions to determine holidays
def is_new_year(date_str):
    date = pd.to_datetime(date_str)
    return 1 if (date.month == 12 and date.day == 31) or (date.month == 1 and date.day == 1) else 0
    
def is_christmas(date_str):
    date = pd.to_datetime(date_str)
    return 1 if (date.month == 12 and date.day == 25) else 0

def is_black_friday(date_str):
    date = pd.to_datetime(date_str)
    return 1 if (date.month == 11 and date.day >= 23 and date.day <= 29 and date.weekday() == 4) else 0

def is_cyber_monday(date_str):
    date = pd.to_datetime(date_str)
    return 1 if (date.month == 11 and date.day >= 26 and date.day <= 30 and date.weekday() == 0) else 0

def is_valentines_day(date_str):
    date = pd.to_datetime(date_str)
    return 1 if (date.month == 2 and date.day == 14) else 0


# Dictionary mapping holiday names to their respective functions
holidays = {
    'new_year_indicator': is_new_year,
    'christmas_indicator': is_christmas,
    'black_friday_indicator': is_black_friday,
    'cyber_monday_indicator': is_cyber_monday,
    'valentines_day_indicator': is_valentines_day
}


def add_holiday(df):
    result = df.copy()
    
    # Add holiday indicators
    for holiday_name, holiday_func in holidays.items():
        result.loc[holiday_name] = result.columns.map(holiday_func)
    
    return result
