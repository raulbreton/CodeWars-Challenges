def filter_list(list):
    result = []
    for x in list:
        if type(x) is int and x < 0: return None
        elif type(x) is int: result.append(x)
    return result

def run():
    list = [1,2,'aasf','1','123',123]
    print(filter_list(list))

if __name__=="__main__":
    run()