# Spotify Data Analysis: New Song Discovery Patterns

## Project Overview
This project investigates user behavior on Spotify by analyzing when users are most likely to discover and add new songs to their playlists. Using historical Spotify technical log data, we test the hypothesis that specific time periods (e.g., holiday seasons or summer) influence new song discovery rates. 

Our findings aim to provide insights into seasonal music discovery trends and help enhance user recommendations and marketing strategies.

---

## Hypothesis
**Hypothesis**: Users are more likely to discover new songs during specific periods of the year.

- **Null Hypothesis (\(H_0\))**: New song additions are uniformly distributed across the year.
- **Alternative Hypothesis (\(H_1\))**: New song additions vary significantly during specific time periods.

---

## Objectives
1. Analyze Spotify listening history and identify patterns in new song discoveries.
2. Visualize trends in song discovery rates across months and seasons.
3. Perform statistical testing to validate the hypothesis using p-value analysis.

---

## Data Description
- **Source**: Spotify technical log data
- **Fields Extracted**:
  - `Timestamp`: When the song was added to the playlist
  - `Song ID`: Unique identifier for each song
  - `User ID` (optional): Identifier for user activity
  - Other song attributes (e.g., genre, popularity, release date)

---

## Methodology
1. **Data Preprocessing**:
   - Clean and structure raw Spotify log data.
   - Extract time-based features such as month and season.
   - Remove duplicate song entries.
   
2. **Exploratory Data Analysis (EDA)**:
   - Identify patterns in new song discoveries over time.
   - Visualize trends using bar charts, line graphs, and heatmaps.
   
3. **Hypothesis Testing**:
   - Conduct statistical tests (e.g., ANOVA) to evaluate seasonal variation in song discovery rates.
   - Determine p-values to validate the hypothesis.

4. **Results and Insights**:
   - Summarize findings with clear visualizations.
   - Discuss implications of seasonal discovery trends.

---

## Tech Stack
- **Languages**: Python
- **Libraries**:
  - Data Analysis: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`, `plotly`
  - Statistical Testing: `scipy.stats`
- **Tools**:
  - Jupyter Notebook
  - GitHub for version control

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/spotify-discovery-analysis.git
   cd spotify-discovery-analysis
