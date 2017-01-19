#!/bin/python

## Sorting Sequences
### Types of sorting: Numerical or lexocographic (strings) 
## Guaranteed to be stable (two records equal? keep original placement in sequence)
## Py uses Timsort
## checkout demo online


####################
## Note! sorted(<thing>) does not change the thing, it returns a sorted list.
# <thing>.sort() actually changes the thing you're sorting
#
# some code:
################
lst = [4,5,6,1];
print(sorted(lst)); 
print(lst);
lst.sort();
print(lst);

s = set([4,5,6,1]);
sorted(s);
print(s);

###########################
# using the split() function
# 
##########################

print('----------------------------------------\n\n');
s = 'bb AA cC ee Dd'
print(s.split()); # splits on whitespace and returns substrings
print(str.lower);
print(map(str.lower, s.split()));

print(sorted(s.split(), key=str.lower));

print('----------------Student sorting--------------\n\n');
student_grades = [('john','nicholson',100),('ali','kutiyanawala',95),('tanwir','zaman',90)]

print('---------By Score------------\n');
print(sorted(student_grades, key=lambda sr:sr[2]));
print('---------By Score Reverse-----\n');
print(sorted(student_grades, key=lambda sr:sr[2], reverse=True));
print('---------By Name------------\n');
print(sorted(student_grades, key=lambda sr:str.lower(sr[0])));
print(sorted(student_grades, key=lambda sr:str.lower(sr[1])));

## if __name__ == '__main__': ## if you want to do stuff as soon as thing is executed.

print('---------Using Itemgetter------------\n');
from operator import itemgetter
print(sorted(student_grades, key=itemgetter(2)));

#############################
#
# Using comparator function
#
#############################
def funct1(x,y):
    if(x < y):
        return -1;
    if(x > y):
        return 1;
    return 0;
print('------------Using key=str------------\n');
sorted_lst=sorted(lst,cmp=funct1);

numbers=[3,1,11,2,24]
sorted_numbers=sorted(numbers,key=str);
print(sorted_numbers);
print('\n');

words = ['bb', 'aa', 'a', 'ccc', 'dddd'];
print(sorted(words, key=len));

print('--------------Using key=sum--------\n');

lst=[[1,2,3,5],[4,0,1],[0,0,1,0,1]]
print(sorted(lst,key=sum));
print(' ');

## Write a function that returns the even numbers

print('-----------function that returns even numbers---------\n');

def is_even(x):
    return x%2==0

print(filter(is_even,[1,2,3,4]));
print('');

# py3 -- filter returns a filter object. Pass the filter to a list!!!!

## List Comprehension & Set-Former Notation
### syntactic construct in some programming languages for building lists
###  from their specifications

## Write a Py program that builds {2 * x || x \in \mathbb{N}, 2 | x, x < 11}

print('------build a list s.t.{2 * x || x \in \mathbb{N}, 2 | x, x < 11}-----\n'); 

def build_list_1a():
    rslt = []
    x = 0
    while x < 11:
        if x % 2 == 0:
            rslt.append(2*x)

        x += 1
    return rslt

print build_list_1a();

def build_list_1b(): return [2*x for x in xrange(10) if x%2==0]

print('--- in a much more sexy 1 line way----------\n');
print('def build_list_1b(): return [2*x for x in xrange(11) if x%2==0]\n');

print build_list_1b();

print('--- build {4x || x \in \mathbb{N}, x^2 < 100} via list/loop----\n');

def build_list_2a():
    rslt = []
    x = 0
    while x**2 < 100:
        rslt.append(4*x)
        x+=1
    return rslt

print build_list_2a();

def build_list_2b(): return [4*x for x in xrange(101) if x**2 < 100]

print build_list_2b(); ## Pretty awesome
