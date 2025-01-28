#!/usr/bin/env python
# coding: utf-8

# **Weather Data set**
# 
# A Time-Series data set 
# with per hour information
# about the weather conditions at a particular location.
# Records Temp, Dew point temp, Relative Humidity, Wind speed, Visibility, Pressure and Conditions
# 
# CSV file

# **Notes**
# 
# head() - It shows the first N rows in the data (by default, N=5).
# 
# shape - It shows the total no. of rows and no. of columns of the dataframe.
# 
# index - This attribute provides the index of the dataframe.
# 
# columns - It shows the name of each column.
# 
# dtypes - It shows the data-type of each column.
# 
# unique() - In a column, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe.
# 
# nunique() - It shows the total no. of unique values in each column. It can be applied on a single column as well as on the whole dataframe.
# 
# count - It shows the total no. of non-null values in each column. It can be applied on a single column as well as on the whole dataframe.
# 
# value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# 
# info() - Provides basic information about the dataframe.

# In[3]:


import pandas as pd


# In[10]:


data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\datasets\weatherData.csv")


# r is for removing unicode error

# In[15]:


data


# 8784 rows
# 
# 8 columns
# 
# Date/Time, Temp_C,	Dew Point, Temp_C,	Rel Hum_%,	Wind Speed_km/h, Visibility_km,	Press_kPa.	Weather

# head() - It shows the first N rows in the data (by default, N=5).
# 

# In[23]:


data.head()


# tail() - last 5 data

# In[26]:


data.tail()


# .shape - It shows the total no. of rows and no. of columns of the dataframe.

# In[38]:


data.shape


# index of the data frame
# starting from 0 and last position is 8784 and increment by 1

# In[43]:


data.index


# In[45]:


data.columns


# In[47]:


data.dtypes


# unique data values present in weather column

# In[53]:


data['Weather'].unique()


# In[56]:


data.nunique()


# total no. of non null val in each column. can apply on single column or whole dataset

# In[70]:


data.count


# In[82]:


data['Weather'].count


# .value_counts
# unique values with their count
# applied on single columns only

# In[85]:


data['Weather'].value_counts()


# In[87]:


data.info()


# Unique wind speed values in the data

# In[108]:


data.head(2)


# In[110]:


data.nunique()


# In[114]:


data['Wind Speed_km/h'].nunique()


# In[116]:


data['Wind Speed_km/h'].count()


# In[118]:


data['Wind Speed_km/h'].unique()


# number of times when the Weather is exactly clear

# using Value count

# In[121]:


data.columns


# In[123]:


data['Weather'].unique()


# In[152]:


data['Weather'].value_counts()


# In[169]:


clear = data['Weather'] == 'Clear'


# In[177]:


clear_count = clear.value_counts()


# In[183]:


clear_count


# In[185]:


clear_count[True]


# *Using Filtering*

# In[203]:


data[data.Weather == 'Clear']


# *using groupby*

# In[206]:


data.groupby('Weather').get_group('Clear')


# Number of times when the wind speed was exactly 4km/h

# In[209]:


data.head(2)


# In[229]:


windSpeed = data['Wind Speed_km/h'] == 4


# In[239]:


speed_4 = windSpeed.value_counts()


# In[241]:


speed_4


# In[253]:


speed_4[True]


# In[255]:


data[data['Wind Speed_km/h'] == 4]


# In[259]:


data.groupby('Wind Speed_km/h').get_group(4)


# All the null values in the data

# In[264]:


data.isnull().sum()


# In[266]:


data.notnull().sum()


# Rename the column name Weather in to Weather Condition

# In[271]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[275]:


data.head(1)


# In[279]:


data.rename(columns = {'Weather' : 'Weather Conditions'}, inplace = True)


# In[281]:


data.head(1)


# Mean Visibility

# In[286]:


data['Visibility_km'].mean()


# Standerd Deviation of Pressure

# In[291]:


data.Press_kPa.std()


# In[296]:


#if there is no space okay to use after . no need of []


# Varioance of Relative Humidity

# In[299]:


data['Rel Hum_%'].var()


# All instances when Snow was recorded

# In[302]:


data.head(1)


# In[310]:


data['Weather Conditions'].value_counts()


# In[314]:


snow = data['Weather Conditions'] == 'Snow'


# In[334]:


snow_count = snow.value_counts()


# In[336]:


snow_count[True]


# In[338]:


data.groupby('Weather Conditions').get_group('Snow')


# all instances when wind speed is above 24 and visibility is 25

# In[408]:


windSpd = data[data['Wind Speed_km/h'] > 24]


# In[410]:


vis = data[data['Visibility_km'] == 25]


# In[412]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# mean value of each column against each 'weather condition'

# In[415]:


data.head(1)


# In[421]:


data['Weather Conditions']


# In[425]:


data.groupby('Weather Conditions').mean(numeric_only=True)


# min and max val of each cell against weather condition

# In[428]:


data.groupby('Weather Conditions').min(numeric_only=True)


# In[432]:


data.groupby('Weather Conditions').max(numeric_only=True)


# Show all the records of weather condition is Fog

# In[445]:


data.head(1)


# In[451]:


data[data['Weather Conditions'] == 'Fog']


# In[453]:


data.groupby('Weather Conditions').get_group('Fog')


# all records when weather is clear and visibility is above 40

# In[458]:


data[(data['Weather Conditions']=='Clear') & (data['Visibility_km'] > 40)]


# weather clear and relative humidity > 50

# In[472]:


data[(data['Weather Conditions'] == 'Clear') & ((data['Rel Hum_%'] > 50) | (data['Visibility_km'] < 40))]


# In[476]:


data.rename(columns = {'Rel Hum_%' : 'rel_humdity'})


# In[478]:


data.head(1)


# In[480]:


data.rename(columns = {'Rel Hum_%' : 'Relative_humidity'}, inplace=True)


# In[482]:


data.head(1)


# In[ ]:




