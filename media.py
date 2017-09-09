import webbrowser


class Movie():
    """ This class stores  movie related information"""
    def __init__(self, title, storyLine, boxart, trailer):
        """ This function initializes movie title,storyline,box art
            and trailer information"""
        self.title = title
        self.storyline = storyLine
        self.poster_image_url = boxart
        self.trailer_youtube_url = trailer


   
     
