# Past Spotify Listening History and Changes in Mood Analysis

## Project Overview
My name is Yiğit Onur Yılmaz (Student ID: 31981) and I am a sophomore Computer Science student in Sabancı University. Here is DSA 210 term project details which utilizes my raw Spotify data which is requested from Spotify's official website. This project analyzes my Spotify listening history over past years to assess mood changes based on the genres of music I listened to. Using Python, the data is processed to group each track by genre, allowing for a data-driven exploration of personal mood trends over time.

## Features
- Extract and preprocess Spotify listening history data.
- Classify tracks into genres using a Python-based grouping algorithm.
- Visualize genre distribution and trends over time to infer mood changes.
- Manage and track project progress using version control with GitHub.

---

## Table of Contents
1. [Project Motivation](#project-motivation)
2. [Data Collection](#data-collection)
3. [Methodology](#methodology)
4. [Technologies Used](#technologies-used)
5. [Visualizations](#visualizations)
6. [Expected Outcomes](#expected-outcomes)

---

## Project Motivation
Music is a powerful reflection of emotions and moods. Most people associate particular emotions with particular music genres. 
By analyzing the genres of songs I’ve listened to, this project aims to:
- Gain insights into personal mood shifts over time.
- Understand the role of music genres in mood regulation.
- Apply data science techniques for a real-world, personalized analysis.

---

## Data Collection
The project uses Spotify's data export feature to retrieve my listening history. Key attributes include:
- **Track Name**
- **Artist**
- **Listening Timestamp**
- **Track Duration**

### Genre Mapping
Genres are classified based on artist information using the Spotify Web API or a pre-defined dataset for mapping artists to genres.

---

## Methodology
1. **Data Preprocessing**: 
   - Clean and format the raw Spotify data for analysis.
   - Handle missing or incorrect entries.

2. **Genre Grouping**:
   - Match each track to a genre using a Python script.
   - Utilize libraries such as `spotipy` for API-based genre retrieval.

3. **Trend Analysis**:
   - Aggregate listening data by genre over time.
   - Visualize trends to assess correlations with mood.

4. **Mood Assessment**:
   - Infer mood patterns based on dominant genres.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - Data Handling: `pandas`, `numpy`
  - Visualization: `matplotlib`
  - API Interaction: `spotipy`
- **Version Control**: Git and GitHub

---

## Visualizations

### Here is a descriptive table for showing which type of table will be used for displaying certain aspect of the data.

| **Visualization**        | **Description**                                                                                          | **Example Chart Type**     |
|---------------------------|----------------------------------------------------------------------------------------------------------|----------------------------|
| **Genre Distribution**    | Displays the percentage of total listening time spent on different music genres.                        | Pie Chart                  |
| **Mood Analysis**         | Links genres to inferred moods, highlighting dominant moods during specific time periods.               | Heatmap or Bar Chart       |
| **Listening Frequency**   | Analyzes the number of tracks played daily, weekly, or monthly to identify periods of increased activity.| Histogram or Line Chart    |

---

## Expected Outcomes

By creating this project, I aim to:

- Visualize trends in my music listening behavior over time.
- Quantify the relationship between listening frequency and mood changes.
- Identify favorite genres and their share of total listening time.
- Examine whether certain genres are associated with specific moods.
- Illustrate if there is a correlation between listening patterns and seasonal trends.

