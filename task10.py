def found_letter(lst):
    res = {x:lst.count(x) for x in lst}
    return max(res, key=res.get)

inpList = ["A", "A", "A", "B", "B", "C", "A"]
print('\n==========\n')
print('Входное значение списка:\n')
print(inpList)
print('\n==========\n')
print('Чаще всего встречается: ' + str(found_letter(inpList)))
print('\n==========\n')