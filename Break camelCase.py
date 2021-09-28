"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""
def solution(s):
    if not s: return ""
    elif s.islower(): return s
    result = ""
    for x in s:
        if x.isupper(): result += " " + x
        else: result += x
    return result

def run():
    string = "camelCassing"
    print(solution(string))

if __name__ == "__main__":
    run()