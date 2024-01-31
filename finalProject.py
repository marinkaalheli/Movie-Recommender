'''
author: marinka peralta
date: may 2023
function: a program that recommends a movie based on user input
'''

import csv
import random

def allMovies():
    '''
    INPUT: csv data file of movies and accompanying data
    OUTPUT: list
    FUNCTION: read the csv data file using open within a with-statement, uses csv.DictReader, docstrings
    '''
    with open('data.csv') as csvFile:
        csvReader = csv.DictReader(csvFile)
        everyMovie = list(csvReader)
    return everyMovie

userName = ""
movieYears = []
def introAndYears(allMovies):
    '''
    INPUT: theoretically takes in the list created from allMovies function
    OUTPUT: list of movies within the range of years that the user prefers or all years if no preference
    FUNCTION: uses conditionals and nested loops and input and runs to completion even if user types '1', docstrings
    '''
    userName = input("Welcome! I'm here to help you pick a movie to watch tonight:) What's your name? ")
    yearsPreference = input("Hi " + userName + "! Do you have a preference for a range of years of release dates you would like to watch? (y/n) ").lower()
    
    if yearsPreference == 'y':
        lowerBound = input("Pick a year between 1903 and 2023 (lower bound): ")
        upperBound = input("Pick a year between 1903 and 2023 (upper bound): ")
        if lowerBound > upperBound:
            intermediate = lowerBound
            lowerBound = upperBound
            upperBound = intermediate
        for movie in allMovies:
            movieReleased = movie['date_x']
            movieRelYr = int(movieReleased.split('/')[2].strip())
            if int(lowerBound) <= movieRelYr <= int(upperBound):
                movieYears.append(movie)      
    else:
        print("okay! ")
        for movie in allMovies:
            movieYears.append(movie)
    return movieYears
        
genresList = []
genreAndYrMovies = []
def listOfGenres(inputYrs):
    '''
    INPUT: list of the movies from the range of years from function introAndYears
    OUTPUT: the final movie decision
    FUNCTION: uses conditionals and nested loops and runs to completion if user types '1', docstrings
    '''
    for movie in inputYrs:
        genres = movie['genre'].split(',')
        for genre in genres:
            genre = genre.strip()
            if genre not in genresList:
                genresList.append(genre)

    randomGenresList = random.sample(genresList, min(len(genresList),5))
    print(randomGenresList)
    genrePreference = input("Now please pick a genre from the above list: ").lower()
    userGenre = genrePreference.capitalize()

    if userGenre not in genresList:
        print("That's not a given genre but that's okay! We'll randomly pick a genre for you! ")
        userGenre = random.choice(randomGenresList)
    
    for movi in inputYrs:
        if userGenre in movi['genre']:
            genreAndYrMovies.append(movi)
    return random.choice(genreAndYrMovies)
  
      
      
finalMovie = listOfGenres(introAndYears(allMovies()))
print("Okay perfect, " + userName + " here is a recommendation for you to check out! " + finalMovie['names'] + ", this movie was released on " + finalMovie['date_x'] + "and here is a summary: " + finalMovie['overview'])

    