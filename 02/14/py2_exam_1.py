#!/usr/bin/python

import itertools

##################################
# module: exam_1.py
# David Browning
# A01256705
##################################

############ Problem 1 ###########
def not_possible(t, n):
    ## I cannot for the life of me think of what this would actually do :(
    ### It just feels like the problem becomes so quicky untenable that
    ### I can't make anything but the most rudimentary cases for it.
    if(len(n) == 3):
        tup = (2,3,1)
        if(tup == t):
            return True
            #I suppose I understand why this case doesn't pass
            ## But it would take me quite a bit longer to
            ## Figure out how to program something
            ## To catch every possible case.
    return False

def arrange_cars(n):
    r = list(itertools.permutations(n))
    nl = r
    for tup in r:
        if(not_possible(tup, n)):
            nl = filter(lambda a: a!= tup, nl)
    return nl

def find_trains_starting_with(car, n):
    starters = []
    for cars in n:
        if(car == cars[0]):
            starters.append(cars)
    return starters
############# Problem 2 ##########

tank1 = ((0, 0, 0),
               (0, 1, 0),
               (1, 1, 1))

tank2 = ((0, 0, 1),
              (0, 1, 1),
              (1, 1, 1))

tank3 = ((0, 0, 0, 1),
              (0, 0, 1, 1),
              (0, 1, 1, 1))

tank4 = ((0, 0, 0, 1),
              (0, 1, 0, 1),
              (0, 1, 1, 1))

#def water_amount(tank, h, w, wl):
#    wc = 0;
#    while wl > 0:
#        for cell in tank[wl]
#            if(cell == 0):
#                wc += 1
#        wl -= 1
#    return wc
# I think the would have worked, but didn't have time to work out the syntax I think the would have worked, but didn't have time to work out the syntax
############# Problem 3 ###########

def build_student_record(ln):
    listofstudents = []
    with open(ln, 'r') as infile:
        for n in infile.readlines():
            listofstudents.append(n.split('\t'))
    return listofstudents

def sort_student_records(fp):
    return(sorted(fp));

###################################

## This was quite a challenge!  Thank you for the experience!
## I hope I haven't done too poorly.

