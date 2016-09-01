'''
@author: Joel Christophel
'''

def triangularNumber(n):
    if (n > 0 and isinstance(n, int)):
        return n*(n+1)/2

def positiveFactors(n):
    if (isinstance(n, int)):
        if n == 1:
            return [1]
        else:
            n = abs(n)
            factors = []
            for i in range(1, int(round(n**(1.0/2)))+1):
                if n % i == 0:
                    factors.append(i)
                    pair = n/i
                    if pair != i:
                        factors.append(n/i)
        return factors

def firstTriangularNumberWithNFactors(n):
    count = 1
    maxLength = 0
    while True:
        triangle = triangularNumber(count)
        numFactors = len(positiveFactors(triangle))
        if numFactors < n:
            if maxLength < numFactors:
                maxLength = numFactors
                print(maxLength)
            count += 1
        else:
            break
    print(str(triangle) + ' is triangular number #' + str(count) + ' and has ' + 
      str(numFactors) + ' divisors, making it the first triangular number with ' + str(n) + ' or more divisors.')

firstTriangularNumberWithNFactors(501)