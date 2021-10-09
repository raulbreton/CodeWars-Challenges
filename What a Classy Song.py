"""
Your job is to create a class called Song.

A new Song will take two parameters, title and artist.

You will also have to create an instance method named howMany() (or how_many()).
The method takes an array of people who have listened to the song that day. 
The output should be how many new listeners the song gained on that day out of all listeners. 
Names should be treated in a case-insensitive manner, i.e. "John" is the same as "john".
"""
class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, array):
        newListeners = []

        for i in array:
            if self.listeners.count(i.lower()) == 0:
                newListeners.append(i.lower())
                self.listeners.append(i.lower())

        return len(newListeners)

def run():
    mount_moose = Song('Mount Moose', 'The Snazzy Moose')

    print(mount_moose.title)
    print(mount_moose.artist)
    print(mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']))
    print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))
    
if __name__=="__main__":
    run()