#Secodn assignment code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

netflix = pd.read_csv("netflix_titles.csv")

print(netflix.head())

#Printing info relating to the dataset

netflix.info()
netflix.describe()

#How many movies are in the dataset

num_movies = netflix["show_id"].value_counts()
print(num_movies)

num_moves_per_country = netflix[["show_id", "country"]].value_counts()
print(num_moves_per_country)

empty_values = netflix.isna().sum()
print(empty_values)

titles_empty_values = netflix[netflix.isnull().any(axis=1)]
print(titles_empty_values)