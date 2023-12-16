import time
import pandas as pd
import numpy as np
import re

#Features Needed:
    #user input (city, month/day filter)
    
    #STAT Output:
    #Popular times of travel (most common month, day, week)
    #Popular stations (start, stop, most common route)
    #Trip Duration (total travel time, avg. travel time)
    #User Info (user type count, genser count, birth stats)
    
    #Rerun program if user wants

city_data = {'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv'}

def get_filters():
    #Asks user to specify a city, month, and day to analyze.
    city = ''
    month = ''
    day = ''
    
    #Ask for city
    while city == '':
        try:
            city = input("Which city do you want to analyze: Chicago, NYC, or Washington?\n").lower()
            if not re.match('chicago|nyc|washington', city):
                city = ''
                raise ValueError("Invalid input. Please enter a valid city.\n")
            else:
                print("We'll provide data for {}\n".format(city.upper())) 
        except ValueError:
            print("Invalid input. Please enter a valid city.\n")
    
    #Ask for month
    while month == '':
        try:
            month = input("Which month do you want to filter by (or all): jan feb mar apr may jun all?\n").lower()
            if not re.match('jan|feb|mar|apr|may|jun|all', month):
                month = ''
                raise ValueError("Invalid input. Please enter a valid month: jan feb mar apr may jun all\n")
            else:
                print("We'll filter by {}\n".format(month.upper())) 
        except ValueError:
            print("Invalid input. Please enter a valid month or all: jan feb mar apr may jun all\n")
    
    #Ask for day
    while day == '':
        try:
            day = input("Which day of the week do you want to filter by (or all): m t w th f s su all?\n").lower()
            if not re.match('m|t|w|th|f|s|su|all', day):
                day = ''
                raise ValueError("Invalid input. Please enter a valid month (or all): m t w th f s su all\n")
            else:
                print("We'll filter by {}\n".format(day.upper())) 
        except ValueError:
            print("Invalid input. Please enter a valid month (or all): m t w th f s su all\n")
    
    return city, month, day

def load_data():
    #TO DO
    return

def time_stats():
    #TO DO
    return

def station_stats():
    #TO DO
    return

def trip_stats():
    #TO DO
    return

def user_stats():
    #TO DO
    return

if __name__ == "__main__":
    city, month, day = get_filters()
    print('city:{} month:{} day:{}'.format(city, month, day))