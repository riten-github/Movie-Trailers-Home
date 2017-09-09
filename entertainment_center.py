import media
import movie_trailer

toyStory=media.Movie("ToyStory","A story of a boy and toy that comes to life",
                     "https://animationfascination.files.wordpress.com/2013/11/toy_story.jpg?w=584&h=328",
                     "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar=media.Movie("Avatar" , "A marine in a alien planet" ,
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" ,
                    "https://www.youtube.com/watch?v=oJJazzx5bO0")

planet_apes=media.Movie("War for the planet of Apes " , " A story of confrontation between the apes, led by Caesar, and the humans for control of                         Earth" ,
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS9sq8YtZzeOrmpVcNOF_A2BVvs-kNX4CDFf8lJYrS-CEGnvblsA" ,
                        "https://www.youtube.com/watch?v=X5lWpxvrd-I")

frozen=media.Movie("Frozen","A story of a fearless princess who sets off on a journey alongside a rugged iceman, his loyal pet reindeer, and a                      naive snowman to find her estranged sister, whose icy powers have inadvertently trapped the kingdom in eternal winter.",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_(2013_film)_poster.jpg/220px-Frozen_(2013_film)_poster.jpg",
                   "https://www.youtube.com/watch?v=TbQm5doF_Uc")

lionKing=media.Movie("The Lion King" , " A story of Simba, a young lion who is to succeed his father, Mufasa, as King of the Pride Lands;" ,
                    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg" ,
                    "https://www.youtube.com/watch?v=4sj1MT05lAA")

jungleBook=media.Movie("The Jungle Book" , " A story of Mowgli, an orphaned human boy who, guided by his animal guardians, sets out on a journey of self-discovery while evading the threatening Shere Khan" ,
                    "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_(2016).jpg" ,
                    "https://www.youtube.com/watch?v=C4qgAaxB_pc")

movies=[toyStory,avatar,planet_apes,frozen,lionKing,jungleBook]
print "########################################################"
print "            Application Launched intiated                       "
print "########################################################"
movie_trailer.open_movies_page(movies)
