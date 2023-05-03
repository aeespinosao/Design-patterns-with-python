class Database:
    __instance = None
    
    def __init__(self) -> None:
        print('load a database from file')
        
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
            
        return cls.__instance
    
if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    print(d1 is d2)