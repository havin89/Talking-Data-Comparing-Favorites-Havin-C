#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Hunger Games: Catching Fire"

print("My favorite movie is " + favMovie)


#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

favMovieBooleanList = movieData["movie_title"] == favMovie

#print(favMovieBooleanList)

favMovieData = movieData. loc[favMovieBooleanList]
print( favMovieData)




print("\n\n")

#Create a new variable to store a new data set with a certain genre
actionMoviesBooleanList = movieData["genres"].str.contains("Action")

actionMovieData = movieData. loc[actionMoviesBooleanList]

numOfMovies = actionMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Action in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = actionMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 89 points higher than the lowest rated movie.")
print()

#find max
max = actionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 9 points lower than the highest rated movie.")
print()

#find mean
mean = actionMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.\n")

#find median
median = actionMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create a histogram
plt.hist(actionMovieData["audience_rating"], range = (0, 100), bins = 20)


#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Action Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, where do you find the most values?\n"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = actionMovieData, x = "audience_rating", y = "critic_rating")


#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, is there a correlation?"
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
