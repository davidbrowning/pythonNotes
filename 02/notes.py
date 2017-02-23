#!/usr/bin/python

import re
import sys
import os
import fnmatch

def find_files(filepat, rootdir):
    for path, dirlist, filelist in os.walk(rootdir):
            for file_name in fnmatch.filter(filelist, filepat):
                yield os.path.join(path, file_name)
