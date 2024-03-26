def fibnocii(n):

    l=[0,1]
    f=0
    s=0
    n=0
    #1,1,2,3,5
    if n <= 1:
         return l[:]
    if n <= 2:
         return l[:]
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
        print(l[i])
        return l


    # if n <= 1:
    #     return fib_sequence[:n + 1]
    #
    # for i in range(2, n + 1):
    #     next_fib = fib_sequence[-1] + fib_sequence[-2]  # Compute the next Fibonacci number
    #     fib_sequence.append(next_fib)  # Add the next Fibonacci number to the sequence
    #
    # return fib_sequence

print(fibnocii(5))


