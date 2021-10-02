"""
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation. 
"""
def what_century(year):
    if len(str(year)) == 2: 
        if year > 9 and year < 20: numberSuffix = {0:'th', 1:'th', 2:'th', 3:'th', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th'}
        else: numberSuffix = {0:'th', 1:'st', 2:'nd', 3:'rd', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th'}
        return str(year) + numberSuffix[int(str(year)[1])]
    elif len(str(year)) == 4:
        if int(str(year)[:2]) > 9 and int(str(year)[:2]) < 20: numberSuffix = {0:'th', 1:'th', 2:'th', 3:'th', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th'}
        else: numberSuffix = {0:'th', 1:'st', 2:'nd', 3:'rd', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th'}
        if str(year)[3] != '0' or str(year)[2:] != '00': return str(int(str(year)[:2]) + 1) + numberSuffix[int(str(int(str(year)[:2]) + 1)[1])]
        else: return str(year)[:2] + numberSuffix[int(str(year)[1])]
    else: return None

def run():
    century = 22
    print(what_century(century))

if __name__ == "__main__":
    run()