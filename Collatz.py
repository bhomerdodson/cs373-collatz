#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array of int
return true if that succeeds, false otherwise
"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------
"""
Used to store amount of steps a number takes to satisfy the end condition for
the 3n+1 problem.  Reduces the time taken to calculated the maximum number of
steps within a range of numbers.
"""
cache = 1000000 * [None]

"""
Within a range of two numbers, calculates the maximum amount of steps it took
to satisfy the end condition of the 3n+1 problem
@param i The beginning of the range
@param j The end of the range

@return The maximum amount of steps taken within a range of numbers
"""

def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0
    maxCount = 1
    calcNum = 0
    a = 0
    b = 0
    """
    Determines if i and j need to be switched due to i being less than j
    """
    if i <= j:
        a = i
        b = j
    else:
        a = j
        b = i
    k = b + 1
    if(a <= (b / 2)):
        a = (b / 2)
        
    """
    Goes through the range of numbers
    """
    for x in range(a, k):
        calcNum = x
        count = 1
        """
        If the maximum amount of steps has already been calculated
        """
        if cache[x] != None:
            count = cache[x]
            if count > maxCount:
                maxCount = count
            continue
        """
        While the end condition for 3n+1 problem has not been met
        """
        while calcNum > 1:
            """
            Even case
            """
            if (calcNum % 2) == 0:
                temp = calcNum
                calcNum = (calcNum / 2)
                """
                If the maximum for the next number to be checked has been found
                """
                if (calcNum < 1000000) and cache[calcNum] != None:
                    """
                    If the maximum of the current number has not been found
                    """
                    if (temp < 1000000) and cache[temp] == None:
                        cache[temp] = 1 + cache[calcNum]
                    count += cache[calcNum]
                    break
                count += 1
            else:
                temp = calcNum
                calcNum = ((calcNum * 3) + 1) / 2
                """
                If the maximum for the next number to be checked has been found
                """
                if (calcNum < 1000000) and cache[calcNum] != None:
                    """
                    If the maximum of the current number has not been found
                    """
                    if (temp < 1000000) and cache[temp] == None:
                        cache[temp] = 2 + cache[calcNum]
                    count += 1 + cache[calcNum]
                    break
                count += 2

        if count > maxCount:
            maxCount = count
        if cache[x] == None:
            cache[x] = count
    
    assert maxCount > 0
    return maxCount

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
prints the values of i, j, and v
w is a writer
i is the beginning of the range, inclusive
j is the end of the range, inclusive
v is the max cycle length
"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
