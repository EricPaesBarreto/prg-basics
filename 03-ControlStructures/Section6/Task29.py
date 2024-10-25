N = int(input('Enter N: '))
count = 2
primes = ''
while N > 0:
    isPrime = True;
    for i in range(2, count):
        if(count % i == 0 and count != i): isPrime = False; break;
    if(isPrime): N-=1; primes+=(str(count)+' ')
    count+=1

print(primes)