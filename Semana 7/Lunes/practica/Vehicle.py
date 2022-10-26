class Vehicle:
    def __init__(self, brand, model, color, years):
        self.__brand = brand
        self.model = model
        self.color = color
        self.year = years
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,brand):
        self.__brand = brand
