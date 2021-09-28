"""
Acknowledgments:

I thank yvonne-liu for the idea and for the example tests :)
Description:

Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter must be converted to its ASCII code.
        The second letter must be switched with the last letter
    Keepin' it simple: There are no special characters in the input.

"""
def encrypt_this(text):
    result =[]
    for x in text.split():
        if len(x) == 1: result.append(str(ord(x[:1])))
        elif len(x) == 2:
            s = str(ord(x[:1]))
            s += x[1:2]
            result.append(s)
        else:
            s = str(ord(x[:1]))
            s += x[len(x)-1]
            s += x[2:len(x)-1]
            s += x[1:2]
            result.append(s)

    return ' '.join(result)

def run():
    text = 'The more he saw the less he spoke'
    print(encrypt_this(text))

if __name__ == "__main__":
    run()