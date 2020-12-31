import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday","saturday", "sunday",]
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

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
    while True:
        city = input("Please enter city name (ex-> chicago, new york city or washington):\n")
        city = city.lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Wrong input!! please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("If you want filter by month please enter month or enter all if you dont:\n")
        month = month.lower()
        if month in MONTHS:
        # use the index of the months list to get the corresponding int
            month = MONTHS.index(month) + 1
            break
        else:
            if month == "all":
                break
            print("Wrong input!! please try again")
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:     
        day = input("If you want filter by day please enter day or enter all if you don't :\n")
        day = day.lower()
        if day in DAYS:
            break
        else:
            if day == "all":
                break
            print("Wrong input!! please try again")


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
    #open the targeted city data
    df = pd.read_csv(CITY_DATA[city])
    
    #convert Start time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    #extract and create new column for month and day
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    
    if month != "all":
        df = df[df["month"] == month]   
    if day != "all":
        df = df[df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Popular Month: ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most Popular Day Of Week: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print('Most Popular Start Hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most common start station: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("Most common end station: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df["User Type"].value_counts()
    print("Counts of user types ",counts_of_user_types)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        counts_of_gender = df["Gender"].value_counts()
        print("Counts of gender :",(counts_of_gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year_of_birth = df["Birth Year"].min()
        print("Earliest year of birth: ",earliest_year_of_birth)
        most_recent_year_of_birth = df["Birth Year"].max()
        print("Most recent year of birth: ",most_recent_year_of_birth)
        most_common_year_of_birth = df["Birth Year"].mode()[0]
        print("Most common year of birth: ",most_common_year_of_birth)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    str_msg_display = "Do you want to see the raw data?:(yes or no)\n"
    frame_start = 0
    frame_end = 5
    while True:
        display_data = input(str_msg_display).lower()
        if display_data == "yes":
            print(df.iloc[frame_start:frame_end])
            str_msg_display = "Do you wish to continue?:(yes or no)\n"
            frame_start = frame_end
            frame_end += 5 
            continue
        elif display_data == "no":
            break        
        else:
            print("Wrong input!! please try again")        
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
