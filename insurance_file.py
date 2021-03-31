# -*- coding: utf-8 -*-
"""
Some possible ideas for analysis are the following:

Find out the average age of the patients in the dataset.
Analyze where a majority of the individuals are from.
Look at the different costs between smokers vs. non-smokers.
Figure out what the average age is for someone who has at least one child in this dataset.
"""

import os
os.chdir(r"C:\Users\bdobson\Documents\collette\codecademy course\python-portfolio-project-starter-files\python-portfolio-project-starter-files")
import csv
import pandas as pd


with open('insurance.csv', newline='') as insurance_csv:
  print(insurance_csv.read())
  
df = pd.read_csv('insurance.csv')
print(df)

""" average age two ways : 1) using pandas
    2) manually
    """
mean_age=df[["age"]].mean()
print(mean_age)

age = df["age"]

mean_age = sum(age)/len(age)

"""
where are individuals from
"""
region = df["region"]
print(type(region))

region_count={x:0 for x in region.unique()}
for regions in region:
    region_count[regions]+=1

df.region.value_counts()
"""
smoker vs non smoker insurance costs
"""

smoker =df[df["smoker"].isin(["yes"])]
print(smoker)


mean_smoker_cost = smoker[["charges"]].mean()
print(mean_smoker_cost)

def smoking_costs(x):
    mean_cost = sum(x["charges"])/len(x)
    return mean_cost
    
smoking_cost_calc=smoking_costs(smoker)

print(smoking_cost_calc)

non_smoker =df[df["smoker"].isin(["no"])]
print(non_smoker)

mean_non_smoker_cost = non_smoker[["charges"]].mean()
print(mean_non_smoker_cost)

non_smoking_cost_calc=smoking_costs(non_smoker)
print(non_smoking_cost_calc)

"""
avg age of person with 1 child in dataset
"""

people_with_kids = df[df["children"] >1]
print(len(people_with_kids))
mean_parent_age = people_with_kids[["age"]].mean()
print(mean_parent_age)

def avg_age(x):
    mean_age = sum(x["age"])/len(x)
    return mean_age

parent_age= avg_age(people_with_kids)
print(parent_age)