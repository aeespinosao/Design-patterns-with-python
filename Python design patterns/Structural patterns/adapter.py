from dataclasses import dataclass

# 3rd party functionality
@dataclass
class DisplayDataType:
    index: float
    data: str
    
class DisplayData:
    def __init__(self, display_data: DisplayDataType) -> None:
        self.display_data = display_data
        
    def show_data(self) -> None:
        print(f"3rd party funcionality {self.display_data.index} {self.display_data.data}")
        

@dataclass
class DatabaseDataType:
    position: int
    amount: int
    

class StoreDatabaseData:
    
    def __init__(self, database_data: DatabaseDataType) -> None:
        self.database_data = database_data
        
    def store_data(self):
        print(f"Database data stored {self.database_data.position} {self.database_data.amount}")
        
class DisplaydataAdapter(StoreDatabaseData, DisplayData):
    
    def __init__(self, data) -> None:
        self.data = data
        
    def store_data(self):
        print("call out code but use the 3rd party code")
        
        for item in self.data:
            ddt = DisplayDataType(float(item.position), str(item.amount))
            self.display_data = ddt
            self.show_data()
    
    
def generate_data():
    data = list()
    data.append(DatabaseDataType(3,2))
    data.append(DatabaseDataType(5,7))
    data.append(DatabaseDataType(1,5))
    data.append(DatabaseDataType(3,1))
    return data

if __name__ == "__main__":
    adapter = DisplaydataAdapter(generate_data())
    adapter.store_data()