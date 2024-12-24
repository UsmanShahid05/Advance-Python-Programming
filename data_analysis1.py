'''
import pandas as pd
import numpy as np

data={"Name":["Usman","Ajmal",np.nan,"Tariq"],
      "Age":[23,22,14,20],
      "City":["BWP",np.nan,"Multan","Lahore"]}
print(data)

df=pd.DataFrame(data)
print(df)

print(df.isna())
print(df.notna())
df_dropped_data=df.dropna()
print(df_dropped_data)
print(df)

# Renaming the columns
df.rename(columns={"Name":"Student Name","Age":"Student Age","City":"Student City"},inplace=True)
print(df)


df.rename(index={0:"First",1:"Second",2:"Third",3:"Fourth"},inplace=True)
print(df)

'''

#=============================================#
# New code Script
print("\n\n\t==============================\n\n")

#import pip
#import os
# os.system("python -m pip install pandas")
#os.system("python -m pip install numpy")
import pandas as pd
import numpy as np

# Creating sample Dataframe with missing values
data={
    "A":[1,2,np.nan,4,5],
    "B":[np.nan,2,3,np.nan,5],
    "C":["cat","dog","dog","cat",np.nan],
    "D":[1,2,3,4,5]
    }

print(data)

# Creating pandas dataframe using "data"
df=pd.DataFrame(data)
print(df)

# Handing missing data values
print(f"\nChecking for missing values with isna()\n")

print(f"Missing values will appears as True in the DataFrame \n",df.isna())

# Droping columns with any missing values
print("\nDropping columns with any missing values")
print(f'\nRemaining columns with no NaN value\n',df.dropna())

# Filling missing values with a special values
print("\nFilling missing values with fillna()\n")
#print(df.fillna(value={"A":0,"B":df["B"].mean(),"C":"Unknown"}))
print(df.fillna(value={"A":50,"B":df["B"].mean(),"C":"Known"}))


# Dropping duplicate values in the dataframe
# Firstly creating duplicate columns in datafrme
df_duplicate=df._append(df.iloc[1],ignore_index=True)
print(df_duplicate)

# Dropping duplicate values
print("\nDropping duplicate values.\n")
print(df_duplicate.drop_duplicates())


# Replacing values using replace() method
print("\nReplacing cat and dog values with feline and canine respectively using 'replace()' method.")
print(df.replace({'cat':"feline","dog":"Canine"}))

# Renaming columns
print("\nRenaming columns using 'rename()' method.")
print(df.rename(columns={"A":"Alpha","B":"Bravo"}))
df=df.rename(columns={"A":"Alpha","B":"Bravo"})
print(df.rename(index={0:"First",1:"Second",2:"Third",3:"Fourth"}))

# Outliers
# Outliers are the values that seems far away from the means or avarage vlaues in the dataframe
# For simplicity, consider values greater than 4 in col'D', as outliers
print(df[df['D']<4])


#Permutation
#Permutations are the set of samples in sequences
print('\nPermutated DF rows using sample(frac=1):')
# Frac values range from 0 to 1, as 1 shows 100%.
print(df.sample(frac=.5).reset_index(drop=True))

df=df.rename(index={0:"First",1:"Second",2:"Third",3:"Fourth",4:"Fifth"})
print(df)
















