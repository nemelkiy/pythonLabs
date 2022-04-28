print('Введите значение X:')
xVal = int(input())
print('Введите значение Y:')
yVal = int(input())

if xVal > 0 and yVal >0:
    print('\n----------\n')
    print('Точка находится в I координатном углу')
    print('\n----------\n')
elif xVal < 0 and yVal > 0:
    print('\n----------\n')
    print('Точка находится во II координатном углу')
    print('\n----------\n')
elif xVal < 0 and yVal < 0:
    print('\n----------\n')
    print('Точка находится в III координатном углу')
    print('\n----------\n')
else:
    print('\n----------\n')
    print('Точка находится в IV координатном углу')
    print('\n----------\n')