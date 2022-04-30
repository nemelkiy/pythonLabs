def found_letter(lst):
    res = {x:lst.count(x) for x in lst}

    max_value = 0
    for key in res:
        if max_value < res[key]:
            max_value = res[key]
    list_most_common = []
    for key, value in res.items():
        if value == max_value:
            list_most_common.append(key)
    return list_most_common
    
inpList = ["A", "A", "A", "B", "B", "C", "A", "B", "B"]

print('\n==========\n')
print('Входное значение списка:\n')
print(inpList)
print('\n==========\n')
print('Чаще всего встречается: ' + str(found_letter(inpList)))
print('\n==========\n')