import csv
import statistics
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    # def convert_temp_in_f(temp_c):
#     temp_f = (temp_c - 32) * (5/9)
#     return temp_f

# print(convert_temp_in_f(350))
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")



def convert_f_to_c(temp_in_fahrenheit):
    
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round((float(temp_in_fahrenheit) - 32)/1.8, 1)

    



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    return statistics.mean(map(float,weather_data))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(file)
        list_of_lists = []
        for line in reader: 
            if line != []:
                list = [line[0], int(line[1]), int(line[2])]
                list_of_lists.append(list)
        return list_of_lists


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data:
        min_val = min(weather_data)
        for i in range(len(weather_data)):
            if weather_data[i] == min_val:
                index = i
        return float(min_val), index
    else:
        return ()


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data:
        max_val = max(weather_data)
        for i in range(len(weather_data)):
            if weather_data[i] == max_val:
                index = i
        return float(max_val), index
    else:
        return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    n = len(weather_data)
    date_list = []
    min_list = []
    max_list = []
    for value in weather_data:
        date_list.append(value[0])
        min_list.append(value[1])
        max_list.append(value[2])
    min_value, min_pos = find_min(min_list)
    min_temp = convert_f_to_c(min_value)
    min_date = convert_date(weather_data[min_pos][0])
    max_value, max_pos = find_max(max_list)
    max_temp = convert_f_to_c(max_value)
    max_date = convert_date(weather_data[max_pos][0])
    min_mean_value = calculate_mean(min_list)
    min_mean = convert_f_to_c(min_mean_value)
    max_mean_value = calculate_mean(max_list)
    max_mean = convert_f_to_c(max_mean_value)
    return f"{n} Day Overview\n  The lowest temperature will be {min_temp}{DEGREE_SYMBOL}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}{DEGREE_SYMBOL}, and will occur on {max_date}.\n  The average low this week is {min_mean}{DEGREE_SYMBOL}.\n  The average high this week is {max_mean}{DEGREE_SYMBOL}.\n"


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    for value in weather_data:
        date = convert_date(value[0])
        min_temp = convert_f_to_c(value[1])
        max_temp = convert_f_to_c(value[2])
        result += f"---- {date} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n"
    return result
