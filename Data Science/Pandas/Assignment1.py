"""
# 1. Create + Inspect + Basic Cleaning
# Create a DataFrame from a dict (at least 10 rows).
# Show .head() , .info() , .describe(include="all") .
# Convert a date column to datetime.
# Trim whitespace from string columns
"""
import pandas as pd

dict_data = {"Name":[" Dhanesh"," Pranav"," Vaibhav","Aniket","Rohit"
                     ,"Yash "," Aditya","Arron","Roshan","Arin"],
             "Age": [22,23,24,21,25,24,20,24,23,21],
             "BirthDate":["23/08/2003","24/04/2004","24/05/2001","02/04/2004"
                          ,"27/02/2003","23/08/2003","24/04/2004","24/05/2001"
                          ,"02/04/2004","27/02/2003"]
            }
#creating DataFrame
df= pd.DataFrame(dict_data)  

# Show .head() , .info() , .describe(include="all") .
print(df.head())   #show first 5 records

print("information about the DataFrame.\n")
df.info()

print(df.describe())

# Convert a date column to datetime.
df["BirthDate"]=pd.to_datetime(df["BirthDate"])
print(df.head())

# Trim whitespace from string columns
print("\nBefore Trim WhiteSpace Name Col:",df.head())
df["Name"]=df["Name"].str.strip()
print("\nAfter Trim WhiteSpace Name Col:\n\n",df.head())