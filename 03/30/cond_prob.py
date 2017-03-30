#!/usr/bin/python

from numpy import random
random.seed(0)

peopleInAgeGroup = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchasesInAgeGroup = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}

numOfPurchases = 0;
numOfPeople = 10000;

for _ in xrange(numOfPeople):
    ageGroup = random.choice([20,30,40,50,60,70])
    purchaseProbability = float(ageGroup) / 100.0
    peopleInAgeGroup[ageGroup] += 1
    if(random.random() < purchaseProbability):
        numOfPurchases += 1
        purchasesInAgeGroup[ageGroup] += 1


def probOfPurchaseGivenAgeGroup(x):
    return float(purchasesInAgeGroup[x])/peopleInAgeGroup[x]

def probOfAgeGroup(x):
    return float(peopleInAgeGroup[x])/numOfPeople

def probOfPurchase():
    return float(numOfPurchases)/numOfPeople

def probOfPurchaseAndAgeGroup(x):
    return float(purchasesInAgeGroup[x])/numOfPeople

def condProbOfPurchaseGivenAgeGroup(x):
    return probOfPurchaseAndAgeGroup(x)/probOfAgeGroup(x)

for ag in xrange(20, 80, 10):
    print('P(purchase | %d) = %f' % (ag, probOfPurchase()))


for ag in xrange(20, 80, 10):
    print('P(purchase | %d) = %f' % (ag, probOfAgeGroup(ag)))

for ag in xrange(20, 80, 10):
    p = probOfPurchaseGivenAgeGroup(ag)
    cp = condProbOfPurchaseGivenAgeGroup(ag)
    print('p = %f; cp = %f' % (p, cp))
