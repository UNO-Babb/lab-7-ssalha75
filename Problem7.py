#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
    number = 10001
    prime_count = 0
    candidate = 1
    
    while prime_count < number:
        candidate += 1
        if isPrime(candidate):
            prime_count += 1
    
    print(candidate)

if __name__ == '__main__':
  main()
