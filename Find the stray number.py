"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)
"""
def stray(arr):
    result = next((x for x in arr if arr.count(x)==1),None)
    return result

def run():
    array = [17, 17, 3, 17, 17, 17, 17]
    print(stray(array))

if __name__=="__main__":
    run()