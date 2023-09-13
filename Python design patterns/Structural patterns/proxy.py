from abc import ABC, abstractmethod

class Image(ABC):
    
    @abstractmethod
    def display(self):
        pass
    
class RealImage(Image):
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        print(f"Real image loading {filename}")
        
    def display(self):
        print(f"Real image displaying {self.filename}", end="\n\n")
        
        
class ProxyImage(Image):
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.real_image = None
        
    def display(self):
        print(f"Proxy image displaying {self.filename}")
        
        if not self.real_image:
            print("From disk")
            self.real_image = RealImage(self.filename)
        else:
            print(f"Print from cache")
        
        self.real_image.display()
        
        
if __name__ == "__main__":
    image = ProxyImage("test.jpg")
    
    image.display()
    
    image.display()