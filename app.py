import numpy as np
import pandas as pd

movies = pd.read_csv('movies_dataset.csv')
credits = pd.read_csv('movies_dataset.csv')
# movies.head(1)
credits.head(1)['cast'].values