# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
#Reading the CSV file
netflix_data = pd.read_csv("netflix_data.csv")

#Creating new DataFrame containg only movie entries
movie_data = netflix_data[netflix_data["type"] == "Movie"]

#Checking for Missing Values
print(movie_data.isnull().sum())

#Calculating Average Duration by Year
movie_duration_by_year = movie_data.groupby("release_year")["duration"].mean()

#Creating Line Plot
plt.plot(movie_duration_by_year.index, movie_duration_by_year.values)
plt.xlabel("Release Year")
plt.ylabel("Average Movie Duration (minutes)")
plt.title("Trend of Average Movie Length")
plt.show()
