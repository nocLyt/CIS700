import random
from turtle import *

def first():
    a = random.randint(1, 128)
    while(True):
        b = int(input("Input a number:"))
        if a > b :
            print "your number is too low!"
        elif a < b:
            print "your number is too high!"
        else:
            print "Right number!"
            break;


def sencond():
    a = random.randint(1, 300)
    print "The random number if %d" % a
    left, right = 1, 300
    while(left <= right):
        mid = (left + right) / 2
        print "Mid number is %d" % mid
        if (a < mid):
            print "Your mid number is too high!"
            right = mid - 1
        elif (a > mid):
            print "Your mid number is too low!"
            left = mid + 1
        else:
            print "Right number!"
            break;

def K(s):

    if s > 10:
        for a in [60, -120, 60, 0]:
            K(s / 3);
            lt(a)
    else:
        fd(s)
        for i in range(3):
            K(400);
            rt(120)

if __name__ == "__main__":
    # first()
    sencond()
