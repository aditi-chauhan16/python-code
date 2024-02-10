# #WRITE A FUNCTION TO CREATE A FIBONACCI SERIES OF A NUMBER
def fib(n):
    a=0
    b=1
    for i in range(2,n+2):
      c=a+b
      a=b
      b=c
      print(c)
fib(8)
