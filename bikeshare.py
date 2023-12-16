import time
import pandas as pd
import numpy as np
import re

#Features Needed:
    
    #STAT Output:
    #Popular times of travel (most common month, day, week)
    #Popular stations (start, stop, most common route)
    #Trip Duration (total travel time, avg. travel time)
    #User Info (user type count, genser count, birth stats)
    
    #Rerun program if user wants

city_data = {'chicago': 'data/chicago.csv',
            'nyc': 'data/new_york_city.csv',
            'washington': 'data/washington.csv'}

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
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(city_data[city], parse_dates=['Start Time', 'End Time'])

    mask = pd.Series()
    mask2 = pd.Series()
    
    #create mask based on month filter
    if month == 'jan':
        mask = (df['Start Time'] > '2017-01-01') & (df['Start Time'] < '2017-02-01')
    elif month == 'feb':
        mask = (df['Start Time'] > '2017-02-01') & (df['Start Time'] < '2017-03-01')
    elif month == 'mar':
        mask = (df['Start Time'] > '2017-03-01') & (df['Start Time'] < '2017-04-01')
    elif month == 'apr':
        mask = (df['Start Time'] > '2017-04-01') & (df['Start Time'] < '2017-05-01')
    elif month == 'may':
        mask = (df['Start Time'] > '2017-05-01') & (df['Start Time'] < '2017-06-01')
    elif month == 'jun':
        mask = (df['Start Time'] > '2017-06-01') & (df['Start Time'] < '2017-07-01')
    elif month == 'all':
        mask = (df['Start Time'] > '2017-01-01') & (df['Start Time'] < '2017-07-01')
    
    #create mask based on day filter
    if day == 'm':
        mask2 = (df['Start Time'].dt.dayofweek == 0)
    elif day == 't':
        mask2 = (df['Start Time'].dt.dayofweek == 1)
    elif day == 'w':
        mask2 = (df['Start Time'].dt.dayofweek == 2)
    elif day == 'th':
        mask2 = (df['Start Time'].dt.dayofweek == 3)
    elif day == 'f':
        mask2 = (df['Start Time'].dt.dayofweek == 4)
    elif day == 's':
        mask2 = (df['Start Time'].dt.dayofweek == 5)       
    elif day == 'su':
        mask2 = (df['Start Time'].dt.dayofweek == 6)    
    elif day == 'all':
        mask2 = (df['Start Time'].dt.dayofweek < 7)
    
    #return filtered dataframe using masks
    print('-'*40)
    return df.loc[mask].loc[mask2]

def time_stats(df, month, day):
    #Displays statistics on the most frequent times of travel.
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    if month == 'all':
        top_month = df['Start Time'].dt.month.value_counts().idxmax()
        print("The most common month is {}\n".format(top_month))
    
    # display the most common day of week
    if day == 'all':
        top_dow = df['Start Time'].dt.dayofweek.value_counts().idxmax()
        print("The most common day of week is {}\n".format(top_dow))
    
    # display the most common start hour
        top_hour = df['Start Time'].dt.hour.value_counts().idxmax()
        print("The most common start hour is {}\n".format(top_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    #Displays statistics on the most popular stations and trip.
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    s1 = df['Start Station'].value_counts().idxmax()
    print("Start Station: {}\n".format(s1))
    
    # display most commonly used end station
    s2 = df['End Station'].value_counts().idxmax()
    print("End station: {}\n".format(s2))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' TO ' + df['End Station']
    s3 = df['Trip'].value_counts().idxmax()
    print("Trip: {}\n".format(s3))
    
    print('-'*40)

def trip_stats():
    #TO DO
    print('-'*40)

def user_stats():
    #TO DO
    print('-'*40)

if __name__ == "__main__":
    city, month, day = get_filters()
    df = load_data(city, month, day)
    
    #time_stats(df, month, day)
    station_stats(df)