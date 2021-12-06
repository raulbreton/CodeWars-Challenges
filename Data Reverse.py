def data_reverse(data):
    result = []
    firstIndex = len(data)-8
    lastIndex = len(data)
    while firstIndex >= 0:
        result += data[firstIndex:lastIndex]
        firstIndex -= 8
        lastIndex -= 8
    return result

def run():
    print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))

if __name__=="__main__":
    run()