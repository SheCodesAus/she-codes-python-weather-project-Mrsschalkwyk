import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"
# print(format_temperature("32")) #this is just to check it is not correst

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # print(round(((float(temp_in_farenheit) - 32) * 5/9), 1))
    return round(((float(temp_in_farenheit) - 32) * 5/9), 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # if weather_data == []:
    #             return ()
    # else:
    #     min_temp = weather_data[0]
    #     min_location = 0
    #     index = 0
    #     for num in weather_data:
    #         if float(num) <= float(min_temp):
    #             min_temp = float(num)
    #             min_location = index
    #         index +=1
    #     return min_temp, min_location




    if weather_data == []:
                return ()
    else:
        length = len(weather_data)
        total_low_temp = 0
        for low_temp in weather_data:
            total_low_temp += float(low_temp)
        total_low_temp /= length
        return total_low_temp
    




def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    lst = []

    with open(csv_file, mode = 'r', encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        for index,line in enumerate(csv_reader):
            if line != [] and index !=0:
                lst.append([line[0],int(line[1]),int(line[2])])
    # print(lst)
    return lst
    # lst=[]
    # with open(csv_file, mode='r', encoding="utf-8" ) as csv_object:
    #     reader = csv.reader(csv_object)
    #     for line in reader:
    #         if line != []:
    #             lst.append (line)
    # lst.pop(0)
    # return lst







def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
#    """
     
    if weather_data == []:
            return ()
    else:
            min_temp = weather_data[0]
            min_location = 0
            index = 0
            for num in weather_data:
                if float(num) <= float(min_temp):
                    min_temp = float(num)
                    min_location = index
                index +=1
            return min_temp, min_location


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
            return ()
    else:
        max_temp = weather_data[0]
        max_location = 0
        index = 0
        for num in weather_data:
            if float(num) >= float(max_temp):
                max_temp = float(num)
                max_location = index
            index +=1
        return max_temp, max_location
    
        

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    # Setting Variables
    summary = ""
    low_temps = []
    high_temps = []
    lowest = [None, None]
    highest = [None, None]

    # Generating lists for the lowest and highest temperatures
    for line in weather_data:        
        low_temps.append(float(line[1]))
        high_temps.append(float(line[2]))

    # Finding the Lowest Temperature and the cooresponding Location
    _min = find_min(low_temps)
    lowest = convert_f_to_c(_min[0])
    low_location = convert_date(weather_data[_min[1]][0])

    # Finding the Highest Temperature and the cooresponding Location
    _max = find_max(high_temps)
    highest = convert_f_to_c(_max[0])
    high_location = convert_date(weather_data[_max[1]][0])
    
    # Calculating the Average Low
    avg_low = calculate_mean(low_temps)
    avg_low = convert_f_to_c(avg_low)

    # Calculating the Average High
    avg_high = calculate_mean(high_temps)
    avg_high = convert_f_to_c(avg_high)

    # Generating Output
    summary = str(len(weather_data))+" Day Overview\n"
    summary += (f"  The lowest temperature will be {format_temperature(lowest)}, and will occur on {low_location}.") + "\n"
    summary += (f"  The highest temperature will be {format_temperature(highest)}, and will occur on {high_location}.") + "\n"
    summary += (f"  The average low this week is {format_temperature(avg_low)}.") + "\n"
    summary += (f"  The average high this week is {format_temperature(avg_high)}.") + "\n"

    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summery = ""
    for line in weather_data:
        summery= summery + f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n"
    return summery
