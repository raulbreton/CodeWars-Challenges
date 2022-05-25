def find_it(seq):
    result = []
    for x in seq:
        if x not in result and seq.count(x) % 2 != 0: result.append(x)
    print(result)

def run():
    list = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    print(find_it(list))

if __name__=="__main__":
    run()