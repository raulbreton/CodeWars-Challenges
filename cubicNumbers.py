""" 
In a string find the numbers (if they exist)
and see if there are any cubic numbers, if there
are not, return 'Unlucky'. Otherwise return only the
cubic numbers joined with 'Lucky'
"""

def is_sum_of_cubes(s):
    numbers = ""
    summatory = 0
    cubicNumbers = []

    for i in s:
        if not i.isdecimal(): i = " "
        numbers += i

    numbers = numbers.split() #Set list of captured numbers from the string

    for number in numbers:
        summatory = 0
        for digit in number:
            summatory += int(digit)**3
        if int(number) == summatory: cubicNumbers.append(str(summatory))

    if not cubicNumbers: return "Unlucky"
    else: return ','.join(cubicNumbers) + " " + "Lucky"
