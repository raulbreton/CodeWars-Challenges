def isbn_converter(isbn):
    result = "978-" + isbn[:len(isbn)-1]
    digits = result.replace("-", "")
    cont=0
    list = []
    for x in digits:
        if cont%2 == 0: 
            list.append(int(x)*1)
            cont += 1
        else: 
            list.append(int(x)*3)
            cont += 1
    if sum(list) % 10 == 0:
        result += str(sum(list) % 10)
        return result
    else: 
        result += str(10 - (sum(list) % 10))
        return result

def run():
    print(isbn_converter("1-85326-158-0"))

if __name__=="__main__":
    run()