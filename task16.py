def stairMaker(floor: int) -> str:
    countStairs = abs(floor)
    i = 0
    string = ''
    while i < countStairs:
        if floor > 0:
            string += +i * '_' + '\n' + (countStairs - i) * '#' 
        elif floor < 0:
            string += i * '_' + (countStairs - i) * '#' + '\n'
        i += 1
    return string[::-1]


print(stairMaker(25))
print(stairMaker(-15))
