#!/bin/bash

## Solution with list Comprehension

print('------------------------Numpy Arrays------------------------------\n\n')
import numpy as np
a = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(a.shape) ### Z x Y array shows as (Z,Y)
print(a.ndim) ### the number of dimensions (in this case: 2)
print(a.sum())

###############################
# To place comment section press @c in normal mode
#
# Was goofing around in vim, see slides for notes.
##############################


def col_sums_w_numpy(na):
    return [na[:,c].sum() for c in xrange(na.shape[1])]

np_mat = np.arange(15).reshape(3,5)
for c, s in enumerate(col_sums_w_numpy(np_mat)):
    print('%d --> %d' % (c,s))

###############################
# Strings
#
# Look for matrix problems in next hw assignment.
# Single vs Double Quotes (from pydocs)
# Raw strings 'r' or 'R' to the py interpreter, there aren't many
# differences between single and double quotes. 
#  consistency is all that really matters, kulyuken prefers single quotes
# Use double quotes for string interpolation or embedding single quotes into 
#  double quotes. 
#
##############################

###############################
# search a string
# 
#
##############################

print('-----------------------find----------------------------\n\n')
txt = 'the sail just needs to open'
s = 'sail'
print(txt.find(s));
print(txt.find(s, 4));
print(txt.find(s, 4, 7));
print(txt.find(s, 4, 8));
print(txt[4:8]);

text = 'sail sail'
print(text.find('sail'));
print(text.find('sail', -5))
print(text.find('i'))
print(text.find('i', -4, -1))
###############################
# rfind (reverse find)
#
##############################

print('-----------------------rfind---------------------------\n\n')
print(text.rfind('l', 0, 4))
print(text.rfind('l'))
print(text.rfind('l',0,4))
#etc etc


print('------------------------join---------------------------\n\n')

###############################
# seperator is a string and seq is a sequence of strings
#
#
##############################
seq1 = ['the', 'sail', 'just', 'needs', 'to', 'open']
print('**'.join(seq1))
print('+++'.join(seq1))

seq3 = ('the', 'sail', 'just', 'needs', 'to', 'open')
## join statements will work the same

## Join doesn't work with non-strings!
## use map

print('-----------------------change num to string------------\n\n')
print('*'.join(map(str, (1,2,3,4,5))))
print('+'.join(map(str, (1,2,3,4,5))))

###############################
# Camel associated with perl 
#
##############################

## not recommended, but you can check the type of an object
def join_seq(separator, seq):
    if type(seq) is str:
        return separator.join(seq.split,' ')
    else:
        return separator.join(map(str, seq))


def join_number_range(separator, xrange_obj):
    return separator.join([str(x) for x in xrange_obj])

###############################
# Splitting strings
# text.split(separator) default separator is white space
#
##############################

print('-----------------------Splitting Strings---------------\n\n')
text_01 = 'word0 word1 word2'
print(text_01.split()) # or split(' '))
print('word0, word1, word2'.split(','))
separator = ','
text_02 = 'word0, word1, word2'
print(separator.join(text_02.split(separator))) ## Split then join
print(','.join('word0 word1 word2'.split()))
