def removeDuplicates(string: str) -> str:
    i = 0
    result = ''
    while i < len(string):
        if string[i] != string[i + 1]:
            result += string[i]
            i += 1
        else:
            i += 2
        if i == len(string) - 1:
            result += string[i]
            break
        elif i > len(string) - 1:
            break
    return result if result else 'Empty String'

print('\n==========\n')
print('Введите строку:')
inputVal = str(input())
print('\n==========\n')
print('Вы ввели:')
print(inputVal)
print('\n==========\n')

print('Результат обработки:')
print(removeDuplicates(inputVal))
