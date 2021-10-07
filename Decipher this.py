"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

Note: there are no special characters used, only letters and spaces
"""
def decipher_this(string):
    result = []
    for word in string.split():
        newString = ""
        s = [x for x in word if x.isalpha()]
        code = [x for x in word if x.isdigit()]
        code = chr(int(''.join(code)))
        if len(s) > 1: newString += code + s[len(s)-1] + ''.join(s)[1:len(s)-1] + s[0]
        else: newString += code + ''.join(s)
        result.append(newString)
    return ' '.join(result)

def run():
    string = '98e'
    print(decipher_this(string))

if __name__=="__main__":
    run()