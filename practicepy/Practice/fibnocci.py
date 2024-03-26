def fibnocci_printall(n):
    fib_series=[1,1]
    if n <=1:
        return fib_series[0]
    elif n <=2 :
        return fib_series
    else:
        #while len(fib_series)<n:
            for i in range(2,n):
                fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

print(fibnocci_printall(10))
#1 1 2 3 5 8

def fibonacci_printall_1(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two terms

    # Generate Fibonacci series up to the nth term
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Change the value of 'terms' to generate Fibonacci series up to different number of terms
n = 10
fib_series = fibonacci_printall_1(n)
print("Fibonacci series up to {} terms: {}".format(n, fib_series))




