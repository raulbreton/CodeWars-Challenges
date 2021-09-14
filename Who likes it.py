"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
"""
def likes(names):
    if len(names) == 0: return "no one likes this"
    elif len(names) == 1: return "{} likes this".format(*names)
    elif len(names) == 2: return "{} and {} like this".format(*names)
    elif len(names) == 3: return "{}, {} and {} like this".format(*names)
    elif len(names) > 3: return "{}, {} and ".format(*names) + str(len(names)-2) + " others like this"

def run():
    names = ["Alex", "Jacob", "Mark", "Max", "Mark", "Max"]
    print(likes(names))

if __name__ == "__main__":
    run()