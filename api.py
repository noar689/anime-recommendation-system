from fastapi import FastAPI, HTTPException
from anime_recommendation1 import recommend_anime, df  # Import functions & dataset from main file
from enum import Enum

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working!"}

# Enum for available recommendation criteria
class RecommendationCriterion(str, Enum):
    genres = "genres"
    studios = "studios"
    geners_type = "genres_type"
    geners_status = "genres_status"
    genersrating = "genres_rating"



@app.get("/recommend")
def get_recommendations(anime_title: str,
                         choice: RecommendationCriterion = RecommendationCriterion.genres,
                         top_n: int = 10):
    # Debugging prints
    print(f"Received request: anime_title={anime_title}, choice={choice.value}, top_n={top_n}")

    # Validate anime title exists in the dataset
    if anime_title not in df["name"].values:
        raise HTTPException(status_code=404, detail="Anime not found in dataset.")
    
    # Handle the "studios" case if the anime has no studio information
    if choice.value == "studios" and df[df["name"] == anime_title]["studios"].values[0] == "":
        return {"message": "Anime not found or has no studio information"}
    
    # Get recommendations
    try:
        recommendations = recommend_anime(anime_title, choice.value, top_n)
        
        # Debugging: Print the result
        print("Recommendations generated successfully!")
        
        # If no recommendations found, return a message
        if recommendations is None or recommendations.empty:
            return {"message": "No recommendations found."}
        
        return {"recommended_animes": recommendations.to_dict(orient="records")}

    except Exception as e:
        print(f"Error in recommend_anime: {e}")  # Debugging
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")



