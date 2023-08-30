from abc import ABC, abstractmethod

class FoodType:
    french=1
    american=2
    
# Abstract factory
class Restaurant(ABC):
    
    @abstractmethod
    def make_food(self):
        pass
    
    @abstractmethod
    def make_drink(self):
        pass
    
class FrenchRestaurant(Restaurant):
    
    def make_food(self):
        return "Cordon bleu"

    def make_drink(self):
        return "Merlot"
    
class AmericanRestaurant(Restaurant):
    
    def make_food(self):
        return "Hamburguer"
    
    def make_drink(self):
        return "Coca cola"
    

class RestaurantFactory:
    
    @staticmethod
    def suggest_restaurant(type: FoodType):
        if type == FoodType.french:
            return FrenchRestaurant()
        
        return AmericanRestaurant() 
    

def dine_at(restaurant: Restaurant):
    print("For dinner we are having ")
    print(restaurant.make_food())
    print(restaurant.make_drink())
    

if __name__ == "__main__":
    s1 = RestaurantFactory.suggest_restaurant(FoodType.french)
    s2 = RestaurantFactory.suggest_restaurant(FoodType.american)
    
    
    dine_at(s1)
    dine_at(s2)