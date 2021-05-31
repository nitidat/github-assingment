import pandas as pd

"""
    This script will analyze Bike usage of Divvy Bikeshare with data input from 3 cities -
    namely, Chicago, New York City and Washington. Statistics are computed based on input by
    the user for city, month and day of the week. The following information is computed -
        # Popular times of travel - pop_time
        # Popular stations and trip - pop_station
        # Trip duration -trip_duration
        # User info - user_stats
        # Present raw data - raw_data
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():

    #Function to get input from user to specify city, month and day

    print('Hello! Welcome to Divvy Bikeshare page. We will present bikeshare data of your favorite city!')

    city = ''

    while city not in CITY_DATA.keys():
        print("Please choose your city:")
        print("chicago, new york city or washington?")

        #You will find this happening at every stage of input throughout this
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("Please check your input city - it should be one of the three cities mentioned above")

    print(f"You have chosen {city.title()} as your city.")
    return city


def get_day_month():

    #Function to get input from user to specify month and day

#Creating a dictionary to store months
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in month_dict.keys():
        print("Please enter the month, between January to June, for which you're seeking the data:")

        print("You may also choose data for all months. If so, please type 'all' or 'All' or 'ALL'")
        month = input().lower()

        if month not in month_dict.keys():
            print("Invalid input!!!!!!!! Please try again in the accepted input format.")


    print(f"You have chosen {month.title()} as your month.")

#Creating a list to store all the days including the 'all' option
    days_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in days_list:
        print("Please enter a day of the week - monday, tuesday, wednesday, thursday, friday, saturday, sunday or ALL:")

        day = input().lower()

        if day not in days_list:
            print("Invalid input. Please try again.")

    print(f"You have chosen {day.title()} as your day.")

    #Returning the month and day selections
    return month, day

def load_data(city, month, day):

    #This function loads data for the specified city and filters by month and day if applicable.

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print("You have chosen to view data for this city, month, day respectively:" , city, month, day)
    print('*'*80)
    return df


#Function to computes most popular start hour, most popular day and most popular month
def pop_time(df):
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day:', popular_day)

    popular_month = df['month'].mode()[0]

    print('Most Popular Month (1 = January,...,6 = June):', popular_month)
    print('*'*80)

#Function to calculate station related statistics
def pop_station(df):

    print('The Most Popular Stations and Trip...')
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Uses mode method to find the most common start station
    common_start_station = df['Start Station'].mode()[0]

    print('The most commonly used start station:', common_start_station)

    #Uses mode method to find the most common end station
    common_end_station = df['End Station'].mode()[0]

    print('The most commonly used end station:', common_end_station)
    print('*'*80)

#Function to calculate trip duration related statistics
def trip_duration(df):

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Uses sum method to calculate the total trip duration
    total_duration = df['Trip Duration'].sum()

    print('The total trip duration is:' , total_duration)
    print('*'*80)

#Function to calculate user statistics
def user_stats(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # print value counts for each user type
    user_type = df['User Type'].value_counts()

    print('The types of users by number are given below:', user_type)
    print('*'*80)

def raw_data(df):
#Function to display the data frame itself as per user request

    #Creating a list of acceptable user responses
    user_response_list = ['yes', 'no']
    rdata = ''

    counter = 0
    while rdata not in user_response_list:
        print("Do you wish to view the raw data? - yes or no")

        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in user_response_list:
            print("Please check your input - acceptable responses are 'yes' or 'no'")

    #Ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             print("Goodbye!")
             break

    print('*'*80)

#Main function to call all the previous functions
def main():
        city = get_city()
        month, day = get_day_month()
        df = load_data(city, month, day)

        pop_time(df)
        pop_station(df)
        trip_duration(df)
        user_stats(df)
        raw_data(df)

if __name__ == "__main__":
    main()
