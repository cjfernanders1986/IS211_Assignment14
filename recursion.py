#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
    """Implement the Fibonnaci Sequence."""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """­ Implement Euclid’s GCD Algorithm."""
    while b:
        (a, b) = (b, (a % b))
    return a

    
if __name__ == '__main__':
    fibonacci(7)
    gcd(18, 2)