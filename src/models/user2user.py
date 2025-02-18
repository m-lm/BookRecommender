# Implementation of User-to-User Collaborative Filtering.
# Based on the idea that users who rate similar books highly have similar taste.

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import coo_matrix

# Initialize dataframes for each dataset
books = pd.read_csv("../../data/Books.csv") # Book metadata
ratings = pd.read_csv("../../data/Ratings.csv") # Book ratings by user
users = pd.read_csv("../../data/Users.csv") # User metadata

def create_ratings_matrix():
    # Creates a sparse ratings matrix comprised of book ratings and users
    isbn_to_index = {isbn: i for i, isbn in enumerate(books["ISBN-13"])}
    ratings["ISBN-13"] = ratings["ISBN-13"].map(isbn_to_index)
    num_books = len(books)
    num_users = len(users)
    ratings_matrix = coo_matrix((ratings["Book-Rating"].values, (ratings["User-ID"].values, ratings["ISBN-13"].values)), shape=(num_users, num_books))
    return ratings_matrix

def predict_rating(user_id, book_id, similarity_matrix, ratings_matrix):
    pass

def recommend_books(user_id, k, ):
    pass

ratings_matrix = np.array([
    [5, 3, 0, 2],
    [4, 0, 5, 1],
    [1, 4, 3, 5]
])