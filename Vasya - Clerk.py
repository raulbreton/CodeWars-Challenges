"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
"""

def tickets(people):
    y = 'YES'
    n = "NO"
    cash = []

    for payment in  people:
        if payment == 25: cash.append(25)
        elif payment == 50:
            if cash.count(25) > 0:
                cash.remove(25)
                cash.append(50)
            else: return n
        elif payment == 100:
            if cash.count(50) > 0 and cash.count(25) > 0:
                cash.remove(25)
                cash.remove(50)
                cash.append(100)
            elif cash.count(50) == 0 and cash.count(25) >= 3:
                cash.remove(25)
                cash.remove(25)
                cash.remove(25)
                cash.append(100)
            else: return n
    return y

def run():
    people = [25,50,25,100,25,25,50,100,25,50,25,100,50,25]
    print(tickets(people))

if __name__=="__main__":
    run()