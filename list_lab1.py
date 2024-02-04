list1=[] #EMPTY LIST
print(type(list1)) #TYPE OF LIST
list2=[10,30,60] #LIST OF INT
list3=[10.6,10.8,50.6]#LIST OF FLOAT NUMBERS
list4=['one','two','three'] #LIST OF STRINGS
list5=[31,'ram',[50,11],['adi']] #NESTED LOOPS
print(len(list2)) #LENGTH OF LIST

#LIST INDEXING
print(list2[1]) #RETREIVE FIRST ELEMENT OF LIST
print(list5[0],[0]) #NESTED INDEXING
print(list4[-1]) #LAST ITEM OF LIST

#LIST SLICING
list=['hey','bye','one','six','three']
print(list[0:3])
print(list[:4])
print(list[:]) #returns whole list
print(list[-2:])#return last 2 list

#ADDING INTO LIST
list.append('yo')
print(list)

list.insert(1,'yup')
print(list) #ADD ITEM AT INDEX LOCATION 1

#REMOVING FROM LIST
list.remove('hey')
print(list)

list.pop()#REMOVE LAST ITEM OF THE LIST
print(list)

list.pop(1) #REMOVE ITEM AT IDEX LOCATION 1
print(list)

del list[2] #REMOVE ITEM AT INDEX LOCATION 2
print(list)

#CHANGING VALUE OF THE STRING
list[0]=1
list[1]=2
print(list)

#DELETE ALL ITEMS IN THE LIST
list.clear()
print(list)

del list
print(list)

#COPY LIST
mylist=['one','two','three','four','five','six']
mylist1=mylist #CREATE A NEW REFRENCE "MYLIST1"
print(mylist1)

print(id(mylist)) #ADDRESS OF BOTH MYLIST AND MYLIST1 WILL BE SAME
print(id(mylist1))

mylist2=mylist.copy()  #CREATES COPY OF LIST
print(id(mylist2)) #ADDRESS OF MYLIST2 WILL BE DIFFERENT FROM MYLIST 

mylist[0]=1
print(mylist)
print(mylist1) #MYLIST1 WILL BE ALSO IMPACTED AS IT IS POINTING TO THE SAME LIST
print(mylist2) #COPY OF LIST WONT BE AFFECTED BY THE CHANGES

#JOIN LIST
mylist=['one','two','three','four','five']
mylist1=['six','seven','eight','nine']
list3=mylist+mylist1
print(list3)

mylist.extend(mylist1) #APPEND MYLIST1 WITH MYLIST
print(mylist)

#LIST MEMBERSHIP
print('one' in mylist) #CHECK IF 'ONE' EXIST IN THE LIST

if 'one' in mylist:
    print('one is present')
else:
    print('one is not there')
    
#REVERSE LIST
mylist.reverse()
print(mylist)

mylist=mylist[::2]
print(mylist) #PRINT EVEN INDEXES INCLUDING ZERO INDEXES

#SORT LIST
asc=[1,3,2,8,9]
asc.sort() #SORT LIST IN ASCENDING ORDER
print(asc)

asc.sort(reverse=True) #SORT LIST IN DESCENDING ORDER
print(asc)

sorting=[22,43,12,54,67]
print(sorted(sorting)) #RETURNS A NEW SORTED LIST WITHOUT CHANGING ORIGINAL LIST
print(sorting)

#LOOP THROUGH A LIST
list=['one','two','three','four','five']
for i in list:
    print(i)
    
for i in enumerate(list): #PRINT WITH INDEX LOCATION
    print(i)

#WRITE A PYTHON PROGRAM TO SWAP LAST AND FIRST ELEMENT OF LIST
SWAP=['One','two','three','four','five']
a=SWAP[0]
SWAP[0]=SWAP[4]
SWAP[4]=a
print(SWAP)





