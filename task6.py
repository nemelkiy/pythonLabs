print('Введите число')
inputVal = int(input())

print('\n----------\n')
print('Введенное число равно: ' + str(inputVal))
print('\n----------\n')

toBit = bin(inputVal)

print('\n----------\n')
print('В двоичной системе через bin это: ' + str(toBit))
print('\n----------\n')

wBit = ''
 
while inputVal > 0:
    wBit = str(inputVal % 2) + wBit
    inputVal = inputVal // 2
 
print('\n----------\n')
print('В двоичной системе через вычисления это: ' + str(wBit))
print('\n----------\n')