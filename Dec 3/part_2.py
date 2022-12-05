with open('input.txt') as f:
    rucksacks = f.readlines()

sum_priority = 0
n = 0

while ((n + 2) <= len(rucksacks)):
    print(n)
    print(len(rucksacks))
    first_elf = rucksacks[n]
    second_elf = rucksacks[n + 1]
    third_elf = rucksacks[n + 2]
    break_flag = False

    for x in first_elf:
        for y in second_elf:
            for z in third_elf:
                if x == y and y == z:
                    if x.islower():
                        priority = ord(x) - 96
                    elif x.isupper():
                        priority = ord(x) - 38

                    sum_priority += priority

                    n += 3
                    break_flag = True
                    break
            if (break_flag):
                break
        if (break_flag):
            break

print(sum_priority)
