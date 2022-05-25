def find_it(seq):
    if len(seq) == 0: return None
    for x in seq:
        if seq.count(x) % 2 != 0: return x
    return None

def run():
    list = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    print(find_it(list))

if __name__=="__main__":
    run()