def count_smileys(arr):
    if len(arr) == 0: return 0
    else:
        count = 0
        for x in arr:
            if len(x) == 2:
                if x[0] == ":" or x[0] == ";":
                    if x[1] == ")" or x[1] == "D": count += 1
                    else: pass
                else: pass
            elif len(x) == 3:
                if x[0] == ":" or x[0] == ";":
                    if x[1] == "-" or x[1] == "~":
                        if x[2] == ")" or x[2] == "D": count += 1
                        else: pass
                    else: pass
                else: pass
            else: pass
        return count

def run():
    print(count_smileys([';D', ':-(', ':-)', ';~)']))

if __name__=="__main__":
    run()