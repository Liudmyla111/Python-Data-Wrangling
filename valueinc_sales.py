#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:38:57 2022

@author: Liudmyla.Shepetiuk
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#mathematical operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

#CostPerTransaction Column Calculation

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#SalesPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup Calculation

data['Markup'] = data['ProfitperTransaction'] / data['CostPerTransaction']

#Rounding Marking

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#Combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#checking columns data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using split to split the client_keywords field

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merge files

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day', 'Month', 'Year'], axis = 1)

#Export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)















