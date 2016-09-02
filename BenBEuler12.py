##Ben Beidler
##Euler 12 problem
##9/1/16
##this version will work but is a brute force way of finding the answer
##and will take a long time.

def FindNextTriangle(n):
	return int(n * (n - 1)) / 2

def FindNumberOfDivisors(triangle):
	divisors = 0

	for x in range(1, triangle + 1):
		if triangle % x == 0: divisors += 1

	return divisors

n = 0
LastDivisor = 0
triangle = 0
while LastDivisor < 500:
	n += 1
	triangle = FindNextTriangle(n)
	LastDivisor = FindNumberOfDivisors(int(triangle))

else: print (('the lowest triangle number is ') + str(FindNextTriangle(n)))
	
