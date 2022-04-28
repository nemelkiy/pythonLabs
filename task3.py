
def findAndMath(inList):
    maxVal = max(inList)
    minVal = min(inList)

    resultVal = maxVal - minVal

    return resultVal



list = [10,125,15,35,9,289,175,13,5]

print('\n----------\nMax value is: ' + str(max(list)) + '\nMin value is: ' + str(min(list)))
print('---------')
print('Result of function is: ' + str(findAndMath(list)))
print('---------')