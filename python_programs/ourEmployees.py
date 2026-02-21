#!/bin/python3

from Employees import Employees

e1 = Employees("Hasan", "Ethical Hacker", "High", 2500)
e2 = Employees("JoJo", "Red Teamer", "High", 1500)

print(e2.name)

if e2.eligible_for_increment():
	print("Congrats! You've been promoted!")
else:
	print("You are not eligible for promotion")
