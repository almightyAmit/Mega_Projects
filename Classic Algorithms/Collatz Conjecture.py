# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
def Collatz(inNum, count=0):
    if inNum<=1:
        return count
    if inNum%2==0:
        return Collatz(inNum/2, count + 1)
    else:
        return Collatz(inNum*3+1, count + 1)

s = int(input())
print(Collatz(s))
