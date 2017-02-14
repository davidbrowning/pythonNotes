#!/usr/bin/python

import py2_exam_1 as pytest

n = (1,2,3)
print pytest.arrange_cars(n);
print pytest.find_trains_starting_with(1,pytest.arrange_cars(n))
print  pytest.build_student_record("students.txt")
