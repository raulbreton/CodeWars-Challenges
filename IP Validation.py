"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets,with values between 0 and 255, inclusive.
"""
def is_valid_IP(strng):
    if len(strng) == 0 or strng.count('.') != 3 or strng.replace('.','').isdigit() == False: return False
    else:
        numbers = strng.split('.')
        for num in numbers: 
            if len(num) == 3 and num[0] == '0': return False
            elif len(num) == 2 and num[0] == '0': return False
            else:
                if int(num) > 255 or int(num) < 0: return False
        return True

def run():
    ip = '123.145.007.289'
    print(is_valid_IP(ip))

if __name__ == "__main__":
    run()