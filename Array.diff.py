"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
"""
def array_diff(a, b):
    result = [x for x in a if b.count(x) == 0]
    return result

def run():
    arr01 = [1,2,2,2,3]
    arr02 = [2]
    print(array_diff(arr01,arr02))

if __name__ == "__main__":
    run()