#!/usr/bin/python3
a=int(input("Input a number: "))
b=int(input("Input a number: "))
for n in range(1001):
	print(n, end="")
	if n%a==0:
		print(" HANS", end="")
	if n%b==0:
		print(" DEKKERS", end="")
	print("")
