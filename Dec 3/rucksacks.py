with open('input.txt') as f:
    rucksacks = f.readlines()

sum_priority = 0

for rucksack in rucksacks:
    break_flag = False
    first_compartment = rucksack[:len(rucksack)//2]
    print(first_compartment)

    second_compartment = rucksack[len(rucksack)//2:]
    print(second_compartment)

    for x in first_compartment:
        for y in second_compartment:
            if x == y:
                print(x)
                print(y)
                if x.islower():
                    priority = ord(x) - 96
                elif x.isupper():
                    priority = ord(x) - 38

                sum_priority += priority

                break_flag = True
                break
        if (break_flag):
            break

print(sum_priority)
