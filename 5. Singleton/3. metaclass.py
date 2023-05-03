from typing import Any

class Singleton(type):
    __instances = {}
    
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
    
    
class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('loading database')
    
    
if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    print(d1 is d2)
    
    