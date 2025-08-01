# Analyze and summarize user viewing history using Pandas filtering, grouping, and sorting.
# Demonstrates: DataFrame creation, filtering, grouping, sorting, and summary statistics

import pandas as pd

# Step 1: Create dummy data as a dictionary
data = {
    "User": ["Abhi", "Abhi", "Sai", "Abhi", "Rhea", "Sai", "Rhea"],
    "Show": ["Dark", "Narcos", "The Office", "Black Mirror", "Stranger Things", "Narcos", "Wednesday"],
    "Genre": ["Sci-Fi", "Crime", "Comedy", "Sci-Fi", "Mystery", "Crime", "Mystery"],
    "Duration": [60, 50, 40, 45, 55, 50, 48]  # Duration in minutes
}

# Step 2: Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Basic view of the DataFrame
print("Netflix Watch History")
print(df.head())  # View top rows
print("\nSummary Info:")
print(df.info())  # DataFrame info (columns, types, etc.)

# Step 4: Filter shows by genre (e.g., Sci-Fi)
sci_fi_shows = df[df["Genre"] == "Sci-Fi"]
print("\nSci-Fi Shows Only:")
print(sci_fi_shows)

# Step 5: Calculate total duration watched by each user
total_by_user = df.groupby("User")["Duration"].sum()
print("\nTotal Watch Time Per User:")
print(total_by_user)

# Step 6: Count number of shows watched per genre
count_by_genre = df.groupby("Genre")["Show"].count()
print("\nShow Count by Genre:")
print(count_by_genre)

# Step 7: Sort shows by longest duration
sorted_shows = df.sort_values(by="Duration", ascending=False)
print("\nShows Sorted by Duration:")
print(sorted_shows)

# Pandas is like Excel on steroids:
# - DataFrame = smart table for data analysis
# - GroupBy = like pivot tables for summarizing
# - Chaining methods = write less, do more
# Perfect for cleaning, analyzing, and slicing real-world data.
