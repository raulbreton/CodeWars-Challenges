"""
You will have a list of rationals in the form

lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]

where all numbers are positive integers. You have to produce their sum N / D in an irreducible form: this means that N and D have only 1 as a common divisor.

Return the result in the form:

    [N, D] in Ruby, Crystal, Python, Clojure, JS, CS, PHP, Julia, Pascal

If the result is an integer (D evenly divides N) return:

    an integer in Ruby, Crystal, Elixir, Clojure, Python, JS, CS, PHP, R, Julia

If the input list is empty, return

    nil/None/null/Nothing

Example:

[ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]
1/2  +  1/3  +  1/4     =      13/12
"""
def sum_fracts(list):
    from fractions import Fraction

    if list:
        summatory = 0
        
        for element in list:
            #summatory += element[0] / element[1]
            summatory += Fraction(element[0], element[1])

        if float(summatory).is_integer(): return int(summatory)
        
        else:
            Tuple = str(summatory).partition('/')
            Tuple = [int(x) for x in Tuple if x != '/']
            return Tuple
            
    else: return None

def run():
    list = [ [1, 3], [5, 3] ]
    print(sum_fracts(list))

if __name__ == "__main__":
    run()
