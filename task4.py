from random import randint
 
def listChecker(list):
    ch = [int(i) for i in list if i % 2 == 0]
    return ch

print('Pls, insert value:')
inputVal = int(input())

list = [i for i in range(1,inputVal)]

print('\n----------\nInput value is: ' + str(inputVal) + '\nList value is: ' + str(list))
print('----------\n')
print('----------')
print('Output value of list is: ' + str(listChecker(list)))
print('----------\n')