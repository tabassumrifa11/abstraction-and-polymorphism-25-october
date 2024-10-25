from abc import ABC, abstractmethod

class Absclass(ABC):
    
    def print(self,x):
        print("Passed value:", x)
        
        
    @abstractmethod
    def task(self):
        print("We are inside of Absclass task")
        
        
        
class testClass(Absclass):
    
    def task(self):
        print("We are inside of test class task")
        
        
testobj = testClass()
testobj.task()
testobj.print(100)