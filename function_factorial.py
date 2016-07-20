def factorial(n):
	factorial = 1
	for i in range(1, n + 1):
		factorial *= i
	return factorial

#single number factorial
n = int(raw_input('Enter a number: '))
print factorial(n)

#loop to factorial up to n
n = int(raw_input('Enter a number to compute factorials up to: '))
for i in range(1, n + 1):
	print factorial(i)

#recursive function
def recurse(n, i, factorial):
	if i == n:
		return factorial*n
	else:
		return recurse(n, i+1, factorial*i)

n = int(raw_input('Enter a number to compute factorial recursively: '))
print recurse(n, 1, 1)
