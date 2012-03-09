def fib_gen(max):
    prev, cur = 0, 1
    while cur < max:
        yield cur
        prev, cur = cur, prev + cur
        
print sum(x for x in fib_gen(4000000) if not(x%2))

