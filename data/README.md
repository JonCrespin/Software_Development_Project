# Software_Development_Project
# Project Title: Video Game Sales & Analysis Streamlit App

## Project Overview

This Streamlit app visualizes video game sales data and provides insights into sales performance by genre, developer, and critic scores. The app allows users to explore data related to video games, including total sales across various platforms, and compare how critic scores influence total sales. The dataset used contains information about video game sales, publishers, developers, and other relevant attributes for 12,580 games.

The app allows users to:
- Filter the data by console type.
- Visualize sales vs. critic scores.
- View sales distribution by genre and developer.
- Filter and explore the data interactively via Streamlit widgets.

## Key Features
- **Sales vs. Critic Score Histogram**: Visualizes the relationship between critic scores and total sales, with optional genre-based coloring.
- **Genre and Developer Sales**: Displays aggregated sales data by game genre and developer.
- **Data Filtering**: Allows users to filter the data by specific consoles (e.g., Xbox Series, PS4, etc.).

## Technologies Used
- **Streamlit**: For building the interactive web application.
- **Plotly**: For creating interactive visualizations.
- **pandas**: For data manipulation and cleaning.
- **NumPy**: For numerical operations.
- **Matplotlib & Seaborn**: For additional visualizations and styling.

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository-name
    ```

3. Install dependencies (if not already done):
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open the app in your browser (Streamlit will provide the local URL):
    ```bash
    # URL will look like this:
    http://localhost:8501
    ```

## Dataset Information

The dataset used in this project is called `vgchartz_2024.csv`, which contains data for 12,580 video games, including the following columns:

- **title**: The title of the video game.
- **console**: The platform or console the game was released on.
- **genre**: The genre of the game (e.g., action, sports).
- **publisher**: The game's publisher.
- **developer**: The game's developer.
- **critic_score**: The game's average critic score.
- **total_sales**: The total sales of the game (in millions).
- **release_date**: The date the game was released.
- **last_update**: The date the game's data was last updated.

**Note**: This dataset is anonymized and does not contain personal user data.

## How the App Works

- The app starts by loading the dataset, cleaning missing values, and parsing date columns for analysis.
- Users can select a console from a dropdown list to filter the data.
- The app visualizes the relationship between critic scores and total sales using a histogram.
- The user can choose to group the data by genre to see how sales perform across different genres.
- The app also shows a summary of the most popular games by developer and genre.
