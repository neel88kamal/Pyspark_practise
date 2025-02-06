# Question 8 >

# use the drinksbycountry dataset to solve the following question
import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head(10)

drinks.loc[(drinks['continent']=='Africa')]

# find all the countries in africa who drink more beer than average beer consupution in europe?