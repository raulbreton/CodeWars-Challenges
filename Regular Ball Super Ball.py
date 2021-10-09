"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""
class Ball():
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

def run():
    ball1 = Ball()
    ball2 = Ball("super")
    print(ball1.ball_type)  #=> "regular"
    print(ball2.ball_type)  #=> "super"


if __name__ == "__main__":
    run()