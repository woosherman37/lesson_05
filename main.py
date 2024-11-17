#Small app to simulate conversations between 2 individuals

import time 


name = input(f"\nHi, What is your name? ")

if name == "tom":
	print(f"\nYou are NOT welcome here, {name}! Get out!\n")
	exit() #stop code execution

else:
	print(f"\nCome on in, {name}!\n")

x = input(f"\nJust give me a number and I'll show you I can count\n")

x = int(x)

if x <= 1:
	x = input(f"\nJust give me a number higher than 1 please\n")
	x = int(x) 

print(f"\nOk, thanks. I will start from 1 and stop at {x}\n")

for num in range(1, x+1):
	print(f"This number is: {num}")
	time.sleep(1.5)

print(f"I've finished!")

	



















