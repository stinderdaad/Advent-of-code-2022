with open('input.txt') as f:
    lines = f.readlines()

points = 0

for x in lines:
    opponent = x[0]
    result = x[2]

    match result:
        case 'X': #lose
            #no points
            if opponent == 'A': #chose rock
                points += 3 #choosing scissor
            elif opponent == 'B': #chose paper
                points += 1 #choosing rock
            elif opponent == 'C': #chose scissor
                points += 2 #choosing paper
        case 'Y': #draw
            points += 3
            if opponent == 'A': #chose rock
                points += 1 #choosing rock
            elif opponent == 'B': #chose paper
                points += 2 #choosing paper
            elif opponent == 'C': #chose scissor
                points += 3 #choosing scissor
        case 'Z': #win
            points += 6
            if opponent == 'A': #chose rock
                points += 2 #choosing paper
            elif opponent == 'B': #chose paper
                points += 3 #choosing scissor
            elif opponent == 'C': #chose scissor
                points += 1 #choosing rock

print(points)
