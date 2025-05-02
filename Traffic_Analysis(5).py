# Install plotly if not already installed
# !pip install plotly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

df = pd.read_csv(url)

# Display basic info
print("Initial Data Preview:")
print(df[['Start_Time', 'Severity', 'Weather_Condition', 'State']].head())

# ---------------------------------------
# 2. Preprocessing
# ---------------------------------------
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['Day'] = df['Start_Time'].dt.day_name()

# Drop rows with missing values in key columns
df = df[['Start_Time', 'Severity', 'Weather_Condition', 'Hour', 'Day', 'State', 'Start_Lat', 'Start_Lng']].dropna()

# ---------------------------------------
# 3. Time-based Visualizations
# ---------------------------------------

# Accidents by Hour
plt.figure(figsize=(10, 4))
sns.countplot(x='Hour', data=df, palette='magma')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

# Accidents by Day
plt.figure(figsize=(8, 4))
sns.countplot(x='Day', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title("Accidents by Day of the Week")
plt.xticks(rotation=45)
plt.ylabel("Number of Accidents")
plt.show()

# ---------------------------------------
# 4. Weather Condition Patterns
# ---------------------------------------

top_weather = df['Weather_Condition'].value_counts().head(10)

plt.figure(figsize=(10, 4))
sns.barplot(x=top_weather.index, y=top_weather.values, palette='Blues_r')
plt.title("Top 10 Weather Conditions During Accidents")
plt.xticks(rotation=45)
plt.ylabel("Number of Accidents")
plt.show()

# ---------------------------------------
# 5. Map Visualization: Accident Hotspots
# ---------------------------------------

# Sample to speed up plotting
df_sample = df.sample(1000)

fig = px.scatter_mapbox(df_sample,
                        lat="Start_Lat",
                        lon="Start_Lng",
                        color="Severity",
                        hover_data=["State", "Weather_Condition"],
                        mapbox_style="carto-positron",
                        zoom=3,
                        height=500,
                        title="Accident Hotspots in the US (Sample)")
fig.show()

# ---------------------------------------
# 6. Optional: Save Processed Data
# ---------------------------------------
# df.to_csv("processed_accidents.csv", index=False)