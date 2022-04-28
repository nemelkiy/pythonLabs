def coountPlaces(string: str) -> int:
    coountPlaces = string.count('0')
    numberOfPersons = string.count('1')
    return coountPlaces - numberOfPersons if coountPlaces - numberOfPersons >= 0 else 0
    
print('\n==========\n')
print('Введите схему пляжа:\n')
beachPlaces = str(input())

print('\n==========\n')
print('Схема пляжа:\n')
print(beachPlaces)
print('\n==========\n')
print('Резултат вычислений:')
print(coountPlaces(beachPlaces))
print('\n==========\n')

