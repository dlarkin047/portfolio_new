# This is your main python file.
# In here you will import your module and call its methods/Functions.

import module_primes

print(module_primes.isPrime(3))
print(module_primes.listPrimes(20))

# You can import a function/method from a module without having to import the whole module

from module_primes import listPrimes

print(listPrimes(30))