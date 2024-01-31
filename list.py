#STRING INTO LIST
'''str1="hello"
list1=[i for i in str1]
print(list1)

#PRINT LIST OF EVEN NUMBERS TILL 41
number=[]
for i in range(41):
    if i%2== 0:
        number.append(i)
print(number)

#CONCATENATION OF STRING
str1='hello'
abc=input("enter another string:")
str1+=abc
print(str1)
print(id(str1))'''

'''#TO CREATE A DICTIONARY
dict={'date':'16/2/2005','name':'adi','course':'btech'}
print("dict[date]=",dict['date'])
print("dict[name]=",dict['name'])
print("dict[course]=",dict['course'])'''

#WAP TO APPEND THE NUMBERS IN THE LIST AND PRINT EVERY NUMBER THAT IS EVEN OR ODD

number=[]
for i in range(50):
    number.append(i)
    if i%2== 0:
     print('number is even')
     
    else:
     print('number is odd')
     
#WAP  TO EXTRACT LETTERS FROM STRING AND PUT IN A STRING
str1="hello"
list1=[i for i in str1]
print(list1)  
#CREATE A TUPLE WHICH CONSIST OF 10 VALUES AND PRINT ALL OF THEM USING VALUES

int=(10,20,30,1,5,6,7,8,9,10)
for i in int:
   print(i)
