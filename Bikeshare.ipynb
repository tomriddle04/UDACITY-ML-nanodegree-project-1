import pandas as pd
import numpy as np
import json
import time

def filtering_the_data():
    while True:
        city=input(print('which city data you want out of chicago new york or washington\n'))
        if city in cities:
            break
    month=input(print('enter the month name\n'))
    day=input(print('enter the day of the week\n'))
    return(city,month,day)

def load_data(city,month,day):
    name=pd.read_csv(CITY_DATA[city])
    name['Start Time']=pd.to_datetime(name['Start Time'])
    name['month']=name['Start Time'].dt.month
    name['hour']=name['Start Time'].dt.hour
    name['day']=name['Start Time'].dt.weekday_name
    if month!='None':
        month=months.index(month)+1
    if day!='None':
        name=name[name['day']==day.title()] 
    return(name)

def  popular_times_of_travel(name):
    most_common_month=name["month"].value_counts().idxmax()
    most_common_day_of_week=name["day"].value_counts().idxmax()
    most_common_hour_of_day=name["hour"].value_counts().idxmax()
    print('The most common month:',most_common_month)
    print('The most day of the week:',most_common_day_of_week)
    print('The most common hour:', most_common_hour_of_day)
def popular_station_trip(name):
    most_common_start_station=name['Start Station'].value_counts().idxmax()
    most_common_end_station=name['End Station'].value_counts().idxmax()
    #most_common_trip_from_start_to_end=name[['Start Station','End Station']].mode().loc[0]
    print('most_common_start_station is :',most_common_start_station)
    print(' most_common_end_station is :', most_common_end_station)
    #print("most commonly start and end station are :{},{}".format( most_common_trip_from_start_to_end[0],\
        #                                                           most_common_trip_from_start_to_end[1]))
    
def trip_duration(name):
    total_travel_time=name['Trip Duration'].sum()
    avg_travel_time=name['Trip Duration'].mean()
    print('total_travel_time is :',total_travel_time)
    print('avg_travel_time is :',avg_travel_time)    

def user_information(name):
    count_of_each_user_Type=name['User Type'].value_counts()
    gender_counts=name['Gender'].value_counts()
    most_common_year=name['Birth Year'].value_counts().idxmax()
    print('count_of_each_user_Type is :',count_of_each_user_Type)
    print('gender_counts is :',  gender_counts)
    print('most_common_year is :',most_common_year)    
    
while True:
    CITY_DATA={'chicago':'chicago.csv','new york city':'new_york_city.csv','washington':'washington.csv'}
    cities=['chicago','new york','washington']
    months=['january','february','march','april','may','june','august','september','october','november','december']
    days=['sunday','monday','tuesday','wednesday','thrusday','friday','saturday','sunday']
    city,month,day=filtering_the_data()
    name=load_data(city,month,day)
    popular_times_of_travel(name)
    popular_station_trip(name)
    trip_duration(name)
    user_information(name)
    z=input(print('enter yes to end the program:'))
    if(z=='yes'):
        break

                                                                              
            
            
            
            
            
    
    
    
