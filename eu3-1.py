import sys
import math

def gpf(num):

    num = abs(num)
    
    if num == 0:
        return 'Undefined' # also, you're being annoying 
        
    if num < 4:
        return num # shortcut for 1,2,3
        
    # The basic plan is to divide out increasingly large primes up to the sqrt
    # of the number.  It's safe to try and pull out non-primes, they just won't 
    # do anything.
    
    # Lets start by pulling out the 2's
    fact = 2
    while (num % fact == 0):
        num /= fact
    if num == 1: # perfect power of 2
        return fact
        
    # now we pull out the 3's
    fact = 3
    while (num % fact == 0):
        num /= fact
        
    # now we pull out everything else.  I don't know much about prime patterns,
    # but I do know they are always odd after 2, so we only need to check odds
    while(math.sqrt(num) > fact): # only need to check up to the sqrt'
        fact += 2 # next odd number
        while (num % fact == 0):
            num /= fact
            
    return max(num,fact)
    
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        for each in range(101):
            x = gpf(each) 
            if (each == x):
                print '{} is prime!'.format(x)
            else:
                print 'gpf({0}) = {1}'.format(each, x)
    else:
        print gpf(int(sys.argv[1]))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    