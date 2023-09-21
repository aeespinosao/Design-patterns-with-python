from abc import ABC, abstractmethod

class Command(ABC):
    
    def __init__(self, command_id: int) -> None:
        self.command_id = command_id
        
    @abstractmethod
    def execute(self):
        pass
    

class OrderAddCommand(Command):
    
    def execute(self):
        print(f"adding order with id {self.command_id}")
        

class OrderPayCommand(Command):
    
    def execute(self):
        print(f"Paying for order with id {self.command_id}")
        

class CommandProcesor:
    queue = []
    
    def add_to_queue(self, command: Command):
        self.queue.append(command)
    
    def process_commands(self):
        [command.execute() for command in self.queue]
        self.queue = []
        
if __name__ == "__main__":
    processor = CommandProcesor()
    
    processor.add_to_queue(OrderAddCommand(1))
    processor.add_to_queue(OrderAddCommand(2))
    processor.add_to_queue(OrderPayCommand(1))
    processor.add_to_queue(OrderPayCommand(2))
    
    processor.process_commands()