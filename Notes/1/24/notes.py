#!/bin/bash

## Solution with list Comprehension

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
