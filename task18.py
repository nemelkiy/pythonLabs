def getInfo(head: list, page: int):
    headers = ''
    for key in head:
        if headers == '':
            headers = key
        else:
            if abs(head[headers] - page) > (abs(head[key] - page)):
                headers = key
            elif abs(head[headers] - page) == (abs(head[key] - page)):
                if head[headers] < head[key]:
                    headers = key

    return headers

print(getInfo({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10))

print(getInfo({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200))

print(getInfo({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3))
