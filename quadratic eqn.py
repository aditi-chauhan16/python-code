
# wap program to calucltae the roots of the quadratic eqn

import math
def quadratic_roots(a,b,c):
    Discriminant = (b**2)-(4*a*c)
    if D >0:
        root1=(-b +math.sqrt(D))
        root2=(-a - math.sqrt(D))
        return root1, root2
    else Discriminant == 0 :
        root = -b/ (2*a)
        return root, root
print("root1", root1)
print("root2", root2) 
    


