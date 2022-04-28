print('Введите значение num:')
numVal = int(input())
print('Введите значение lenght:')
lenVal = int(input()) + 1

i = 0
i += 1
result = [numVal * i for i in range(1,lenVal)]

print('\n----------\n')
print('Результат выполнения: ' + str(result))
print('\n----------\n')