
class Movie():
	""" Representation of a movie, designed be used with movie_trailer.py """

	def __init__(self, movie_name, movie_poster_image_url, movie_trailer_url):
		""" Contructor with the arguments required to use movie_trailer.py """
		# Ensure instance variable names are consistent with movie_trailer.py
		self.title = movie_name
		self.poster_image_url = movie_poster_image_url
		self.trailer_youtube_url = movie_trailer_url

