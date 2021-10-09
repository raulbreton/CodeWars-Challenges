"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""
def number(lines):
    return [str(key + 1) + ': ' + lines[key] for key in range(0, len(lines))]

def run():
    input = ["a", "b", "c"]
    print(number(input))

if __name__=="__main__":
    run()