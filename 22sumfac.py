'''
# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5 # use this value for your computation
x = 0
for i in range(1, n+1):
	x += i
	print(x)
	
i got 1 3 6 10 15

'''
n = 5
fac = 1
for i in range (1, n+1):
	fac = fac * i
	print(fac)
"""
I get 1 2 6 24 120

python3 22sumfac.py
5 15 120 (?)
"""
