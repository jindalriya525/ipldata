import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ipl.csv")

# Display the first few rows to understand the data
print("Players' rows of the dataset:")
print(df.head())

# Basic Data Summary
print("\nDataset Information:")
print(df.info())

print("\nStatistical Overview:")
print(df.describe())

# ----- Data Analysis -----

# 1. Explore Team Performance over Seasons
print("\nTeam Wins per Season:")
if "season" in df.columns and "winner" in df.columns:
    team_wins_per_season = df.groupby(['season', 'winner']).size().unstack(fill_value=0)
    print(team_wins_per_season)

    team_wins_per_season.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Team Performance Over Seasons')
    plt.xlabel('Season')
    plt.ylabel('Number of Wins')
    plt.legend(loc='upper right')
    plt.show()
else:
    print("Season and winner columns not found in the dataset.")

# 2. Analyze All Players Batting Statistics
print("\nAll Players Run Statistics:")
if "player_name" in df.columns and "runs_scored" in df.columns:
    player_runs = df.groupby("player_name")["runs_scored"].sum().sort_values(ascending=False)
    print(player_runs)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_runs.values, y=player_runs.index, color='blue')
    plt.title('All Players by Runs Scored')
    plt.xlabel('Total Runs')
    plt.show()
else:
    print("Player name or runs scored column not found.")

# 3. Boundaries for All Players
if "player_name" in df.columns and "4s" in df.columns and "6s" in df.columns:
    df["total_boundaries"] = df["4s"] + df["6s"]
    player_boundaries = df.groupby("player_name")["total_boundaries"].sum().sort_values(ascending=False)
    print("\nPlayer Boundaries Data:")
    print(player_boundaries)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_boundaries.values, y=player_boundaries.index, color='purple')
    plt.title('All Players by Boundaries (4s + 6s)')
    plt.xlabel('Total Boundaries')
    plt.show()
else:
    print("Player name or boundary columns not found.")

# 4. Analyze Bowling Performance for All Players
print("\nBowling Performance (Wickets and Averages):")
if "player_name" in df.columns and "wickets_taken" in df.columns and "bowling_average" in df.columns:
    player_bowling = df.groupby("player_name")[["wickets_taken", "bowling_average"]].sum().sort_values(by="wickets_taken", ascending=False)
    print(player_bowling)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_bowling["wickets_taken"], y=player_bowling.index, color='green')
    plt.title('All Players by Wickets Taken')
    plt.xlabel('Total Wickets')
    plt.show()

    # Plotting Bowling Averages
    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_bowling["bowling_average"], y=player_bowling.index, color='orange')
    plt.title('All Players by Bowling Average')
    plt.xlabel('Bowling Average')
    plt.show()
else:
    print("Player name, wickets taken, or bowling average columns not found.")

# 5. Player of the Match Analysis
if "player_name" in df.columns and "player_of_match_awards" in df.columns:
    player_awards = df.groupby("player_name")["player_of_match_awards"].sum().sort_values(ascending=False)
    print("\nPlayer of the Match Awards:")
    print(player_awards)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_awards.values, y=player_awards.index, color='orange')
    plt.title('All Players by Player of the Match Awards')
    plt.xlabel('Number of Awards')
    plt.show()
else:
    print("Player name or player of match awards column not found.")

# 6. Strike Rate Analysis
if "player_name" in df.columns and "strike_rate" in df.columns:
    player_strike_rates = df.groupby("player_name")["strike_rate"].mean().sort_values(ascending=False)
    print("\nPlayer Strike Rates:")
    print(player_strike_rates)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=player_strike_rates.values, y=player_strike_rates.index, color='red')
    plt.title('All Players by Strike Rate')
    plt.xlabel('Strike Rate')
    plt.show()
else:
    print("Player name or strike rate column not found.")

print("Analysis complete.")
