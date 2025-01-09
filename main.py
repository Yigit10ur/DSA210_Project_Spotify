import pandas as pd
import json
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns

# Define file paths
file_paths = [
    'AddedToCollection.json',
    'AddedToRootlist.json',
    'CacheReport_Hourly.json',
    'BoomboxPlaybackSession_1.json',
    'AudioStreamingSettingsReport_Hourly.json',
    'AlignedCurationChangeSavedDestination.json',
    'ClientMessagingPlatformInteractionEvent.json'
]

# Function to load JSON files into a DataFrame
def load_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return pd.json_normalize(data)

# Load all JSON files
dataframes = {}
for path in file_paths:
    try:
        df = load_json_file(path)
        dataframes[path.split('/')[-1]] = df
        print(f"Loaded {path} successfully with {len(df)} records.")
    except Exception as e:
        print(f"Failed to load {path}: {e}")

# Extract relevant DataFrames
collection_df = dataframes.get('AddedToCollection.json')
rootlist_df = dataframes.get('AddedToRootlist.json')

# Preprocess DataFrames
for df in [collection_df, rootlist_df]:
    if df is not None and 'timestamp_utc' in df.columns:
        df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])

# Combine DataFrames if both are available
if collection_df is not None and rootlist_df is not None:
    combined_df = pd.concat([collection_df, rootlist_df], ignore_index=True)
    print(f"Combined dataset created with {len(combined_df)} records.")
else:
    combined_df = None

# Perform EDA and save combined data
if combined_df is not None:
    # Extract temporal information
    combined_df['month'] = combined_df['timestamp_utc'].dt.month
    combined_df['day_of_week'] = combined_df['timestamp_utc'].dt.day_name()

    # Map months to seasons
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Autumn'

    combined_df['season'] = combined_df['month'].apply(get_season)

    # Categorize by weekend vs weekday
    combined_df['is_weekend'] = combined_df['day_of_week'].isin(['Saturday', 'Sunday'])

    # Categorize by time of day (morning, afternoon, evening, night)
    def get_time_of_day(hour):
        if 5 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 21:
            return 'Evening'
        else:
            return 'Night'

    combined_df['time_of_day'] = combined_df['timestamp_utc'].dt.hour.apply(get_time_of_day)

    # Group by seasons and count song additions
    seasonal_counts = combined_df.groupby('season').size()

    # Group by months for insights
    monthly_counts = combined_df.groupby('month').size()

    # Group by days of the week
    weekday_counts = combined_df.groupby('day_of_week').size()

    # Group by weekend vs weekday
    weekend_counts = combined_df.groupby('is_weekend').size()

    # Group by time of day
    time_of_day_counts = combined_df.groupby('time_of_day').size()

    # Save combined data for further exploration
    combined_df.to_csv('combined_data.csv', index=False)

    # Visualization: Monthly additions
    monthly_counts.plot(kind='bar', figsize=(10, 5), title='Song Additions by Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_by_month.png')
    plt.show()

    # Visualization: Seasonal additions
    seasonal_counts.plot(kind='bar', figsize=(10, 5), title='Song Additions by Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_by_season.png')
    plt.show()

    # Visualization: Day of the week additions
    weekday_counts.plot(kind='bar', figsize=(10, 5), title='Song Additions by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_by_weekday.png')
    plt.show()

    # Visualization: Weekend vs Weekday additions
    weekend_counts.plot(kind='bar', figsize=(10, 5), title='Song Additions: Weekday vs Weekend')
    plt.xlabel('Is Weekend')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_weekend_vs_weekday.png')
    plt.show()

    # Visualization: Song additions by time of day
    time_of_day_counts.plot(kind='bar', figsize=(10, 5), title='Song Additions by Time of Day')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_by_time_of_day.png')
    plt.show()

    # Visualization: Song additions by time of day (hourly)
    combined_df['hour'] = combined_df['timestamp_utc'].dt.hour
    hourly_counts = combined_df.groupby('hour').size()
    hourly_counts.plot(kind='line', figsize=(10, 5), title='Song Additions by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Additions')
    plt.savefig('song_additions_by_hour.png')
    plt.show()

    # Additional Visualization: Cumulative Song Additions Over Time
    combined_df['date'] = combined_df['timestamp_utc'].dt.date
    cumulative_counts = combined_df.groupby('date').size().cumsum()
    cumulative_counts.plot(kind='line', figsize=(10, 5), title='Cumulative Song Additions Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Additions')
    plt.savefig('cumulative_song_additions.png')
    plt.show()

    # Additional Visualization: Heatmap of Additions by Day and Hour
    heatmap_data = combined_df.groupby(['day_of_week', 'hour']).size().unstack(fill_value=0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='Blues', annot=False)
    plt.title('Heatmap of Song Additions by Day and Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Day of the Week')
    plt.savefig('heatmap_song_additions.png')
    plt.show()

    # Additional Visualization: Distribution of Song Popularity (if applicable)
    if 'message_item_uri' in combined_df.columns:
        combined_df['popularity_score'] = combined_df['message_item_uri'].str.extract('(\d+)$').astype(float)
        combined_df['popularity_score'].dropna().plot(kind='hist', bins=20, figsize=(10, 5), title='Distribution of Song Popularity')
        plt.xlabel('Popularity Score')
        plt.ylabel('Frequency')
        plt.savefig('song_popularity_distribution.png')
        plt.show()

    # P-value test for uniform distribution
    observed_counts = monthly_counts
    expected_counts = [observed_counts.sum() / len(observed_counts)] * len(observed_counts)

    # Chi-squared test
    chi2, p_value, _, _ = chi2_contingency([observed_counts, expected_counts])

    print(f"Chi-squared Test Results:\nChi2: {chi2}\nP-value: {p_value}")
