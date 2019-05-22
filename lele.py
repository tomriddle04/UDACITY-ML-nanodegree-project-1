#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


cd C:\Users\Abhishek\Desktop\final01


# In[3]:


#importing all the necessary functions and packages
import pandas as pd
import numpy as np
import json
import time
def filtering_the_data():
    while True:
        city=input(print('which city data you want out of chicago new york or washington\n'))
        city=city.lower()
        if city in cities:
            break
    while True:
        month=input(print('enter the month name\n'))
        month=month.lower()
        if month in months:
            break
    while True:
        day=input(print('enter the day of the week\n'))
        day=day.lower()
        if day in days:
            break
    return(city,month,day)


# In[4]:


"""load_data fun here selecting the data of a city which is given by user as a input and changing
    1.datatype of Start Time column.
    2.datatype of month column.
    3.datatype of hour and day column also.
    4.returning the file of data.
    5.print the first few lines of dataset.
"""
def load_data(city,month,day):
    name=pd.read_csv(CITY_DATA[city])
    name['Start Time']=pd.to_datetime(name['Start Time'])
    name['month']=name['Start Time'].dt.month
    name['hour']=name['Start Time'].dt.hour
    name['day']=name['Start Time'].dt.weekday_name
    show_data=input(print("press yes if you want to see the first 5 rows of your dataset"))
    show_data=show_data.lower()
    i=5
    while(show_data=='yes'):
        print('\n First 5 lines of your dataset is \n')
        print(name.head(i))
        show_data=input(print("press yes if you want to see the first 5 rows of your dataset"))
        show_data=show_data.lower()
        i=i+5
    if month!='None':
        month=months.index(month)+1
    if day!='None':
        name=name[name['day']==day.title()] 
    return(name)


# Popular times of travel
# - find most common month
# - find most common day of week
# - find most common hour of day
#     

# In[ ]:


"""this fun find
   1.most_common_month.
   2.most_common_day_of_week.
   3.most_common_hour.
"""
def  popular_times_of_travel(name):
    most_common_month=name["month"].value_counts().idxmax()
    most_common_day_of_week=name["day"].value_counts().idxmax()
    most_common_hour_of_day=name["hour"].value_counts().idxmax()
    print('\n The most common month:',most_common_month)
    print('\n The most day of the week:',most_common_day_of_week)
    print('\n The most common hour:', most_common_hour_of_day)
 
 


# Q.Popular stations and trip
# - find most common start station
# - find most common end station
# 

# In[ ]:


"""This fun find most_common_start station and most_common_end_station"""
def popular_station_trip(name):
    most_common_start_station=name['Start Station'].value_counts().idxmax()
    most_common_end_station=name['End Station'].value_counts().idxmax()
    #most_common_trip_from_start_to_end=name[['Start Station','End Station']].mode().loc[0]
    print('\nmost_common_start_station is :',most_common_start_station)
    print('\n most_common_end_station is :', most_common_end_station)
    #print("most commonly start and end station are :{},{}".format( most_common_trip_from_start_to_end[0],\
        #                                                           most_common_trip_from_start_to_end[1])              


# Q.Trip duration
# - Find total travel time
# - Find average travel time

# In[ ]:


"""This fun find out total sum of trip duration and average of trip duration """
def trip_duration(name):
    total_travel_time=name['Trip Duration'].sum()
    avg_travel_time=name['Trip Duration'].mean()
    print('\n total_travel_time is :',total_travel_time)
    print('\n avg_travel_time is :',avg_travel_time)   


# Q.Find the answer of the following questions
# - Counts of each user type
# - Counts of each gender

# In[ ]:


"""user_iformation is a fun which find the following things 
   1.count of each_gender_type.
   2.Most common year.
"""
def user_information(name):
    gender_counts=name['Gender'].value_counts()
    most_common_year=name['Birth Year'].value_counts().idxmax()
    print('\n gender_counts is :',  gender_counts)
    print('\n most_common_year is :',int(most_common_year)) 


# In[ ]:


"""each_user_type is a fun which find 
   the count of each user type
"""
def each_user_type(name):
    count_of_each_user_Type=name['User Type'].value_counts()
    print('\n count_of_each_user_Type is :',count_of_each_user_Type)
    


# In[ ]:


"""This block is the main body of code from here we call the other function to  perform specific 
   functionality.city_data is a dictionary which contain dataset of 3 town"""
while True:
    CITY_DATA={'chicago':'chicago.csv','new york':'new_york_city.csv','washington':'washington.csv'}
    cities=['chicago','new york','washington']
    months=['january','february','march','april','may','june','august','september','october','november','december']
    days=['sunday','monday','tuesday','wednesday','thrusday','friday','saturday','sunday']
    city,month,day=filtering_the_data()
    name = load_data(city,month,day)
    popular_times_of_travel(name)
    popular_station_trip(name)
    trip_duration(name)
    each_user_type(name)
    if(city!='washington'):
        user_information(name)
    z=input(print('enter yes to end the program:'))
    z=z.lower()
    if(z=='yes'):
        break
    


# In[ ]:





# In[ ]:




