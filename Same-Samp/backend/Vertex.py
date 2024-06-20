class Vertex:
  def __init__(self, artist, name, genre, instrument, year, popularity, duration, explicit, avail_marks, playCount, grossRev, age, annualRev):
    self.name = artist + " - " + name
    self.artist = artist
    self.genre = genre
    self.instrument = instrument
    self.popularity = popularity
    self.duration = duration / 1000
    self.explicit = explicit
    self.avail_marks = avail_marks
    self.age = age
    self.playCount = playCount
    self.grossRev = grossRev
    self.annualRev = annualRev
    
  def getName(self):
    return self.name
  def getArtist(self):
    return self.artist
  def getExplicit(self):
    return self.explicit
  def getGenre(self):
    return self.genre
  def getInstrument(self):
    return self.instrument