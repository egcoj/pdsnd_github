import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('CHOOSE A CITY: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("CHOOSE A CITY BETWEEN chicago, new york city OR washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('CHOOSE MONTH: ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('CHOOSE A MONTH BETWEEN: january, february, march, april, may, june OR all: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("CHOOSE A DAY BETWEEN:all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: " ).lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("CHOOSE A VALID DAY OR all FOR ALL OF THEM:").lower()

    print('-'*40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = "january"
    elif popular_month == 2:
        popular_month = "february"
    elif popular_month == 3:
        popular_month = "march"
    elif popular_month == 4:
        popular_month = "april"
    elif popular_month == 5:
        popular_month = "may"
    elif popular_month == 6:
        popular_month = "june"
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Common_Start_Station = df['Start Station'].mode()[0]
    print('Most Commonly used start station: ', Common_Start_Station)


    # TO DO: display most commonly used end station
    Common_End_Station = df['End Station'].mode()[0]
    print('Most Commonly used end station:', Common_End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    Combination_Station = df['Start To End'].mode()[0]
    print('Most Commonly used combination of start station and end station trip:', Combination_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = round(df['Trip Duration'].sum() / 3600)
    print('Total travel time: ', Total_Travel_Time, ' hours')

    # TO DO: display mean travel time
    Mean_Travel_Time = round(df['Trip Duration'].mean() / 60)
    print('Average travel time: ', Mean_Travel_Time, ' minutes')

    # TO DO: display longest trip time and details
    Longest_trip_duration = round(df['Trip Duration'].max() / 60)
    print('\nLongest trip time: ', Longest_trip_duration, ' minutes')
    print(df.loc[df['Trip Duration'] == df['Trip Duration'].max(),['Trip Duration','Start Station', 'End Station']])
    print("\n")

    # TO DO: display shortest trip time and details
    Shortest_trip_duration = round(df['Trip Duration'].min() / 60)
    print('Shortest trip time: ', Shortest_trip_duration, ' minutes')
    print(df.loc[df['Trip Duration'] == df['Trip Duration'].min(),['Trip Duration','Start Station', 'End Station']])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nUsers repartition by genders:\n' , user_gender)
    except:
        print("\nGENDER data is NOT AVAILABLE for your selection.")



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print("\nThe EARLIEST YEAR OF BIRTH is ",earliest_year_of_birth,
          ", the MOST RECENT YEAR OF BIRTH is ",most_recent_year_of_birth,
           "and the MOST COMMON YEAR OF BIRTH is ",most_common_year_of_birth,'.')
        print("\nOldest Customer is ",int(2022 - earliest_year_of_birth)," years")
        print("\nYoungest Customer is ",int(2022 - most_recent_year_of_birth)," years")
        print("\nThe average age of a Customer is ",int(2022 - most_common_year_of_birth)," years")
    except:
        print('\nBIRTH YEAR data is NOT AVAILABLE for your selection')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_raw_data(df):
    view_raw_data = input("\nDO YOU WANT TO VISUALISE THE FIRST 5 LINES OF RAW DATA? PLEASE CHOOSE yes OR no :").lower()
    start_line = 0
    while view_raw_data == "yes":
        print(df.iloc[start_line:start_line + 5])
        start_line += 5
        view_raw_data = input("\nDO YOU WANT TO VISUALISE THE NEXT 5 LINES OF RAW DATA? PLEASE CHOOSE yes OR no :").lower()

    return df

def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            view_raw_data(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
        main()

# Check my Github profile: https://github.com/egcoj
