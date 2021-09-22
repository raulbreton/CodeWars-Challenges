"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
"""
def count_positives_sum_negatives(arr):
    if not arr: return []
    positive_num = [x for x in arr if x > 0]
    negative_num = [x for x in arr if x < 0]
    result = [len(positive_num), sum(negative_num)]
    return result

def run():
    array = [0,0]
    #array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    print(count_positives_sum_negatives(array))
    
if __name__ == "__main__":
    run()