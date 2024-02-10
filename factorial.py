#WRITE A FUNCTION TO CREATE A FACTORIAL SERIES

def factorial():
    k = int(input("Enter a number whose factorial you want: "))
    if k == 0 or k == 1:
        print("The factorial is 1")
        return 1
    else:
        m = 1
        for i in range(1, k + 1):
            m *= i
        print(f"The factorial of {k} is {m}")
        return m
result=factorial()

#WRITE A FUNCTION USING RECURSION TO CREATE A FACTORIAL OF A NUMBER

def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

result = factorial_recursion(int(input("Enter a number whose factorial you want: ")))
print("Result:", result)

def fibonacci_recursive(n, n1=0, n2=1):
    if n == 0:
        return []
    elif n == 1:
        return [n1]
    else:
        return [n1] + fibonacci_recursive(n-1, n2, n1 + n2)

num = int(input("Enter the range till which you want it: "))
result = fibonacci_recursive(num)
print(f"The Fibonacci series is {', '.join(map(str, result))}")
