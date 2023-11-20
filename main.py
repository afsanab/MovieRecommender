import pandas as pd

# Load the dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Explore the data
print(movies.head())
print(ratings.head())