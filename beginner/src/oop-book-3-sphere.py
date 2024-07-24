# shoa begire masahat hajm 
# volume= 3.1415*4/3*r**3
# area=3.1415*4*r**2

import math
class Sphere:
    def __init__(self,r=0):
        self.r=r
    def get_r(self):  # getting Radius
        self.r=float(input("enter r: "))

    def area(self):
        return (math.pi)*4*(self.r)**2
    
    def volume(self):
        return (math.pi)*(4/3)*(self.r)**3
    

s=Sphere()
s.get_r()
print(s.area())
print(s.volume())