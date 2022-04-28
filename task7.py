my_list = [3, 5, 2, 1, 4, 4, 1, 7, 7, 8, 8]

uniqeList = [item for item in my_list if my_list.count(item) == 1]

print('\n----------\n')
print('Заданный список: ' + str(my_list))
print('\n----------\n')

print('\n----------\n')
print('Уникальные значения: ' + str(uniqeList))
print('\n----------\n')