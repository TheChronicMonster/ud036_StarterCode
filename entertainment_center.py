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
					 "http://www.pembinatrails.ca/vincentmassey/pd/photography21G/photoshop/fatma/schew-photoshop%20-%20Unit%208%20Avatar_files/avatar-movie-poster-english1.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

peanuts_movie = media.Movie("The Peanuts Movie", "A story about a dog and his boy",
							"http://www.impawards.com/2015/posters/snoopy_and_charlie_brown_the_peanuts_movie_ver26.jpg",
							"https://www.youtube.com/watch?v=fVR4E6Q6u5g")
# print(peanuts_movie.storyline)
# peanuts_movie.show_trailer()

ex_machina = media.Movie("Ex Machina", "A young coder meets his CEO and participates in a bizarre experiment",
						 "http://a1.mzstatic.com/us/r30/Video3/v4/f3/fb/9b/f3fb9b48-d3b3-be47-3554-aababef6c654/poster600x600.jpeg",
						 "https://www.youtube.com/watch?v=bggUmgeMCdc")

theory_of_everything = media.Movie("The Theory of Everything", "The story of Stephen and Jane Hawking",
									"http://t0.gstatic.com/images?q=tbn:ANd9GcSgW7hpezP5xtikV7WqwwqFm37kqMeJeFEGpYcO30CDcchn9g8m",
									"https://www.youtube.com/watch?v=Salz7uGp72c")

gravity = media.Movie("Gravity", "Astronauts are stranded in space after the mid-orbit destruction of their space shuttle",
						"http://t1.gstatic.com/images?q=tbn:ANd9GcRu6dxMqi3cxDsmH1ajpW3Kr-bKPh2Nf57GXRFW4ybrEgcaUu-C",
						"https://www.youtube.com/watch?v=OiTiKOy59o4")

movies = [toy_story, avatar, peanuts_movie, ex_machina, theory_of_everything,
		gravity]
		
fresh_tomatoes.open_movies_page(movies)
