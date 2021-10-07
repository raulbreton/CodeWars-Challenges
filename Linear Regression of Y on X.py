"""
Task:

The function that you have to write accepts two list/array, xxx and yyy, representing the coordinates of the points to regress (so that, for example, the first point has coordinates (x[0], y[0])).

Your function should return a tuple (in Python) or an array (any other language) of two elements: a (intercept) and b (slope) in this order.

You must round your result to the first 4 decimal digits
"""
def regressionLine(x, y):
    x2 = [i**2 for i in x]
    xy = [x[i]*y[i] for i in range(0, len(x))]
    
    a = ((len(x) * sum(xy)) - (sum(x) * sum(y))) / ((len(x) * sum(x2)) - (sum(x)**2))
    b = (sum(y) - (a * sum(x))) / len(x)
    result = (round(b,4),round(a,4))
    return result

def run():
    x = [25,30,35,40,45,50]
    y = [78,70,65,58,48,42]
    print(regressionLine(x,y))

if __name__=="__main__":
    run()