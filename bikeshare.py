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
    city=''
    while city not in CITY_DATA:
        input_city=input('Please enter name of city you are looking for (chicago/new york city/washington):')
        input_city=input_city.lower()
        if input_city in CITY_DATA:
            city=input_city
        else:
            print('Please enter the correct city!')
           

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    months=['all','january','february','march','april','may','june']
    while month not in months:
        input_month=input('Please enter month name you want to search:')
        input_month=input_month.lower()
        if input_month in months:
            month=input_month
        else:
            print('Month name you have entered is not available, please try again.')
                
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while day not in days:
        input_day=input('Please enter the name of day you are trying to search:')
        input_day=input_day.lower()
        if input_day in days:
            day=input_day
        else:
            print('Please enter the correct name of the day!')


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day of week']=df['Start Time'].dt.dayofweek
    df['hour']=df['Start Time'].dt.hour
    
    
    months=['january','february','march','april','may','june']
    if month in months:
       month=months.index(month)+1
       df=df[df['month']==month]
    else:
       df
                                    
    
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    if day in days:
       day=days.index(day)+1
       df=df[df['day of week']==day]
    else:
       df
                                    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month=df['month'].mode()[0]
    print('The most common month that people are riding the bicycle in : {}'.format(most_month))

    # TO DO: display the most common day of week
    most_dow=df['day of week'].mode()[0]
    print('The most common day of week for people riding the bicycle is {}'.format(most_dow))

    # TO DO: display the most common start hour
    most_hour=df['hour'].mode()[0]
    print('The most common start hour for people to ride the bicycle is {}'.format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start=df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(most_start))

    # TO DO: display most commonly used end station
    most_end=df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(most_end))

    # TO DO: display most frequent combination of start station and end station trip
    most_com=(df['Start Station']+' and '+df['End Station']).mode()[0]
    print('The most frequent combinantion of start and end station trip as follow : {}'.format(most_com))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trav=df['Trip Duration'].sum()
    print('The total travel time of the bicycle is {}'.format(tot_trav))

    # TO DO: display mean travel time
    mean_trav=df['Trip Duration'].mean()
    print('The average travel time of the bicycle is {}'.format(mean_trav))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_t=df['User Type'].value_counts()
    print('Type of users who ride the bicycle as follow : \n{}'.format(user_t))
   
    # TO DO: Display counts of gender
    if True:
        try:
            gender=df['Gender'].value_counts()
            print('Type of genders who ride the bicycle as follow :\n {}'.format(gender))
        except:
            print('The gender data not available')
    # TO DO: Display earliest, most recent, and most common year of birth
    if True:
        try:
            earl_b=df['Birth Year'].min()
            rec_b=df['Birth Year'].max()
            most_b=df['Birth Year'].mode()[0]
            print('The earliest, most recent and most common birth year as follow respectively:\n{};\n{};\n{}'.format(earl_b,rec_b,most_b))
        except:
            print('The birth year data not available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print('In case you are curious about raw bikeshare data.')
    input_data=input('Do you want to see raw data of bikeshare?').lower()  
    start=0
    end=5
    while True: 
        if input_data=='yes': 
            print(df.iloc[start:end])
            start+=5
            end+=5
            input_data=input('Would you like to see next data?(Yes or No):').lower()  
        if input_data=='no':
            break
        
       
                  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
