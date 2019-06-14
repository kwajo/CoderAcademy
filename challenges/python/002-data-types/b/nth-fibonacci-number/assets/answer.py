golden = (1 + 5 ** 0.5) / 2
def nth_fibonacci(n):
  fib = long((golden**n-(-golden)**-n)/5**.5)
  #print ('Number {} in the fibonacci sequence is: {}'.format(n,fib))
  print(fib)
  print(n)
  return long(fib)
  pass


def fib(n): 
    a = q = long(1)
    b = p = long(0)
    while n > 0: 
        if n % 2 == 0: 
            qq = q*q
            q = 2*p*q + qq
            p = p*p + qq
            n /= 2
        else: 
            aq = a*q
            a = b*q + aq + a*p
            b = b*p + aq
            n -= 1
    print(b)
    return b;

fib(70000)
'''
for i in range (0,70000):
	print("sequence: " +str(i))
        fib(i)
#	nth_fibonacci(i)
'''	
