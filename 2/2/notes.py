############################################################################################################################
#  Pipes and pipelines
#  Pipeline Construction
#  Multi-Lingual Pipelines (c++ and perl)
#
#
############################################################################################################################

print('\n\n----------------------read, print odds---------\n\n')
import sys
file_path = sys.argv[1]
with open(file_path, 'r') as infile:
    for n in [int(x) for x in infile.readlines() if int(x) % 2 != 0]:
        print n

print('\n\n----------------------read, print evens--------\n\n')
file_path = sys.argv[1]
with open(file_path, 'r') as infile:
    for n in [int(x) for x in infile.readlines() if int(x) % 2 != 1]:
        print n


print('\n\n----------------------read from std::in, print even numbers---------------------\n\n')
for n in [int(x) for x in sys.stdin.readlines() if int(x) % 2 != 1]:
    print n
#cat stuff.txt | python notes.py stuff.txt
## I'm getting tired of just typing his slides, go check canvas for good examples of piping
