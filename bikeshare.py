import time
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

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

    #----------------------------------------------------------------------
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #using 1-3 as options instead of manually typing to reduce errors. then converting to city name using if statement
    while True:
        mychoice = input('Please select a city number to analyze the city data:\n   Chicago: 1\n   New York City: 2\n   Washington: 3\n').strip()
        if mychoice.isnumeric():
            if int(mychoice) in range(1,4):
                #convert to int
                #select city based on inputted choice
                if int(mychoice) == 1:
                    city = 'chicago'
                elif int(mychoice) == 2:
                    city = 'new york city'
                else:
                    city = 'washington'
                break
            else:
                print('This is not a valid choice! Please try again')
        else:
            print('Your input was not a number. Please choose a number [1:3]')


    #----------------------------------------------------------------------

    # get user input for month (all, january, february, ... , june) as a number to minimize input errors
    while True:
        month_in = input('select a month for the analysis\n   January = 1\n   February = 2\n   ...\n   November = 11\n   December = 12\n   or type 0 for all\n').strip()
        #check if input is numeric
        if month_in.isnumeric():
            if int(month_in) in range(0,13):
                #convert month number to string month name or all if 0 is inputted
                if int(month_in) ==0:
                    month = 'all'
                else:
                    #code from https://www.yodiaditya.com/convert-month-name-into-number-month-number-to-month-name-in-python/, modified to fit my need
                    formatted_month = datetime(2019, int(month_in), 1)
                    month = formatted_month.strftime("%B")
                break
        else:
            print('Your input should be a number and between 0 and 12')


    #----------------------------------------------------------------------
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_in = input('Please select the day you want to analyze:\n Monday: 0\n Tuesday: 1\n ...\n Saturday: 5\n Sunday: 6\n or 7 for all\n' ).strip()

        if day_in.isnumeric():
            if int(day_in) in range(0,8):
                break
        else:
            print('This is not a valid choice')

    #convert the numeric input into day of week
    day_in = int(day_in)
    if day_in == 7:
        day = 'all'
    else: #code from https://stackoverflow.com/questions/36341484/get-day-name-from-weekday-int
        day = calendar.day_name[day_in]
    #----------------------------------------------------------------------
    print('-'*40)
    return city, month, day

    #----------------------------------------------------------------------
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
    df= pd.read_csv(CITY_DATA[city])

    #preparing the data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['start stop']= df['Start Station'] + '/' +df['End Station']
#----------------------------------------------------------------------
    #Apply month filter
    #print(df['Start Time'].dtype)
    if month != 'all':
        df = df[(df['month'] == month)]


#----------------------------------------------------------------------
    #apply day of week filter

    if day != 'all':
        df = df[(df['day']== day.title() )]


#----------------------------------------------------------------------
    #print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month is: {}'.format(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most popular day of the week is: {}'.format(popular_day))
    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('Most popular hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most popular end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most popular start/end station combination: {}'.format(df['start stop'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of user types is: \n{}\n\n\n'.format(df['User Type'].value_counts()))
    a=input('Press Enter to continue')
    #verify if the columns gender and birth year are available in the data
    #code from  https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
    if 'Gender' in df:
    # TO DO: Display counts of gender
        print('The count of gender is: \n{}\n\n\n'.format(df['Gender'].value_counts()))
        a=input('Press Enter to continue')

    if 'Birth Year' in df:
    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest birth year is: {}\nMost recent birth year is: {}\nMost common birth year is: {}\n\n\n'.format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_source(df):
    """"displays the raw data, 5 rows at a time as long as the user continues to type 'yes' in the             promp

        Args:
            df: the dataframe it will use to printout
    """

    for n in range(0,len(df.index)-5,5):
        #choose the correct prompt if at the beginning of the loop
        if n == 0:
            answer = input('Do you want to view the source data? \nyes/no\n').strip().lower()
        else:
            answer = input('Do you want to continue? \nyes/no\n').strip().lower()

        #evaluate the input
        if answer == 'no':
            break
        elif answer == 'yes':
            print(df[n:n+5])
        else:
            print('not a valid prompt')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # asking for input between functions to improve readability of outputs

        time_stats(df)
        a=input('Press Enter to continue')
        station_stats(df)
        a=input('Press Enter to continue')
        trip_duration_stats(df)
        a=input('Press Enter to continue')
        user_stats(df)
        a=input('Press Enter to continue')
        view_source(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
