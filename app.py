import streamlit as st
import pickle 
import requests
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

# fetch poster
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=327e937f4b9ab44bf9e49790bdf665e0'.format(movie_id))
    data=response.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

# recommend movie
def recommend(movie_name):
    movie_index=movies[movies['title']==movie_name].index[0]
    distances=similarity[movie_index]
    recommend_movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
 
    recommended_movies=[] 
    recommended_movies_poster=[]
    for i in recommend_movie_list:
        # getting movie id
        movie_id=movies.iloc[i[0]].movie_id
        # fetching poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
        # storing recommended movie
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_poster

st.title("Movie Recommender")
movie=st.selectbox('Enter the movie',sorted(movies['title'].unique()))
if st.button('Recommend'):
    names,posters=recommend(movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
    #    st.write(f'<span style="font-size: 15px;">{names[0]}</span>', unsafe_allow_html=True)
       st.image(posters[0],caption=names[0])

    with col2:
    #    st.write(f'<span style="font-size: 15px;">{names[1]}</span>', unsafe_allow_html=True)
       st.image(posters[1],caption=names[1])

    with col3:
    #    st.write(f'<span style="font-size: 15px;">{names[2]}</span>', unsafe_allow_html=True)
       st.image(posters[2],caption=names[2])

    with col4:
    #    st.write(f'<span style="font-size: 15px;">{names[3]}</span>', unsafe_allow_html=True)
       st.image(posters[3],caption=names[3])

    with col5:
    #    st.write(f'<span style="font-size: 15px;">{names[4]}</span>', unsafe_allow_html=True)
       st.image(posters[4],caption=names[4])

    with col1:
    #    st.write(f'<span style="font-size: 15px;">{names[5]}</span>', unsafe_allow_html=True)
       st.image(posters[5],caption=names[5])

    with col2:
    #    st.write(f'<span style="font-size: 15px;">{names[6]}</span>', unsafe_allow_html=True)
       st.image(posters[6],caption=names[6])

    with col3:
    #    st.write(f'<span style="font-size: 15px;">{names[7]}</span>', unsafe_allow_html=True)
       st.image(posters[7],caption=names[7])

    with col4:
    #    st.write(f'<span style="font-size: 15px;">{names[8]}</span>', unsafe_allow_html=True)
       st.image(posters[8],caption=names[8])

    with col5:
    #    st.write(f'<span style="font-size: 15px;">{names[9]}</span>', unsafe_allow_html=True)
       st.image(posters[9],caption=names[9])