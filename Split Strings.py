"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').
"""
def solution(s):
    string = s
    cont = 0
    cont2 = 2
    result = []
    if len(string) % 2 != 0: string += "_"
    while(cont != len(string)):
        result.append(string[cont:cont2])
        cont += 2
        cont2 += 2
    return result

def run():
    string = "abcde"
    print(solution(string))

if __name__ == "__main__":
    run()