#Using the same logic as above calculate the final_price for only those bills that have a positibe value
prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
output = [price for price in prices if price>0]
print(output)

#find area of square whose radius is given in a list
radius = [10 ,11, 12, 13, 14, 15]

#using list comprehension
area_1 = [round(3.14*r*r,2) for r in radius]
print(area_1)

#using lambda function & map
area_2 = list(map(lambda r: 3.14*r*r , radius ))
print(area_2)

#how to sort a dictionary based on its value and not key
student = {"Ambika":85, "Joshna":88, "Bibek":99, "Anand":99, "Manala":100}

#methos-1, using an already defined function
def get_marks(s):
    return s.items[1]
values= list(x for x in student.values())
print(values)
#this way i can sort the values alone, but output is not coming as a sorted dictionary

# Method 2 , use sorted function
sorted_dict = sorted(student.items(), key=lambda stu_tup:stu_tup[1])
print(sorted_dict)


#question - how to convert from list of tuple to a dictionary
# A
# [('Ambika', 85), ('Joshna', 88), ('Bibek', 99), ('Anand', 99), ('Manala', 100)]
#to B
# {'Ambika': 85, 'Joshna': 88, 'Bibek': 99, 'Anand': 99, 'Manala': 100}

#A is list of tuple
tup1 = [('Ambika', 85), ('Joshna', 88), ('Bibek', 99), ('Anand', 99), ('Manala', 100)]
output_dict ={}
for i in tup1:
    output_dict[i[0]]=i[1]
print(output_dict)

#Rgex
# find all emails from a multi line string
import re
emails = """
pythonprogramming@gmail.com
python-programming-fun@happy-mail.edu
python123_programming456_fun@happy-mail.edu
"""
pattern = re.compile(r'[a-z0-9-_]+@[a-z0-9_-]+\.[a-z]{3}')
matches = pattern.finditer(emails)
for match in matches:
    print(match)

#pandas
import pandas as pd
chips_df = pd.read_table("http://bit.ly/chiporders", sep="\t")

def get_proper_col_names(col_name):
    return col_name.split("_")[-1][:5].strip()

print(list(map(get_proper_col_names, chips_df.columns)))

print(chips_df.head(15))

new_df= chips_df.loc[(chips_df["item_name"].isin(["Chicken"]))]
print(new_df.head(5))

new_df1 = chips_df.loc[(chips_df["item_name"].str.lower().str.contains("chicken")), :]
print(new_df1.head(5))


#how to convert datatype of a column in pandas
chicken_orders_df = chips_df.loc[(chips_df["item_name"].str.lower().str.find("chicken")!=-1), :]
#chicken_orders_df["price"] = chicken_orders_df["price"].str[1:].astype(float)

#drop a column from pandas
new_df = chips_df.drop(["quantity", "item_price"],axis=1)

#drop rows
chips_df.drop([4, 7, 8, 11], axis =0, inplace=False).head(15)


ufo = pd.read_csv("http://bit.ly/uforeports")
# check which rows have NaN values and how many NaN values are there in each row
print(ufo.isnull().sum(axis=0))

# fetch all the rows where City column is NaN
print(ufo.value_counts())
null_ufo= ufo.loc[ufo["City"].isna()]
print(null_ufo)


#ufo.dropna()
#how to drop records where city & shape reported is null
ufo.dropna(subset=["City", "Shape Reported"], how="any", inplace=True)

#how to drop null from a column,
ufo["Colors Reported"].value_counts(dropna=True).head(10)

# replace all the NaN in the series with the value UNKNOWN
#ufo["Colors Reported"].fillna(value="UNKNOWN", inplace=True)

#print(ufo.isna().sum(axis=0))


#describe the datafram => gives count, min, max, std
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.describe())

# get the mean bear servings for Europe
print(drinks.loc[drinks['continent']=='Europe', 'beer_servings'].mean())

#drinks.loc[(drinks["continent"]=="Asia"), "beer_servings"].agg([min, max])

# Find all countries in AFRICA that consume more beer than the average beer consumption in EUROPE
# Find the average beer consumption in Europe

avg_beer_europe = drinks.loc[drinks['continent']=='Europe','beer_servings'].mean()
print(f'avg is : {avg_beer_europe}')
avg_beer_europe2 = drinks.groupby('continent')["beer_servings"].mean()
print(avg_beer_europe2)
print(avg_beer_europe2['Europe'])

africa_df = drinks.loc[(drinks["continent"]=='Africa') & (drinks["beer_servings"] > avg_beer_europe), :]
print(africa_df)


#how to set existing column an index of a df
drinks.set_index(["country"], inplace=False)
#how to reset index
drinks.reset_index(inplace=True)
#rename index column back to contry
drinks.rename(columns={"index":"country"}, inplace=False)

