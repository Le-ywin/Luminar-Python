class Parent:
   
   def greeting(self): 
     
     print("hello") 
 
 
class Child(Parent): 
   
   def hello(self): 
     
     print("1 am the child") 
 
   def greeting(self): 
   
      print("key") 
   
      return super().greeting() 
 
obj1 = Child() 
 
obj1.greeting() 
 
obj1.hello() 

