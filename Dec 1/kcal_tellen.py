with open('input.txt') as f:
    lines = f.readlines()

newline  = lines[14]
kcal = 0
elfs = []

for x in lines:
    if x == newline:
        elfs.append(kcal)
        kcal = 0
    else:
        kcal = kcal + int(x)

elfs.sort(reverse=True)

print(elfs[0] + elfs[1] + elfs[2])
