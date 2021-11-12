import pandas as pd
import requests
import streamlit as st
import pickle

def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=1715acb6d6443a724775241a68a1a42b&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommented_movies=[]
    recommented_movies_posters=[]

    for i in movies_list:
        movie_id=i[0]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommented_movies.append(movies.iloc[i[0]].title)
        recommented_movies_posters.append(fetch_poster(movie_id))
    return recommented_movies,recommented_movies_posters

st.title("movie recommender system")

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])

