print('\n==========\n')
print('Введите выражение:')
inputVal = str(input())


def strCalc(expression: str) -> float:
    args = expression.split()
    if args[1] == '+':
        return float(args[0]) + float(args[2])
    if args[1] == '-':
        return float(args[0]) - float(args[2])
    if args[1] == '*':
        return float(args[0]) * float(args[2])
    if args[1] == '/':
        if args[2] == '0':
            return -1
        return float(args[0]) / float(args[2])

print('\n==========\n')
print('Входное выражение:\n')
print(inputVal)
print('\n==========\n')
print('Резултат вычислений:')
print(strCalc(inputVal))
print('\n==========\n')