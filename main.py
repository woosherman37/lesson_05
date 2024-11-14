#Small app to simulate conversations between 2 individuals

name = input(f"\nHi, What is your name? ")

if name == "tom":
	print(f"\nYou are NOT welcome here, {name}! Get out!\n")
	exit() #stop code execution

else:
	print(f"\nCome on in, {name}!\n")

x = input(f"\nJust give me a number and I'll show you I can count\n")

x = int(x)

print(f"\nOk, thanks. I will start from 1 and stop at {x}\n")

for num in range(1, x):
	print(num)




