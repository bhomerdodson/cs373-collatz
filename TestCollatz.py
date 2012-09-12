#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% python TestCollatz.py >& TestCollatz.py.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_empty (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        
    def test_read_output_as_input (self) :
        r = StringIO.StringIO("1 10 20\n5 10 20\n")
        a = [0,0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
        a = [0,0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 5)
        self.assert_(a[1] == 10)
        
    def test_read_no_separation (self) :
        r = StringIO.StringIO("1 10 20 5 10 20\n")
        a = [0,0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
        a = [0,0]
        b = collatz_read(r, a)
        self.assert_(b == False)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)
        
    def test_eval_swapped (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
        
    def test_eval_lowest_possible_evaluation (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_huge_range (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_swapped (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")
    
    def test_print_empty (self) :
        w = StringIO.StringIO()
        collatz_print(w, "", "", "")
        self.assert_(w.getvalue() == "  \n")
        
    def test_print_multiple (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "1 10 20\n10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_swapped (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")
        
    def test_solve_small_and_huge_range (self) :
        r = StringIO.StringIO("1 1\n1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 999999 525\n")
        
    def test_solve_empty (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
