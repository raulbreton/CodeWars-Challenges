"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(array):
    zeroes = array.count(0)
    for x in range(0,zeroes): 
        array.remove(0)
        array.append(0)
    return array
    

def run():
    array = [1, 0, 1, 2, 0, 1, 3]
    print(move_zeros(array))

if __name__=="__main__":
    run()