def countSymbols(lists: list) -> int:
    symbols = {
        '#': 5,
        'О': 3,
        'X': 1,
        '!': -1,
        '!!': -3,
        '!!!': -5,
    }

    result = 0

    for list in lists:
        for i in list:
            if symbols.get(i) is not None:
                result += symbols.get(i)

    return result if result > 0 else 0

symbolList = [['#', '#', '!!'],['!!', '#', '#'],['!!', '!!!'],['!!!', 'X', 'X']]

print('\n==========\n')
print('Входной вложенный список:\n')
print(symbolList)
print('\n==========\n')
print('Резултат вычислений:')
print(countSymbols(symbolList))
print('\n==========\n')

