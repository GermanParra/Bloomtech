import pandas as pd
# Classes represent some entity
# Class to represent a vehicles

# Classes have variables and fuctions
# Variables associated with Objects/Classes are call Attributes
# Fuctions associated with Objects/Classes are call Methods

df = pd.DataFrame({'A':[1,2,3] , 'B':[4,5,6]})

# Data Frame Attributes
 # Attributes have no parenthesis
print(df.shape)
print(df.index)
print(df.dtypes)

# Data Frame Methods
 # Attributes do have parenthesis
print(df.isnull())
print(df.head())
print(df.describe())