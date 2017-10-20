#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------


# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    eager cache peak_list inside function holds every peak number, identify the peak range n is in
    return the value that produces the max cycle length of the range [1, n]
    """
    assert n > 0

    # eager cache filled with the peak number values
    # peak number has a collatz sequece length greater than or equal to all length all collatz
    # sequence length created by numbers in [1,n]
    # for example, 3 has a collatz sequece length of 8 which is the largest in range [1,3]
    # same to 3732423, the length of 597 is the largest in [1,3732423], but in this problem no
    # number in (3732423,5000000] can generate a greater length than 3732423
    peak_list = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327,
                 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171,
                 10971, 13255, 17647, 17673 ,23529, 26623, 34239, 35497, 35655, 52527, 77031,
                 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065,
                 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]

    # First case. When n happens to be a peak number, then no number before it has a length greater
    # than itself. Return itself
    if n in peak_list:
        assert n > 0
        return n

    # Second case. When n is greater than the number(3732423) that has largest length in
    # [1,5000000]. Return 3732423 which is the last element in peak_list
    if n > peak_list[-1]:
        assert peak_list[-1] > 0
        return peak_list[-1]

    # Last case. When n is between 2 peaks, its length must be less than last peak since itself is
    # not a peak. Return last peak
    list_size = len(peak_list)
    for i in range (list_size):
        if n < peak_list[i]:
            assert peak_list[i-1] > 0
            return peak_list[i-1]

# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)
