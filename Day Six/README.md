### Day Six: descriptive statistics
Dot's finished their cleaning, and the house now looks fabulous. They survey their work with a satisfied smile. And their friends said a city-dweller like them would never be able to get their hands dirty like this — well, Dot sure showed them! Suddenly, a drop of water hits their face. As they look up, they realize that the roof is littered with holes! The landlord sure didn't mention this!

Dot's measuring the sizes of all the different holes in the roof. They need to know how much material to purchase to patch them up. Can you help them?

#### Tutorial
Part of the job of data scientists and data analysts is to understand the data and extrapolate certain findings. In most cases, the first step of understanding a numerical data set is to look at the descriptive statistics. Descriptive statistics are brief descriptions that summarize datasets. There are many great Python libraries we can use to get descriptive statistics from numerical datasets. One such library is Pandas. We won't be going too in-depth with pandas today, just the basics to understand how to use pandas to get some general descriptive statistics. We will be covering pandas extensively and going over some of the advanced functions starting on Day 8.

Pandas is one of the most widely used Python plugins. Pandas can be used when working with large data sets or performing data cleaning, manipulation, and analysis.

Since the Pandas library is external to base Python, we will need to import it. When importing, we give an alias to pandas to shorten our code when calling on functions from pandas. Instead of writing pandas.name_of_function() we'll be able to write pd.name_of_function(). The alias pd is standard within the Python community.

import pandas as pd # we must import our external python plugin

list_of_num = [1,2,3,4,5]

series = pd.Series(list_of_num) 
                                
                                #converting our list_of_num to a pandas series variable
                                
                                #we need to do this to use some of pandas' useful descriptive statistics functions

series.max()    #outputs maximum value in Pandas Series

series.min()    #outputs minimum value in Pandas Series

series.mean()   #outputs average value in Pandas Series

series.median() #outputs median value in Pandas Series

series.mode()   #outputs mode value in Pandas Series

To read more on descriptive statistics, read this article.

To learn more about the various pandas functions, check out user guide in the pandas documentation.

Why should I use the documentation?

On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. However, there are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work.

Challenge:

There are many holes in the living room's ceiling that desperately need to be fixed. Dot's measured them, and in total there are about 100. They need to figure out how much does it cost to fix all of the holes. Differently sized holes will require differently sized patches to fix them.

        '''
            Size of Hole	                        Cost to Fix
            
            Small (less than 20 mm)	$1.30
            Medium (above or equal to 20 mm AND less than 70mm)	$1.60
            Large (above or equal to 70 mm)	$2.10
        '''
Dot needs you to look at the measurements and figure out the answers to the following questions:

1. What is the average sized hole?
2. What is the average cost to fix a hole?
3. What is the total cost of fixing all of the holes?

Note: Use a for loop and an if else statement to answer Q3.
Stretch Question:

Stretch Questions are not required to be completed to finish the challenge but are recommended to further develop your skills.

1. What is the maximum sized hole?
2. What is the minimum sized hole?

Output:

In order to get the average, convert the hole_sizes variable into series. 
Then use series.mean() to get the mean average.

To get the average cost, set count_small, count_medium and count_large to zero.
Then loop thru hole_sizes then check each i if it is:
        
        '''
                i < 20 then count_small
                i >= 20 and i < 70 then count_medium
                i > 70 then count_large
        '''
Average cost should be:

        '''
            ((count_small * 1.3)+(count_medium * 1.6)+(count_large * 2.1)) / 100
            100 = because there's only 100 items in random
        '''
Total cost would be:

        '''
               if i < 20:
                    then total_cost + 1.3
               elif i >= 20 and i < 70:
                    then total_cost + 1.6       
               else:
                    then total_cost + 2.1
        '''