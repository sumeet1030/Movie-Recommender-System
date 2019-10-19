import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
 return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
 return df[df.title == title]["index"].values[0]


df=pd.read_csv("movie_dataset.csv") #loading the dataset


feature=["keywords","cast","crew","director"]



for i in feature:
    df[i]=df[i].fillna('')


df["features"]=df["keywords"]+df["cast"]+df["crew"]+df["director"]



cv=CountVectorizer()

count_matrix=cv.fit_transform(df["features"])



similarity_score=cosine_similarity(count_matrix)


movie_user_likes="Spectre"

movie_index=get_index_from_title(movie_user_likes)

similar_movies=list(enumerate(similarity_score[movie_index]))

sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)

i=0
for movie in sorted_similar_movies:
    if i<10:
        print(get_title_from_index(movie[0]))
        i=i+1
    else:
        break
