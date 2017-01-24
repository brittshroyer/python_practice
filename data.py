myList = [1,2,3,4,5,6]

print myList[0]

myList[0] = 'new value'
print myList

myList.append(99)
print myList

firstItem = myList.pop(0)
print firstItem
print myList

lastItem = myList.pop()
print lastItem
print myList

myList.insert(0,33)
print myList

myTuple = (1,2,3,4,5,5,5, 'hello', 'tuples', True)

print myTuple[0]

print myTuple.count(5)

print myTuple.index(5)

myString = 'hello python python!'

print myString.find('python')
print myString.index('python')
print myString.title()

print myString.index('python')
