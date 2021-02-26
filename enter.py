#!/usr/bin/python3

divisor1 = int(input("Input a number: "))
divisor2 = int(input("Input a number: "))

for number in range(1001):
	print(number, end="")
	if number % divisor1 == 0:
		print(" HANS", end="")
	if number % divisor2 == 0:
		print(" DEKKERS", end="")
	print("")
