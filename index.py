# Base Class 
class Vehicle:
    def __init__(self, brand , model, year):
        self.__brand = brand  # Private attribute         
        self.__model = model  # Private attribute 
        self.__year = year    # Private attribute   

    # Getter method
    def get_brand(self):
        return self.__brand

    # Setter method
    def set_brand(self , brand):
         self.__brand = brand
         
         # Getter method
    def get_model(self):
        return self.__model
    
     # Setter method
    def set_model(self , model):
         self.__model = model
    
    # Getter method
    def get_year(self):
        return self.__year
    
     # Setter method
    def set_year(self , year):
         self.__year = year 
         
         #polymorp
    def display_details(self):
        print(f"Brand: {self.__brand}, Model: {self.__model} , Year:{self.__year}")
        
        #child class
        class Car(Vehicle):
            def __init__(self, brand , model , year, doors):
                super().__init__(brand, model, year)
                self.__doors = doors
                
                #polymorphsim
                def display_details(self):
                    super().display_details()
                    print(f"Doors: {self.__doors}")
                    
                    #encapsulation
                    def get_doors(self):
                        return self.__doors
                    
                    def set_doors(self, doors):
                     self.__doors = doors
                     
                     #define another child class
                     class Bike(Vehicle):
                         def __init__(self,brand,model,year,engine_capacity):
                             super().__init__(brand , model,year)
                             self.__engine_capacity = engine_capacity
                             
                             def display_details(self):
                                 super().display_details()
                                 print(f"Engine Capacity: {self.__engine_capacity}")
                                 
                                 #encapsulation getter and setter method
                                 def get_engine_capacity(self):
                                     return self.__engine_capacity
                                 
                                 def set_engine_capacity(self, engine_capacity):
                                     self.__engine_capacity = engine_capacity
                                     
                                     car = Car("Toyata" , "Corolla" , 2023 , 4)
                                     car.display_details()
                                     
                                     bike = Bike("Honda" , "CBR00R" , 2022, 500)
                                     bike.display_details()
                                       
                                     
                     
                    
            
            
            
            
            
            
            
            
            
            
            
             