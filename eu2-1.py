def even_fib(max):
    prev =1 
    cur = 1
    next = 1
    while next < max:
        if not (next % 2): 
            yield next
        next = prev+cur
        prev = cur
        cur = next
        
print sum(even_fib(4000000))

