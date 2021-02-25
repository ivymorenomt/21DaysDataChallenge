### Day 9: pandas data cleaning & filling NaNs
Dot understands how cows work a bit more now. They got themselves really hyped up to rent a cow, and traversed down the road to the cow farm. Dot spent some time negotiating with the cow farmer how much it would be to rent a cow, then went over to take a look at the beasts and pick a favourite.

Examining the moo-ing creatures, a realization slowly sinks in. If Dot did rent out a cow, they would definitely get attached to it over the month. Having to give it back to the farmer would be heartbreaking! They think back to their youth, when they briefly took care of a friend's plankton. Giving the plankton back was one of the saddest moments of their life.

Maybe Dot isn't thinking big enough. What if they took a leap and bought an entire cow - would it be worth it? How much milk would they get out of it?

#### Tutorial
Many people who work heavily with data would agree that a lot of time is spent on data cleaning, and only a little on actually running models or analyzing.

Data cleaning consists of many different tasks, like handling missing data, reshaping data, and creating new data based on the given data (referred to as feature engineering).

For today's challenge we'll be looking at different methods for dealing with missing values, and we'll be using pandas to help us with basic data cleaning.

The equation for filling in missing values:

df['column_name'] = df['column_name'].fillna(value = 100)

df['column_name'] = df['column_name'].fillna(method = 'backfill')

Before you move forward, take a moment to reflect on these questions:

- How would filling our missing data with the median value vs. the mean value affect the distribution of our data?

- Look up the .fillna function in the pandas documentation, and find some different filling methods we could implement. What are they?

Now let's import our new data.

    '''
        import pandas as pd
        df = pd.read_csv('milk_2.csv')
        print(df.head(3)) #Inputing the value 3 inside the brackets of the df.head() function allows us to
                  #override the default value of 5.
        print('\n') # 
        print(df.shape)
    '''

    '''
        Month  Monthly milk production: pounds per cow  Number of Cows
    0  07-Feb                                    589.0            30.0
    1  07-Mar                                    561.0            32.0
    2  07-Apr                                    640.0            35.0
    
    (168, 3)
    '''
    
As you can see, there are three columns in our new data frame instead of 2 columns from the last challenge. However, sometimes showing what the data frame looks like doesn't tell us much; what if we want to understand the different data types?

There are two ways.

- df.info()
- df.dtypes

First, let's see what df.info() tells us. I will let you try out the second method yourself.
    
    '''
        df.info()
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 168 entries, 0 to 167
        Data columns (total 3 columns):
        #   Column                                   Non-Null Count  Dtype  
        ---  ------                                   --------------  -----  
        0   Month                                    168 non-null    object 
        1   Monthly milk production: pounds per cow  150 non-null    float64
        2   Number of Cows                           151 non-null    float64
      dtypes: float64(2), object(1)
      memory usage: 4.1+ KB
    '''

From the output above, df.info() gives us a good overview of our data frame. It tells us that there are 168 entries, with an index ranging from 0 to 167. It also provides us with the names of the columns, the count of all the non-null data for each column, and the data type for each column.

We also notice 150 non-null counts for our 2nd column and 151 non-null counts from our 3rd column. This indicates to us that there may be some missing rows.

Another method to check the count of how many rows with missing data for each column is by using the df.isnull() function.

    '''
        df.isnull().sum(axis = 0)
        Month                                       0
        Monthly milk production: pounds per cow    18
        Number of Cows                             17
        dtype: int64   
    '''

We can see from the functions we used that there are 18 rows missing in Monthly milk production: pounds per cow, and 17 rows missing from Number of Cows.

To learn more about the various pandas functions, check out user guide in the pandas documentation.

Why should I use the documentation?

On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. However, there are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work.

#### Challenge
Fill out the missing values in the monthly milk production column with the median, and fill out the number of cows column using the ffill method.

After filling in the missing values with our new data, answer these questions for Dot, so they can figure out the value of having a cow year-round:

- What is the average for monthly milk production?
- What is the standard deviation for monthly milk production?
- What is the average number of cows used?

