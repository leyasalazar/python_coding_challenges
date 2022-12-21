# Collatz Conjecture (3n+1)

def hotpo(n):
    count = 0
    while n != 1:
        if n%2==0:
            n = n/2
            count += 1
        else:
            n = 3*n+1
            count += 1
    return count