class MyCalculator:
    #addfunction 
    def add( self ,a , b):
        return a + b
    
    #subfunction
    def sub( self ,a , b):
        return a - b
    
    #mulfuntion
    def mul(self , a , b):
        return a * b
    
    #divfunction
    def div(self , a , b):
        if b == 0:
            print("Cannot divide by zero")
        return a / b
        
        #modulusfunction
    def mod(self , a , b):
            if b == 0:
                print("Cannot divide by zero")
            return a % b 
            
            #floorfunction
    def floor(self , a ,b):
              if b == 0:
                    print("Cannot divide by zero")
              return a // b
        
        #powerfunction
    def power(self , a ,b):
         return a**b
            
    
    #object Creation
calc = MyCalculator()
print( "Addition:" , calc.add(5,10))
print( "Subtract:" ,calc.sub(20,10))
print( "multiply:" , calc.mul(2 , 4))
print( "Divide:" , calc.div(2,10))
print("Modulus:" , calc.mod(5,10))
print("Floor Divide:" , calc.floor(5,10))
print("Power:" , calc.power(2,5))







