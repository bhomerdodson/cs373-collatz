# -------
# imports
# -------

import sys

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

cache = 1000000 * [None]

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
        if cache[x] != None:
            count = cache[x]
            if count > maxCount:
                maxCount = count
            continue
        while calcNum > 1:
            if (calcNum % 2) == 0:
                calcNum = (calcNum / 2)
                if (calcNum < 1000000) and cache[calcNum] != None:
                    count += cache[calcNum]
                    break
                count += 1
            else:
                calcNum = ((calcNum * 3) + 1) / 2
                if (calcNum < 1000000) and cache[calcNum] != None:
                    count += 1 + cache[calcNum]
                    break
                count += 2

        if count > maxCount:
            maxCount = count
        if cache[x] == None:
            cache[x] = count
    
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
        




# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
