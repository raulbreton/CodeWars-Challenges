def rgb(r,g,b):
    hexadecimalR = validation(r)
    hexadecimalG = validation(g)
    hexadecimalB = validation(b)
    return hexadecimalR[2::] + hexadecimalG[2::] + hexadecimalB[2::]

def validation(x):
    if x < 0: hexadecimalX = '0000'
    elif x > 255: hexadecimalX = 'FFFF'
    elif x >= 0 and x <=255:
        hexadecimalX = hex(x)
    return hexadecimalX

def run():
    r = -20
    g = 275
    b = 125
    print(rgb(r,g,b))

if __name__ == "__main__":
    run()