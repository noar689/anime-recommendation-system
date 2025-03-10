# Anime Recommendation System

## Introduction

The **Anime Recommendation System** helps users discover new anime based on preferences using content-based filtering. It provides personalized recommendations through a FastAPI-based web service, allowing users to request anime suggestions based on genres, ratings, and other criteria.

## Features

- Fetch anime recommendations via API.
- Uses content-based filtering for recommendations.
- FastAPI backend with interactive Swagger UI.
- Supports filtering by genres, ratings, and other factors.
- Processes anime datasets for meaningful insights.

## Prerequisites

Ensure you have installed:
- Python 3.8+
- FastAPI
- Uvicorn
- Pandas, Numpy, Scikit-learn
- Matplotlib, Seaborn, Plotly (for visualization)
- Jupyter Notebook (for experimentation)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/anime-recommendation-system.git
   cd anime-recommendation-system
   ```
2. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Open Jupyter Notebook and run:
   ```sh
   jupyter notebook
   ```
5. Execute `anime_recommendation.ipynb` to generate recommendations.

## Running the API

Start the FastAPI server:
```sh
uvicorn api:app --reload
```

Access the interactive API documentation at:
```
http://127.0.0.1:8080/docs
```

### Example API Request
```
GET http://127.0.0.1:8080/recommend/?anime_name=Hunter%20x%20Hunter&criterion=genres
```

## Dataset Information

The system works with datasets containing:
- Anime titles
- Genres
- User ratings
- Popularity scores

## Methodology

- **Content-Based Filtering:** Uses metadata like genres and descriptions to find similar anime.

## Troubleshooting

- **500 Internal Server Error:** Check `api.py` and dataset loading.
- **Connection Refused:** Ensure Uvicorn is running on the correct port.
- **Module Not Found:** Verify dependencies and correct working directory.

## Future Enhancements

- Integrate deep learning for better recommendations.
- Develop a web-based UI.
- Expand dataset sources for improved accuracy.
- Implement real-time updates based on user feedback.
- Use sentiment analysis from user reviews.

## Contribution

Feel free to fork the repository, make improvements, and submit a pull request.

## License

MIT License. Free to use and modify.

