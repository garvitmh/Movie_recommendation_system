import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=40fe765cf358d1c4d417ee7095e82d14&language=en-US")

    data = response.json()

    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/300.png"



def recommend(movie_name):
    movie_index = movie_list[movie_list['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movie_list.iloc[i[0]].id
        recommended_movies.append(movie_list['title'].iloc[i[0]])
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies , recommended_movies_poster

movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similiraty.pkl', 'rb'))

st.title("Movie :red[Recommender] system")

selected_movie_name = st.selectbox(
    "Select a Movie of your liking",
    movie_list['title'].values
)
st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    names , posters = recommend( selected_movie_name)

    col1, col2, col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])

    with col8:
        st.text(names[7])
        st.image(posters[7])

    with col9:
        st.text(names[8])
        st.image(posters[8])

    with col10:
        st.text (names[9])
        st.image(posters[9])