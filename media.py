"""media.py defines the Movie class that holds the details of a attributes of the movie."""
import webbrowser

class Movie():

     def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        """Initialises Movie class instance/object variables."""
        self.title = movie_title
        """title: A string that stores the title of the movie"""
        self.storyline = movie_storyline
        """storyline: Stores the theme/plot of the movie."""
        self.poster_image_url = poster_image
        """poster_image_url: Stores the URL of the movie poster."""
        self.trailer_youtube_url = trailer_youtube
        """trailer_youtube_url: Stores the URL of the movie trailer."""
        self.release_date = movie_release_date
        """release_date: Stores the release date of the movie."""

     def show_trailer(self) :
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
