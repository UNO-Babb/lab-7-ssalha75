#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    number = 2000000
    sumPrimes = 0
    
    for factor in range(2, number):
        if isPrime(factor):
            sumPrimes += factor
    
    print(sumPrimes)

if __name__ == '__main__':
  main()