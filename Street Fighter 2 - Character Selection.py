def street_fighter_selection(fighters, initial_position, moves):
    verticalCount = 0
    horizontalCount = 0
    result = []

    for x in moves:
        if x == 'up': 
            verticalCount = 0
            result.append(fighters[verticalCount][horizontalCount])
        elif x == 'down': 
            verticalCount = 1
            result.append(fighters[verticalCount][horizontalCount])
        elif x == 'right':
            if horizontalCount == 5: horizontalCount = 0
            else: horizontalCount += 1
        elif x == 'left':
            if horizontalCount == 0: horizontalCount = 5
            else: horizontalCount -= 1
        print(verticalCount, horizontalCount)

    return result

def run():
    fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]
    initial_position = (0,0)
    moves = ['up', 'left', 'right', 'left', 'left']
    print(street_fighter_selection(fighters, initial_position, moves))

if __name__ == "__main__":
    run()