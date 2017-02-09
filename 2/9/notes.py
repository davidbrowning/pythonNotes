# Coding Exam Tuesday Posted at 8:55 Due by 10:30 NO LATE SUBMISSIONS!!!!!

############################################################################################################################
# covers everything we've been assigned on Homework (No OOP)
#  Problems will be similar to Homework
#
#  Don't expect regex on exams
#  Look for list comprehension
############################################################################################################################


############################################################################################################################
# Defining/Constructing Objects, Inheritance, Exceptions, Persistent Objects, Magic Methods & Protocols
#
############################################################################################################################

############################################################################################################################
#  Makes a Date class w/month, day, and year. Getters/setters, and toString functions.
#
#
############################################################################################################################

############################################################################################################################
# Inheritance:
#
#
############################################################################################################################

print('\n\n----------------------Inheritance--------------\n\n')
class A:
    def hello(self):
        print('hi, I am A!');

class B(A):
    def hello(self):
        print('hi, I am B!');


a = A()
b = B()

a.hello()
b.hello()


class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaaah...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk';


print('\n\n----------------------SongBird------------------------\n\n')

a = Bird()
a.eat()
a.eat()

b = SongBird()
try:
    b.eat()
except Exception, e:
    print('no can do boss(%s)' % e)

