### Day 10: pandas data modification
Dot shakes hands with the farmer after finalizing the purchase of the most beautiful cow on the farm, who's name is Bessie. They bring Bessie over to their cabin and set her up on the front lawn. Dot stares into the eyes of their new four-legged friend, envisioning all the good times they might have. Eating grass. Standing. Sleeping. Staring blankly into the distance. What a life they could have together!

But, another thought is starting to bother Dot...they're just one person, and they're not sure how much milk they'd be able to drink. They like putting dairy in their coffee and cereal just as much as anyone else, but drinking a tall glass of milk on its own kinda grosses them out.

What are they gonna do with all this milk? Ah-ha - maybe they can sell it! But how profitable will that be?

#### Tutorial
When working with data, sometimes you'll want to create new columns from the data you have. This can enhance your analysis, and uncover hidden insights from the data.

In pandas, you can perform the standard order of operations on a new column from other columns. Check out the examples below.

    
    df['new_column'] = df['column_1'] + df['column_2']
    df['new_column'] = df['column_1'] * df['column_2']

    df['new_column'] = (df['column_1'] + df['column_2'])/(df['column_1'])

To learn more about the various pandas functions, check out the user guide in the pandas documentation.

Why should I use the documentation?

On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. However, there are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work.

#### Challenge

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

- Total Milk Production
- Total Revenue
- How much revenue did the cow farm make in the year 2020?