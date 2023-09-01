from typing import Any
from threading import Thread, Lock
import time

class Singleton(type):
    _instances = {}
    _lock = Lock()
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)
                self._instances[self] =  instance
        return self._instances[self]
    
class NetworkDriver(metaclass=Singleton):
    
    def log(self):
        print(f"{self} -> {id(self)}\n")
        
        
def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

if __name__ == "__main__":
    # Single thread
    s1 = create_singleton()
    s2 = create_singleton()
    
    # Multi thread
    t1 = Thread(target=create_singleton)
    t2 = Thread(target=create_singleton)
    
    t1.start()
    t2.start()