
# Movie Recommender System

This Movie Recommender System is designed to provide personalized movie recommendations based on user input. The system utilizes natural language processing (NLP) techniques on movie tags and employs a similarity score to recommend movies similar to the user's selection.

# Data Source:
The dataset for this project is sourced from Kaggle and can be found https://www.kaggle.com/datasets/prabhakarz/tmdb-15000-movies-dataset-with-credits.

# Files in Repository

## app.py
This file contains the Streamlit application code. It allows users to input a movie and receive personalized recommendations.

## recommender.ipynb

A behind-the-scenes Jupyter notebook, revealing the intricate steps in the creation of the recommendation system. Witness the transformation of movie data, the orchestration of text vectorization, and the magical calculation of cosine similarity scores.
## movies.pkl

A precious pickle file born from the enchanting notebook, containing essential movie data. This file is a key ingredient in the spellbinding recipe for creating the Cinematic Symphony Recommender.
## similarity.pkl

Another magical pickle file crafted in the notebook, holding the secrets of cosine similarity between movies. This file contributes to the harmonious symphony of recommendations on the Cinematic Symphony website.

# How it Works
## 1.Data Preprocessing:

The dataset is imported and basic preprocessing techniques are applied using pandas in a Jupyter notebook.
The dataset is transformed to contain only two columns: "movie name" and "tags," where "tags" consolidates all relevant information for each movie.
## 2.Text Vectorization:

The tags column is converted into vectors using text vectorization techniques such as bag of words. Users can choose any suitable text vectorization method.
## 3.Similarity Score Calculation:

Sklearn's similarity score is employed to calculate the similarity between movies based on their vectorized tags.
The calculated similarity score and the movies dataset are then saved as pickle files.
## 4.Recommendation System:

The Streamlit app uses the preprocessed data and similarity scores to recommend movies.
Users input a movie, and the system returns a list of recommended movies along with their posters.

# Fetching Posters using TMDB API
In order to fetch movie posters dynamically, you'll need to obtain a TMDB API key. Here's how you can get one:

### TMDB API Key
1. Visit TMDB website https://developer.themoviedb.org/ and create an account.
2. Once logged in, go to the "Settings" page, and under the "API" section, you can request an API key.
### Using the API Key in app.py

After obtaining the API key, replace the placeholder **YOUR_TMDB_API_KEY** in the **fetch_poster** function in **app.py** with your actual TMDB API key.

```
# fetch poster
def fetch_poster(movie_id):
  api_key = 'YOUR_TMDB_API_KEY'
  response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
  data=response.json()
  return "https://image.tmdb.org/t/p/original"+data['poster_path']
```

## Features

- **Light/Dark Mode Toggle** Experience the Movie Recommender System in a visually comfortable environment. Toggle between light and dark modes based on your preference.

- **Live Previews** Get real-time previews of recommended movies along with their posters. Visualize the cinematic gems before making your selection.

- **Fullscreen Mode** Immerse yourself in the cinematic world by activating fullscreen mode. Enjoy an uninterrupted movie exploration experience.

- **Cross Platform** Access the Movie Recommender System seamlessly across different platforms. Whether you're on a computer, tablet, or mobile device, the system is optimized for your viewing pleasure.


## Feedback

If you have any feedback, please mail us at nitinbdkt777@gmail.com


## 🚀 About Me
I'm a Data Scinetist and Analyst...


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nitin-budhlakoti-460125253/)


## Installation

1. Clone the repository

```bash
  git clone https://github.com/your-username/movie-recommending-system.git

```
2. Install the required packages

```bash
  pip install -r requirements.txt
```
3. Run the Streamlit app

```bash
  streamlit run app.py

```
4. Enter a movie and click the "Recommend" button to get personalized movie recommendations.

    
## Tech Stack

**Client:** python, jupyter notebook, Streamlit

**Server:**  Streamlit localhost

