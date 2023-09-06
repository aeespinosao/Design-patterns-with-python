from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    
    @abstractmethod
    def make_small_coffee(self):
        pass
    
    @abstractmethod
    def make_large_coffee(self):
        pass
    

class BasicCoffeeMachine(CoffeeMachine):
    
    def make_small_coffee(self):
        print("Basic machine making small coffee")
    
    def make_large_coffee(self):
        print("Basic machine making large coffee")


class EnhanceCoffeeMachine(CoffeeMachine):
    
    def __init__(self, basic_machine: BasicCoffeeMachine) -> None:
        self.basic_machine = basic_machine
        
    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()
        
    def make_large_coffee(self):
        print("Enhanced machine making large coffee")
        
    def make_milk_coffee(self):
        print("Enhanced machine making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enhanced machine adding milk")
        
        
if __name__ == "__main__":
    basic_machine = BasicCoffeeMachine()
    enhance_machine = EnhanceCoffeeMachine(basic_machine)
    
    enhance_machine.make_small_coffee()
    print()
    enhance_machine.make_large_coffee()
    print()
    enhance_machine.make_milk_coffee()
        
