import random

def RangeRandom(low,high):
    #low, high is positive floats or ints
    #low is less or equal high
    low = float(low)
    high = float(high)
    assert high>=low and low>=0 and high>=0 
    rand = random.random()*(high-low)+low
    return rand

def RangeIntRandom(low,high):
    #low, high is positive floats or ints
    #low is less or equal high
    low = float(low)
    high = float(high)
    low = round(low)
    high = round(high)
    assert high>=low and low>=0 and high>=0
    rand = random.random()*(high-low)+low
    rand = round(rand)
    return rand

for i in range(10):
  x = RangeIntRandom(5.5,15)
  print(x)
