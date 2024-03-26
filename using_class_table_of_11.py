#WRITE A CLASS WHICH TAKES A NUMBER 11 AND THEN PRINTS THE NUMBER WHICH IS DIVISIBLE BY 11
class divisiblebyeleven:
    def __init__(self,n):
        self.n=n
    def generate_divisible_by_eleven(self):
       for num in range(self.n+1):
           if num%11==0:
               print(num)

dbs=divisiblebyeleven(100)
dbs.generate_divisible_by_eleven()
