import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1e0abc1f4bb5f5024d"
                 "a033cec3b8a2e2&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(a):
    movie_index = movies[movies["title"] == a].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]


    recommend_movies = []
    recommended_movies_poster=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        ## fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies , recommended_movies_poster


movies_list=pickle.load(open("total_movies.pkl","rb"))
movies =pd.DataFrame(movies_list)

similarity=pickle.load(open("similarity.pkl","rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    (movies["title"].values))

if st.button('Recommend'):
    name , poster = recommend(selected_movie_name)


    col1, col2, col3 ,col4 ,col5= st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])


#It's important to note that the specific algorithm used for collaborative filtering is not explicitly mentioned ' \
 # 'in the provided code. However, collaborative filtering is generally categorized into user-based and item-based' \
 # ' approaches. The code seems to use item-based collaborative filtering, as it calculates the similarity between ' \
 # 'movies based on user preferences.

#In summary, this code implements a movie recommender system using item-based collaborative filtering with
 #   a simple Streamlit interface.