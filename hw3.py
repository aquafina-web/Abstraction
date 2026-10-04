# abstraction
from abc import ABC ,abstractmethod
class shape(ABC):
    dim1 = ''
    dim2 = ''

    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area (self):
       pass

      

class triangle(shape):
   
    def area(self):
        area = 0.5 * self.dim1 * self.dim2 
        print("Area of triangle : ",area)   

class rectangle(shape):
     def area(self):
        area = self.dim1 * self.dim2 
        print("Area of rectangle : ",area) 

t1 = triangle(20,30)
t1.area()


