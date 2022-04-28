def reCode(symbols):
    if isinstance(symbols, str):
        result = []
        i = 0
        for letter in symbols:
            code = ord(letter)
            if i == 0:
                result.append(code)
            else:
                codePrev = ord(symbols[i-1])
                result.append(code - codePrev)
            i += 1
    elif isinstance(symbols, list):
        result = ''
        i = 0
        for el in symbols:
            if i == 0:
                let = chr(el)
                result += let
            else:
                prev = ord(result[i-1])
                code = prev + symbols[i]
                result += chr(code)
            i += 1
    return result
    
print('\n==========\n')
print('Введите строку или лист:\n')
inputVal = input()

print('\n==========\n')
print('Вы ввели:\n')
print(inputVal)
print('\n==========\n')
print('Резултат преобразований:')
print(reCode(inputVal))
print('\n==========\n')

