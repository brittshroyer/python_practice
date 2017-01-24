myList = [1,2,3,4]
myTuple = (1,2,3,4)

if 1 in myList:
    print 'Do I print?'

if 4 in myTuple:
    print 'yo'

if 5 not in myTuple:
    print 'no'

aList = ['apples', 'oranges', 'pineapples']

whatIsRange = range(1,10)
whatIsRangeAgain = range(20,30)

print whatIsRange
print whatIsRangeAgain

for i in range(len(aList)):
    print 'value is %s' % aList[i]

for index, value in enumerate (aList):
    print 'the index is %d' % index
