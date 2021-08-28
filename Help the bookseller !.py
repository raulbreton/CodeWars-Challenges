def stock_list(L, M):
    if L and M: #If both parameters are not empty
        bookDict = {}
        result = ""
        elementPos = 0
        #Set categories with the sum of books of each letter
        for categorie in L:
            num = ""
            for char in categorie:
                if char.isdecimal():
                    num += char
            if not bookDict.get(categorie[0]): #If the categorie does not already exist in our dictionary
                dictData = {categorie[0]:int(num)}
                bookDict.update(dictData)
            else:
                num = int(num) + bookDict.get(categorie[0])
                bookDict[categorie[0]] = num
        #Set the string result
        for element in M:
            elementPos += 1
            if not bookDict.get(element): #If the category does not exist print a 0 instead of None
                result += '(' + element + " : " + '0' + ')'
            else: 
                result += '(' + element + " : " + str(bookDict.get(element)) + ')'
            if elementPos < len(M): result += " - "

        return result

    else:
        return ""

def run():
    a = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    b = ["A", "B" , "C", "W"]
    print(stock_list(a, b))

if __name__=="__main__":
    run()