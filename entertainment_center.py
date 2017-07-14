""" details of movies are stored here and further displayed on a website."""
import media
import fresh_tomatoes

"""this import media will tell the compiler to load contents of the previous python file"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "November 19,1995")


"""media is name of previous python file
 Movies is class defined inside it.
 if we don't pass any arguments inside media.Movie it will throw error
 because when we try to create toy_story init function is called which is looking
 for several arguments/information .
 self is added by default in python."""


#print (toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "December 18, 2009")
#print(avatar.storyline)
#avatar.show_trailer()
the_shaw_redem = media.Movie("The Shawshank Redemption",
                          "A banker is sentenced to life in jail for murdering his wife",
                          "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                          "https://www.youtube.com/watch?v=NmzuHjWmXOc",
                          "September 23, 1994")
spectre = media.Movie("Spectre",
                          "James Bond movie",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                          "https://www.youtube.com/watch?v=vBnGxAkdh_k",
                          "October 26, 2015")

the_dark_knight = media.Movie("The Dark Knight",
                          "The Dark Knight fights against joker",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "July 18, 2008")

harry_potter_4 = media.Movie("Harry Potter and the Goblet of Fire",
                           "Young boy competes in the Triwizard Tournament",
                           "https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                           "https://www.youtube.com/watch?v=PFWAOnvMd1Q",
                           "NOvember 6, 2005")

matrix = media.Movie  ("The Matrix",
                           "The world is a simulation",
                           "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                           "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                           "March 31, 1999")

cars = media.Movie    ("Cars",
                           "A Race car finds meaning of true frienship",
                           "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
                           "https://www.youtube.com/watch?v=SbXIj2T-_uk",
                           "June 9, 2006")


school_of_rock = media.Movie("school of rock",
                             "using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "September 24, 2003")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "June 28, 2007")


bahubali_The_Beginning = media.Movie("Bahubali",
                       "Son takes avenge of his father's death",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Baahubali_poster.jpg/220px-Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI",
                       "July 10,2015")

Hunger_games= media.Movie("Hunger Games",
                          "A really real reality show",
                          "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                          "https://www.youtube.com/watch?v=mfmrPu43DF8",
                          "March 23, 2012")


# Store the Movie objects in a list.
movies = [toy_story, avatar, the_shaw_redem, spectre, the_dark_knight, harry_potter_4,
          matrix, cars, school_of_rock, ratatouille, bahubali_The_Beginning,
          Hunger_games]


# Open the movie website in the user's browser, featuring the movies above
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
                       
