import pandas as pd 
import numpy as np
#Use the read_csv(...) method from Pandas (Documentation Link) to read data
#from file Salaries.csv and to copy it into a dataframe.
#Make the column playerID in the csv file as the index column and the first row
#as the header. Also, skip the second row when reading the file.
Salaries = pd.read_csv('Salaries.csv', header=[0], index_col=[3], skiprows=[1])

#Select the id of the players who are registered in ATL and HOU whose salary is
#higher than one million.
RichALL = Salaries[Salaries["salary"] > 1000000]
RichATLHOU =  RichALL[RichALL["teamID"].isin(["ATL","HOU"])]

#Use the describe() method to calculate the standard deviation, first quartile, median,
#third quartile, mean, maximum, and minimum of the salary in team ATL.
JustATL = Salaries[Salaries["teamID"].isin(["ATL"])]
ATLSalariesDesc = JustATL.describe(percentiles=None)

#Create a Python dictionary object whose keys are the headers of the dataframe
#created in the read_csv() exercise and values are Python list objects that contain
#data corresponding to the headers. Headers are column names.
salheaders = Salaries.columns
salariesdict = {}

#for k,v in Salaries.iterrows():

#    saldicdata = saldicdata + v

for k,v in Salaries.iterrows():
    

for i in salheaders:
    salariesdict[i] = "Toes"
print(salariesdict)


