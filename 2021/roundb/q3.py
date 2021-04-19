import math
import bisect

"""
2
2021
2020
"""

# substring: 7pts, 9pts, 14pts
def sieve(n):
      
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    a = []
    for p in range(n + 1):
        if prime[p]:
            a.append(p)
    return a

def isPrime(n):
     
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True
     
    # This is checked so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True

def nextPrime(N):
 
    # Base case
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime

def prevPrime(N):

    # Base case
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime - 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime

    # get next prime after p

T = int(input())
Z = []
for t in range(T):
    Z.append(int(input()))
Zmax = max(Z)
primes = sieve(int(math.sqrt(Zmax)))
primes.append(nextPrime(primes[-1]))
for case, num in enumerate(Z):
    l = bisect.bisect(primes, int(math.sqrt(num)))
    if primes[l] * primes[l-1] > num:
        ans = primes[l-1] * primes[l-2]
    else:
        ans = primes[l] * primes[l-1]
    print(f"Case #{case+1}: {ans}")

#p1 = prevPrime(44)
#p2 = nextPrime(44)