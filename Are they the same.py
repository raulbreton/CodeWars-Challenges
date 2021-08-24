def comp(array1, array2):
    if array1 == None or array2 == None or len(array1) != len(array2): return False
    else:
        arr1 = [abs(num) for num in array1]
        arr1.sort()
        arr2 = [abs(num) for num in array2]
        arr2.sort()
        print(arr1, arr2)
        pos = -1

        for number in arr1:
            pos += 1
            if (number * number) != arr2[pos]: return False
        return True

def run():
    array1 = [-121, -144, 19, -161, 19, -144, 19, -11]
    array2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(array1, array2))

if __name__ == "__main__":
    run()