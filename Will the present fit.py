"""
Santa's elves are boxing presents, and they need your help! Write a function that takes two sequences of dimensions of the present and the box, 
respectively, and returns a Boolean based on whether or not the present will fit in the box provided. The box's walls are one unit thick, 
so be sure to take that in to account.
"""
def will_fit(present, box): 
    if len(present) == len(box):
        for x in range(0, len(box)):
            if sorted(present)[x] >= (sorted(box)[x] - 1): return False
        return True
    else: return False

def run():
    present = [25, 19, 14]
    box = [15, 39, 21]
    print(will_fit(present, box))

if __name__ == "__main__":
    run()