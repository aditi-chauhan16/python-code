#wap to generate fibonnaci series of a number
n=int(input("enter the number")
sum=0
num = int(input('enter a number: '))
factorial = 1
if num < 0:
  print("factorial doesn't exist for negative numbers")
elif num == 0:
  print("factorial of 0 is 1")
else:
  for i in range(1, num+1):
    factorial = factorial * i
  print("the factorial of the given {num} is " + str(factorial))
  
  
