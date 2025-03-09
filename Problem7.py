#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
    number = 10001
    prime_count = 0
    factor = 1
    
    while prime_count < number:
        factor += 1
        if isPrime(factor):
            prime_count += 1
    
    print(factor)

if __name__ == '__main__':
  main()
