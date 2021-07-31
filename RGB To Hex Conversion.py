"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF rgb(255, 255, 300) # returns FFFFFF rgb(0,0,0) # returns 000000 rgb(148, 0, 211) # returns 9400D3
"""

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
