import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters() :
    print("hello let's explore some bike data")
    #get user input for city
    city = input('please tell us about the city you want to explore \n it must be one of the followings(chicago,new york city,washington)')
    while city.lower() not in ['chicago','new york city','washington']:
        print('please write a city from the provided ones')
        city = input()
    # get user's input for the month
    month = input('please write the the month about which you want to view data \n it has to be one of the following(all,january,february,march,april,may,june)')
    months = ['all','january','february','march','april','may','june']
    while month.lower() not in months :
        print('please write a month from the provided ones')
        month = input()
    #get user's input for day
    print("type the day you want to view data about\nplease type it as an integer all , saturday , sunday , ...")
    day = input()
    days = ['0','1','2','3','4','5','6','7']
    days_names = ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    while day.lower() not in days_names :
        print("please type the day like the provided ones above")
        day = input()
    
    print('-'*40)
    return city , month , day 

def load_data(city,month,day) :
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all' :
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower())+1
        df = df[df['month'] == month]
    if day != 'all' :
        
        df = df[df['day_of_week'].str.startswith(day.title())]
    return df 

def time_stats(df) :
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    month_names = ['january','february','march','april','may','june','july']
    most_common_month_as_number = df['month'].mode()
    print('The most common month is ' , (df['month'].mode()))
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()
    print('The most common day of week is',most_common_day[0])
    
    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()
    print('The most common start hour is',most_common_start_hour[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('Most commonly used start station is {}'.format(most_common_start_station)[:])
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    end_stations_count = df['End Station'].value_counts()
    print('Most commonly used end station is {} '.format(most_common_end_station)[:])
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + '--' + df['End Station']
    most_frequent_start_end_station_name = df['Combination'].mode()
    most_frequent_start_end_station = df['Combination'].value_counts()
    
    print('The most frequent combination of start station and end station trip is \n',most_frequent_start_end_station_name,'for',most_frequent_start_end_station[1],'times')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

    
def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time in days is',(total_travel_time/(3600*24)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in minutes is' , (mean_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    

def user_stats(df):
    
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('counts of user types is\n',count_user_types)
    # TO DO: Display counts of gender
  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
def main() :
    while True :
        city , month , day = get_filters()
        print('The data is about' , city.lower())##
        print('The month is ',month.lower())##
        print('The day is ', day.lower())
        
        df = load_data(city.lower(), month.lower(), day)
        
        start_index = 0
        end_index = 5
        max_end_index = (df.shape[0])-1
        while True :        
    #while max_end_index <= end_index :
            if start_index > 0 :
                print('here are the next 5 rows')
                print(df[ int(start_index) : int(end_index) ])
                if end_index > max_end_index :
                    print('now you have viewed the whole list\n')
                    break
        
            else :
                print('Would you like to see 5 rows from raw data ?\n')
                answer = input('yes or no \n')
    
            while answer.lower() not in ['no','yes']:
                print('please type a valid answer\n')
                answer = input('no or yes \n')
       
            else :
                if answer.lower() != 'yes' :
                    print('it seems you don\'t want to show raw data')
                    break
                elif answer.lower() == 'yes' :
                    #pd.set_option(“display.max_columns”,200)
                    print(df[ int(start_index) : int(end_index) ])
                    print('Would you like to view the next 5 rows')
                    answer = input('yes or no\n')
                    if answer.lower() == 'yes' :
                        start_index +=5
                        end_index += 5
                    else :
                        print('it seems you got what you want')
                        break
                        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city.lower() != 'washington':
            count_of_gender = df['Gender'].value_counts()
            print('Counts of gender is\n ' , count_of_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
            early_year_birth = df['Birth Year'].min()
            print('The earlisest year of birth is ' , int(early_year_birth))
            recent_year_birth = df['Birth Year'].max()
            print('The most recent year of birth is ' ,int(recent_year_birth))
            common_year_birth = df['Birth Year'].mode()
            print('The most common year of birth is ' ,int(common_year_birth[0]))
        else :
            print('These data is not privided in washington data')
        
    

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
   	main()