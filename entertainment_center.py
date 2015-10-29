# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

# media is name of media.py file, Movie is name of class in media file
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
						 "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						 "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

peanuts_movie = media.Movie("The Peanuts Movie", "A story about a dog and his boy",
							"https://en.wikipedia.org/wiki/The_Peanuts_Movie#/media/File:Peanuts_2015.jpg",
							"https://www.youtube.com/watch?v=fVR4E6Q6u5g")
# print(peanuts_movie.storyline)
# peanuts_movie.show_trailer()

movies = [toy_story, avatar, peanuts_movie]
fresh_tomatoes.open_movies_page(movies)