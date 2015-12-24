class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics # self refers to one instance (the current one)
        Song.screwyou = 'Screw you' # this will be in all instances of the class.
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


class Song_with_genre(Song):
    def __init__(self, lyrics, genre):
        Song.__init__(self, lyrics)
        self.genre = genre



happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                    "so I'll stop right there"])

bulls_on_parade = Song(["They rally around",
                        "With pockets like sounds"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()



class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self): # __str__ is what comes out in a print call
        return "%s is a %s" % (self.name, self.species) 

polly = Pet("Polly","Parrot")
Pet.getName(polly)
polly.getName() # same output as line above


class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


bob = Cat('bob',True)
isinstance(bob, Pet) # True
isinstance(bob, Cat) # True





