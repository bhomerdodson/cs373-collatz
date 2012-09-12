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

def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0
    v = 1
    maxCount = 1
    calcNum = 0
    a = 0
    b = 0
    if i <= j:
        a = i
        b = j
    else:
        a = j
        b = i
    k = b + 1
    if(a <= (b / 2)):
        a = (b / 2)
    for x in range(a, k):
        calcNum = x
        count = 1
        while calcNum > 1:
            if (calcNum % 2) == 0:
                count += 1
                calcNum = (calcNum / 2)
            else:
                count += 2
                calcNum = (calcNum * 3) + 1

        if count > maxCount:
            maxCount = count
    
    assert maxCount > 0
    assert v > 0
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
