#!/usr/bin/python3

class Divisor:
	value = 0

	def __init__(self):
		pass

	def readValue(self):
		self.value = int(input("Divisor: "))

	def getValue(self):
		return self.value


divisor1 = Divisor()
divisor2 = Divisor()

divisor1.readValue()
divisor2.readValue()

for number in range(1001):
	print(number, end="")
	if number % divisor1.getValue() == 0:
		print(" HANS", end="")
	if number % divisor2.getValue() == 0:
		print(" DEKKERS", end="")
	print("")
