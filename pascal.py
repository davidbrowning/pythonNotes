#!/usr/bin/python

index = int(raw_input())

#            1
#          1   1
#        1   2   1
#      1   3   3   1
#    1   4   6   4   1
#  1   5  10  10   5   1

# 0 : 1
# 1 : 1, 1
# 2 : 1, 2, 1

def triangle(rows):

    for rownum in xrange (rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)
    print()


triangle(index)

# Source
# http://stackoverflow.com/questions/3134813/pascals-triangle-in-python
