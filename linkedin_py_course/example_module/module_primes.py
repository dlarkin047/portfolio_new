# This is a module.
# It is a file that can contain mulitple methods and funtions which you call call from another file.

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
        return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n):
            foundPrimes.append(n)
    return foundPrimes

print(f'module_primes.py module name is {__name__}')

if __name__ == '__main__' :
    print('This is a module. Import module by using:\n import module_primes')