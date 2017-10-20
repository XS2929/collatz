#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO("10\n")
        n = collatz_read(r)
        self.assertEqual(n, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        m = collatz_eval(3732424)
        self.assertEqual(m, 3732423)

    def test_eval_2 (self) :
        m = collatz_eval(877)
        self.assertEqual(m, 871)

    def test_eval_3 (self) :
        m = collatz_eval(35655)
        self.assertEqual(m, 35655)

    def test_eval_4 (self) :
        m = collatz_eval(3732422)
        self.assertEqual(m, 3542887)

    def test_eval_5 (self) :
        m = collatz_eval(5000000)
        self.assertEqual(m, 3732423)

    def test_eval_6 (self) :
        m = collatz_eval(1)
        self.assertEqual(m, 1)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 10)
        self.assertEqual(w.getvalue(), "10\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("10\n3732423\n3732500\n17\n649\n650\n654\n655\n5000000\n1\n5\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "3732423\n3732423\n9\n649\n649\n654\n655\n3732423\n1\n3\n")

    def test_solve1 (self) :
        r = StringIO("3\n15\n15\n20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "9\n9\n19\n")
# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    main()
