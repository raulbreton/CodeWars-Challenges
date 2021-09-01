def unique_in_order(sequence):
    list = []
    i = -1
    for digit in sequence: 
        if not list: 
            list.append(digit)
            i += 1
        else:
            if digit != list[i]:
                list.append(digit)
                i += 1

    return list

def run():
    sequence = "AAAABBBCCDAABBB"
    print(unique_in_order(sequence))
if __name__=="__main__":
    run()