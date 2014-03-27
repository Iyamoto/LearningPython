# Testing recursive ideas and plots

def check(x0,y0,xn,yn):
    """Params checker"""
    assert type(x0)==int and type(y0)==int
    assert type(xn)==int and type(yn)==int
    return None

def getDirection(x0,xn):
    """Helper is not for users
    return direction from x0 to xn"""
    if x0 < xn:
        dx = 1
    elif x0 > xn:
        dx = -1
    else:
        dx = 0
    return dx    

def Move(x0,y0,xn,yn):
    """Wrapper for MoveRec"""
    check(x0,y0,xn,yn)
    way = [(x0,y0)]
    return MoveRec(x0,y0,xn,yn,way)

def MoveRec(x0,y0,xn,yn,way):
    """Helper is not for users
    Get start and end coordinates
    Get reference to list for hints (way)
    return list of coordinate pairs"""
    # Get directions
    dx = getDirection(x0,xn)
    dy = getDirection(y0,yn)
    if dx==0 and dy==0:# Base case
        return way
    else:
        way.append((x0+dx,y0+dy))
        return MoveRec(x0+dx,y0+dy,xn,yn,way)

def testMove(x0,y0,xn,yn):
    check(x0,y0,xn,yn)
    print('Testing:',(x0,y0),(xn,yn))
    test = Move(x0,y0,xn,yn)
    print("Should be True:", type(test)==list)
    print(test)
    return None

def TestHarness():
    """testing harness"""
    testMove(0,0,0,0)
    testMove(0,0,1,1)
    testMove(3,4,1,1)
    testMove(-5,4,1,-2)
    testMove(0,0,-1,-1)
    testMove(0,0,10,5)
    testMove(0,0,-5,-10)
    return None

#TestHarness()

def getAxis(x0,xn):
    """Helper is not for users"""
    axis_left = min(x0,xn)-1
    axis_right = max(x0,xn)+1
    return (axis_left,axis_right)

def PlotWay(x0,y0,xn,yn):
    check(x0,y0,xn,yn)
    #print(x0,y0,xn,yn)
    way = Move(x0,y0,xn,yn)
    xs = list()
    ys = list()
    for pair in way:
        xs.append(pair[0])
        ys.append(pair[1])
    # Plot    
    import matplotlib.pyplot as plt
    plt.plot(xs, ys, 'ro')
    axis_x = getAxis(x0,xn)
    axis_y = getAxis(y0,yn)
    plt.axis([axis_x[0], axis_x[1], axis_y[0], axis_y[1]])
    title = 'Way from '+str(x0)+','+str(y0)+' to '+str(xn)+','+str(yn)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return None    

import random

def RangeRandom(low,high):
    #low, high is positive floats or ints
    #low is less or equal high
    low = float(low)
    high = float(high)
    assert high>=low# and low>=0 and high>=0 
    rand = random.random()*(high-low)+low
    return rand

def RangeIntRandom(low,high):
    #low, high is positive floats or ints
    #low is less or equal high
    low = float(low)
    high = float(high)
    low = round(low)
    high = round(high)
    assert high>=low# and low>=0 and high>=0
    rand = random.random()*(high-low)+low
    rand = round(rand)
    return rand

#Plot(0,0,0,0)
PlotWay(RangeIntRandom(-20,20),RangeIntRandom(-20,20),RangeIntRandom(-20,20),RangeIntRandom(-20,20))




        
