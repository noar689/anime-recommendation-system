import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Read the processed dataset from the 'dataset' directory
path = os.path.join(os.getcwd(), 'dataset', 'dataset_processed.csv')
df = pd.read_csv(path)
df["studios"] = df["studios"].fillna("")


# Display available recommendation criteria
print("Choose the recommendation criterion:")
options = ["genres", "studios", "genres_type", "genres_status", "genres_rating"]
# for option in options:
#     print(option) 

# Get user input for anime title and recommendation criterion



# Function to get the index of an anime by name
def anime_index_(anime_name):
    try:
        return df[df['name'] == anime_name].index[0]  # Return index of anime
    except IndexError:
        print("Anime not found")  # Handle case where anime is not found
        return None

# anime_index_(anime_title)  # Get the index of the user-selected anime

# Function to recommend similar anime
def recommend_anime(anime_name,choice, top_n=10):

 # Compute TF-IDF and Cosine Similarity for the selected feature
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df[choice])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


    anime_index = anime_index_(anime_name)  # Get anime index
    if anime_index is None:
        return None  # Return None if anime is not found
    
    similarities = list(enumerate(cosine_sim[anime_index]))  # Get similarity scores
    
    similarities = [item for item in similarities if item[0] != anime_index]  # Exclude the selected anime
    
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]  # Sort and get top recommendations

    similar_products = df.iloc[[int(i[0]) for i in similarities]].copy()  # Get recommended anime

    return similar_products[['name', 'type', 'status', 'studios', 'rating']]  # Return selected columns


anime_title='Hunter x Hunter'
choice='genres'
# Handle case where the chosen criterion is 'studios' and there is no studio info
if (choice == 'studios') & (df[df['name'] == anime_title]['studios'].values[0] == ''):
    recommendations = 'Anime not found or has no studio information'
else:
    recommendations = recommend_anime(anime_title, choice)  # Get recommendations

# Print the recommendations
print(recommendations)
