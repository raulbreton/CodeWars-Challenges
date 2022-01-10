def create_phone_number(n):
    if max(n) >= 10: return None
    else:
        numbers = (' '.join(str(x) for x in n)).replace(' ', '')
        return "(" + numbers[0:3] + ") " + numbers[3:6] + "-" + numbers[6:]

def run():
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

if __name__=="__main__":
    run()