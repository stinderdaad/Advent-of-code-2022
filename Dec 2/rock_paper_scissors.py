with open('input.txt') as f:
    lines = f.readlines()

points = 0

for x in lines:
    opponent = x[0]
    myMove = x[2]

    match myMove:
        case 'X': #rock
            points += 1
            if opponent == 'C': #beats scissor
                points += 6
            elif opponent == 'A': #mirror match
                points += 3
        case 'Y': #paper
            points += 2
            if opponent == 'A': #beats rock
                points += 6
            elif opponent == 'B': #mirror match
                points += 3
        case 'Z': #scissor
            points += 3
            if opponent == 'B': #beats paper
                points += 6
            elif opponent == 'C': #mirror match
                points += 3

print(points)
