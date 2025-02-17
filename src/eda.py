# Exploratory data analysis
import pandas as pd

# Initialize dataframes for each dataset
books = pd.read_csv("../data/Books.csv") # Book metadata
ratings = pd.read_csv("../data/Ratings.csv") # Book ratings by user
users = pd.read_csv("../data/Users.csv") # User metadata

print(ratings.head())