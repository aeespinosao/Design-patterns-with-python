class Equipment:
    
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
        
    
class Composite:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []
        
    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self
    
    @property
    def price(self):
        return sum([item.price for item in self.items])
    
    @price.setter
    def price(self, value):
        self.price = value


if __name__ == "__main__":
    computer = Composite("PC")
    proccesor = Equipment("Proccesor", 100)
    hard_drive = Equipment("Hard drive", 400)
    
    memory = Composite("Memory")
    rom = Equipment("ROM", 700)
    ram = Equipment("RAM", 1200)
    
    memory.add(rom).add(ram)
    computer.add(hard_drive).add(proccesor).add(memory)
    
    print(computer.price)