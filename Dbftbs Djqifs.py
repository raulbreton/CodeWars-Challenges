"""
Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
"""
def encryptor(key, message):
    if key >= 0: return positiveNum(key, message)
    else: return negativeNum(key, message)

def positiveNum(key, message):
    plainAlphabet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 
    11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 
    21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    plainAlphabet2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 
    'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    cipherDict = {}
    result = ""

    if key > len(plainAlphabet):
        cipherKey = key / len(plainAlphabet)
        cipherKey = len(plainAlphabet) * int(cipherKey)
        cipherKey = key - cipherKey
        key = cipherKey

    for x in range(0,len(plainAlphabet)):
        cipherKey = x + key
        if cipherKey >= len(plainAlphabet):
            cipherKey = cipherKey - len(plainAlphabet)
            dictValue = {x:plainAlphabet.get(cipherKey)}
            cipherDict.update(dictValue)
        else:
            dictValue = {x:plainAlphabet.get(cipherKey)}
            cipherDict.update(dictValue)
    
    for x in message:
        if x.islower(): result += cipherDict.get(plainAlphabet2.get(x))
        elif x.isupper(): result += (cipherDict.get(plainAlphabet2.get(x.lower()))).upper()
        else: result += x
        
    return result

def negativeNum(key, message):
    plainAlphabet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 
    11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 
    21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    plainAlphabet2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 
    'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    cipherDict = {}
    result = ""
    
    if key < (len(plainAlphabet)) * -1:
        cipherKey = key / len(plainAlphabet)
        cipherKey = len(plainAlphabet) * int(cipherKey)
        cipherKey = key - cipherKey
        key = cipherKey

    for x in range(0, len(plainAlphabet)):
        cipherKey = x + key
        if cipherKey < 0:
            cipherKey = cipherKey + len(plainAlphabet)
            dictValue = {x:plainAlphabet.get(cipherKey)}
            cipherDict.update(dictValue)
        else: 
            dictValue = {x:plainAlphabet.get(cipherKey)}
            cipherDict.update(dictValue)
            
    for x in message:
        if x.islower(): result += cipherDict.get(plainAlphabet2.get(x))
        elif x.isupper(): result += (cipherDict.get(plainAlphabet2.get(x.lower()))).upper()
        else: result += x
        
    return result

def run():
    message = 'Hello World!'
    key = -5
    print(encryptor(key, message))

if __name__ == "__main__":
    run()