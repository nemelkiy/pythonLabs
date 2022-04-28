def isVisible(list: list) -> bool:
    i = 0
    while i < len(list):
        k = 0
        if i == len(list) - 1:
            break
        for item in list[i]:
            if item > list[i + 1][k]:
                return False
            k += 1
        i += 1
    return True

print('\n==========\n')
print(isVisible([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]))
print('\n==========\n')
print(isVisible([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 10, 4, 4], [6, 6, 7, 6, 5, 5]]))
print('\n==========\n')