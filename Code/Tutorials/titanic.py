import pandas as pd
titanic = pd.read_csv('titanic.csv')
print(titanic)
titanic.dtypes
ages = titanic["Age"]
age_sex = titanic[["Age", "Sex"]]