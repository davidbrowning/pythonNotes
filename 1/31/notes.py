from datetime import datetime
import sys

# stored in sys.argv as strings.

for argn, arg in zip(xrange(len(sys.argv)), sys.argv):
    print argn, '--->', arg

# o inserts new line beneath cursor O inserts it above

import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-m','--method', help='rec/iter', default='iter')
ap.add_argument('-n', '--n', help='nth Fibonacci to compute', type=int, default=0)
arg_table = vars(ap.parse_args())

print (datetime.now())


print('-----------------------File Processing-----------------\n\n')
###############################
# Write a program that takes a file path of a file of integers (assuming 1 # per line)
#  make a function and apply it to each integer obtained
##############################


def process_lines(file_path, fun):
    with open(file_path, 'r') as infile:
        return [fun(int(line)) for line in infile]


def addTen(n):
    return n+10

import re
print(process_lines('numbers.txt', addTen))

a_num_and_email = r'.*(A\d+)\s*([\w\.-]+\.(?:com|net|org|edu)).*'
first_name_last_name_a_num = r'(\w+)\s*(\w+)\s*(A\d+).*'

#def make_info_extractor(pat):
#    def info_extractor(line):
#        match = re.match(pat,line)
#        if match is not None:
#            return [match.group(i) for i in xrange(1, len(match.groups())+1]
#    return info_extractor
#
#
#def process_lines(file_path, fun):
#    with open(file_path, 'r') as infile:
#        return [fun(line) for line in infile]
#
#def main(file_path):
#    print '-----------'
#    for groups in process_lines(file_path, make_info_extractor(a_num_and_email))
#        print '\t'.join(groups)
#


# it didn't work :( see his source code on canvas python said line 46 was invalid syntax

#main('students.txt')


print('-----------------------Read file, sort items-----------\n\n')

def sortThings(file_path):
    infile = open(file_path, 'r')
    for item in sorted([line for line in infile.readlines()]):
        print item,

sortThings('words.txt')


def sortOtherThings(file_path):
    infile = open(file_path, 'r')
    for item in sorted([int(line) for line in infile.readlines()]):
        print item,

sortOtherThings('numbers.txt');
