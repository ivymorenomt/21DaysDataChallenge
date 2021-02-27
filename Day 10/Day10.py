'''
**Challenge**

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:
1. Total Milk Production
2.  Total Revenue

**How much revenue did the cow farm make in the year 2020?**
'''
import pandas as pd

df = pd.read_csv('milk_32.csv')
df = df.drop(columns=['Unnamed: 0'])

df

df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']
year_2020 = df['Month'].str.contains('20-')
year_2020

tot_2020 = df[year_2020].sum()['Total Revenue']
print(tot_2020)

''''
The total revenue is $202,149.76
'''

#Solution
df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']
df.head()
''''
Month	Monthly milk production: pounds per cow	Number of Cows	Total Milk Production	Price_Per_Pound	Total Revenue
0	07-Feb	589.0	30	17670.0	0.22	NaN
1	07-Mar	561.0	32	17952.0	0.22	NaN
2	07-Apr	640.0	35	22400.0	0.22	NaN
3	07-May	656.0	35	22960.0	0.22	NaN
4	07-Jun	727.0	35	25445.0	0.22	NaN
'''

df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']
df.tail(15)
'''
Month	Monthly milk production: pounds per cow	Number of Cows	Total Milk Production	Price_Per_Pound	Total Revenue
153	19-Nov	812.0	62	50344.0	0.32	16110.08
154	19-Dec	773.0	62	47926.0	0.32	15336.32
155	20-Jan	813.0	62	50406.0	0.32	16129.92
156	20-Feb	834.0	62	51708.0	0.32	16546.56
157	20-Mar	782.0	62	48484.0	0.32	15514.88
158	20-Apr	892.0	62	55304.0	0.32	17697.28
159	20-May	903.0	62	55986.0	0.32	17915.52
160	20-Jun	966.0	62	59892.0	0.32	19165.44
161	20-Jul	937.0	62	58094.0	0.32	18590.08
162	20-Aug	896.0	62	55552.0	0.32	17776.64
163	20-Sep	858.0	62	53196.0	0.32	17022.72
164	20-Oct	755.5	62	46841.0	0.32	14989.12
165	20-Nov	755.5	62	46841.0	0.32	14989.12
166	20-Dec	797.0	62	49414.0	0.32	15812.48
167	21-Jan	843.0	62	52266.0	0.32	16725.12
'''

revenue_2020 = df['Total Revenue'][155:167]
print(sum(revenue_2020))
# 202149.76

df_revenue_2019 = df[155:167]
df_revenue_2019
#df_revenue_2019['Total Revenue'].sum()

'''
Month	Monthly milk production: pounds per cow	Number of Cows	Total Milk Production	Price_Per_Pound	Total Revenue
155	20-Jan	813.0	62	50406.0	0.32	16129.92
156	20-Feb	834.0	62	51708.0	0.32	16546.56
157	20-Mar	782.0	62	48484.0	0.32	15514.88
158	20-Apr	892.0	62	55304.0	0.32	17697.28
159	20-May	903.0	62	55986.0	0.32	17915.52
160	20-Jun	966.0	62	59892.0	0.32	19165.44
161	20-Jul	937.0	62	58094.0	0.32	18590.08
162	20-Aug	896.0	62	55552.0	0.32	17776.64
163	20-Sep	858.0	62	53196.0	0.32	17022.72
164	20-Oct	755.5	62	46841.0	0.32	14989.12
165	20-Nov	755.5	62	46841.0	0.32	14989.12
166	20-Dec	797.0	62	49414.0	0.32	15812.48
'''