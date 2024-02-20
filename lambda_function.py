#LAMBDA FUNCTION
#FILTER(function,iterator)
#PRINTS VALUES WITH SOME CONDITIONS
list_num=[1,2,3,4,5,6,7,8,9,10]
list_even=list(filter(lambda n: n%2==0, list_num))
print(list_even)


#MAP(,iterator)
#HELPS TO UPDATE

def update(n):
   return n*2

list_3=list(map(update,list_even))
print(list_3)

 #WITH LAMBDA

list_3=list(map(lambda n: n*2,list_even))
print(list_3)

#REDUCE(function,iterator)
from functools import reduce

def adding(a,b):
    return a+b
sum=reduce(adding,list_3)
print(sum)

 #WITH LAMBDA
sum=reduce(lambda a,b: a+b,list_3)
print(sum)

#WRITE A PROGRAM TO FIND THE NUMBERS OF EVEN AND ODD NUMBERS IN THE LIST
list_1=[1,2,3,4,5,6,7]
list_even=list(filter(lambda n: n%2==0, list_1))
list_odd=list(filter(lambda n: n%2!=0, list_1))
print(list_even)
print(list_odd)

 
