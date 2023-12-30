import time
import pandas as pd
import re


city_data = {
    "chicago": "data/chicago.csv",
    "nyc": "data/new_york_city.csv",
    "washington": "data/washington.csv",
}


def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    time_filter = ""
    city = ""
    month = ""
    day = ""

    # Ask for city
    while city == "":
        city = input("Select a city filter: Chicago, NYC, or Washington?\n").lower()
        if re.match("chicago|nyc|washington", city):
            print("We'll provide data for %s\n" % city.upper())
        else:
            city = ""
            print("Invalid input. Please enter a valid city.\n")

    # Check for filters
    while time_filter == "":
        time_filter = input("Would you like to filter by month, day or none?\n").lower()
        if re.match("month|day", time_filter):
            print("We will filter by %s.\n" % time_filter)
        elif time_filter == "none":
            print("We won't filter the data.\n")
        else:
            time_filter = ""
            print("Invalid input: Please enter month, day or none")

    # Filters
    if time_filter == "none":
        month = "all"
        day = "all"

    # Ask for month
    elif time_filter == "month":
        day = "all"
        while month == "":
            month = input(
                "Which month? january february march april may june?\n"
            ).lower()
            if not re.match("january|february|march|april|may|june", month):
                month = ""
                print("Invalid input. Please enter a valid month (january - june).\n")

    # Ask for day
    else:
        month = "all"
        while day == "":
            try:
                day = int(
                    input("Which day? Please type as an integer (e.g., 0=Monday?\n")
                )
                if day < 0 or day > 7:
                    day = ""
                    print(
                        "Invalid input. Please enter a valid month (or all): m \
                        t w th f s su all\n"
                    )
            except ValueError:
                print("Invalid input. Please enter a valid integer\n")

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """Loads csv data to dataframe, filtered by user inputs"""

    df = pd.read_csv(city_data[city], parse_dates=["Start Time", "End Time"])

    # Filter by month
    df["month"] = df["Start Time"].dt.month
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        df = df[df["month"] == months.index(month) + 1]

    # Filter by day
    df["day"] = df["Start Time"].dt.dayofweek
    if day != "all":
        df = df[df["day"] == day]

    # return filtered dataframe
    print("-" * 40)
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    if month == "all":
        top_month = df["Start Time"].dt.month_name().value_counts().idxmax()
        print("Most Common Month: %s\n" % top_month)

    # display the most common day of week
    if day == "all":
        top_dow = df["Start Time"].dt.day_name().value_counts().idxmax()
        print("Most Common Day of Week: %s\n" % top_dow)

    # display the most common start hour
    top_hour = df["Start Time"].dt.hour.value_counts().idxmax()
    print("Most Common Start Hour: %s\n" % top_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    s1 = df["Start Station"].value_counts().idxmax()
    print("Start Station: %s\n" % s1)

    # display most commonly used end station
    s2 = df["End Station"].value_counts().idxmax()
    print("End station: %s\n" % s2)

    # display most frequent combination of start station and end station trip
    df["Trip"] = df["Start Station"] + " TO " + df["End Station"]
    s3 = df["Trip"].value_counts().idxmax()
    print("Trip: %s\n" % s3)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total = df["Trip Duration"].sum()
    total_hours = round(total / (60 * 60))
    print("Total Travel Time: %s hours" % total_hours)

    # display mean travel time
    average_time = df["Trip Duration"].mean()
    average_time_min = round(average_time / 60)
    print("Mean Travel Time: %s minutes" % average_time_min)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts())

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts())

    if city != "washington":
        # Display counts of gender
        print("\n")
        print(df["Gender"].value_counts())

        # Display earliest, most recent, and most common year of birth
        low_year = int(df["Birth Year"].min())  # int removes floating zero
        recent_year = int(df["Birth Year"].max())
        common_year = int(df["Birth Year"].value_counts().idxmax())
        print("\nEarliest Year: %s\n" % low_year)
        print("Most Recent Year: %s\n" % recent_year)
        print("Most Common Year: %s\n" % common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def display_data(df):
    """Displays raw data to user 5 rows at a time"""

    view_data = input(
        "\nWould you like to view 5 rows of individual trip data? yes or no\n"
    ).lower()
    start_loc = 0
    while view_data == "yes":
        print(df.iloc[start_loc : start_loc + 5, :])
        start_loc += 5
        view_data = input(
            "\nWould you like to continue with 5 more? yes or no\n"
        ).lower()


if __name__ == "__main__":
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input("Would you like to restart: y/n?")
        if restart.lower() != "y":
            break
