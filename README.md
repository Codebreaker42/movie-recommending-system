Data Set Link
https://www.kaggle.com/datasets/prabhakarz/tmdb-15000-movies-dataset-with-credits


Movie Recommender System
Project Title: Movie Recommender System
Data Source:
The dataset for this project is sourced from Kaggle and can be found https://www.kaggle.com/datasets/prabhakarz/tmdb-15000-movies-dataset-with-credits

Author Information:
Name: Nitin Budhlakoti
Contact: Email - nitinbdkt777@gmail.com

Description:
This Movie Recommender System is designed to provide personalized movie recommendations based on user input. The system utilizes natural language processing (NLP) techniques on movie tags and employs a similarity score to recommend movies similar to the user's selection.

Files in Repository:
app.py: This file contains the Streamlit application code. It allows users to input a movie and receive personalized recommendations.
How it Works:
Data Preprocessing:

The dataset is imported and basic preprocessing techniques are applied using pandas in a Jupyter notebook.
The dataset is transformed to contain only two columns: "movie name" and "tags," where "tags" consolidates all relevant information for each movie.
Text Vectorization:

The tags column is converted into vectors using text vectorization techniques such as bag of words. Users can choose any suitable text vectorization method.
Similarity Score Calculation:

Sklearn's similarity score is employed to calculate the similarity between movies based on their vectorized tags.
The calculated similarity score and the movies dataset are then saved as pickle files.
Recommendation System:

The Streamlit app uses the preprocessed data and similarity scores to recommend movies.
Users input a movie, and the system returns a list of recommended movies along with their posters.

Usage:
Clone the repository:git clone https://github.com/your-username/movie-recommending-system.git
Install the required packages: pip install -r requirements.txt
Run the Streamlit app: streamlit run app.py

Enter a movie and click the "Recommend" button to get personalized movie recommendations.

Note:
For a detailed understanding of the data preprocessing and model creation, refer to the Jupyter notebook file in the repository.

Feel free to explore and enhance the system according to your preferences! If you have any questions or suggestions, contact Nitin Budhlakoti at nitinbdkt777@gmail.com.


