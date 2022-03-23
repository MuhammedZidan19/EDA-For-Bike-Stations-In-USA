import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
days = ['monday', "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("Available Cities (chicago, new york city, washington)\nChoose The City : ").lower()

        if city in CITY_DATA.keys():
            break
        else:
            print("Sorry,Not Valid. Try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter Month Name To filter By Or all : ").lower()
        if month in months or month == "all":
            break
        else:
            print("Sorry,Not Valid. Try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter Dat Name To filter By Or all : ").lower()
        if day in days or day == "all":
            break
        else:
            print("Sorry,Not Valid. Try again.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name

    if month != 'all':
        df = df[df["month"] == months.index(month) + 1]

    if day != 'all':
        df = df[df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # display the most common month
    df["month"] = df["Start Time"].dt.month
    print('Most Common Month:', df["month"].mode()[0])

    # display the most common day of week
    df["day"] = df["Start Time"].dt.weekday_name
    print('Most Common Day:', df["day"].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most Common hour:', df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station:", df["Start Station"].mode()[0])

    # display most commonly used end station
    print("Most Common End Station:", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["Both"] = df["Start Station"] + df["End Station"]
    print("Most Common Frequent Combination of Start And End  Station:\n",
          df["Start Station"].mode()[0], " and ", df["End Station"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["Total Time"] = df["End Time"] - df["Start Time"]

    print("Total Travel Time:", df["Total Time"].sum())
    print("Total Average Time:", df["Total Time"].sum() / df["Total Time"].size)
    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of User Types:\n", df["User Type"].value_counts())

    if 'Gender' in df:
        # Display counts of gender
        print("Counts of Gender:\n", df["Gender"].value_counts())
        # Display earliest, most recent, and most common year of birth
        print("Most Recent Year Of Birth:", int(df["Birth Year"].min()))
        print("Most Earlier Year Of Birth:", int(df["Birth Year"].max()))
        print("Most Common Year Of Birth:", int(df["Birth Year"].mode()[0]))


    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    start_loc = 0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data != "no":
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            if start_loc + 5 > df.size or df.iloc[start_loc:start_loc + 5]["Start Time"].isnull().values.any():
                print(df.iloc[start_loc:start_loc + 5])
                print("Zero Rows Left")
                break
        else:
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
# 118075
