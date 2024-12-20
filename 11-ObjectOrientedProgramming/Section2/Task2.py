# class definition
class Song:
   def __init__(self,Producer,Title,Album,Year_of_release):
      self.Producer = Producer
      self.Title = Title
      self.Album = Album
      self.Year_Of_Release = Year_of_release

   def __str__(self):
      return f'Performer: {self.Producer},\nTitle: {self.Title},\nAlbum: {self.Album},\nYear: {self.Year_Of_Release}'


# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A night at the opera", 1975)

## object usage
print(song1)
print("--------------------------")
print(song2)