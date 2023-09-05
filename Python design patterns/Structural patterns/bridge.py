from abc import ABC, abstractmethod

class Device(ABC):
    volume = 0
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    

class Radio(Device):
    
    def get_name(self) -> str:
        return f"Radio {self}"
    
class TV(Device):
    
    def get_name(self) -> str:
        return f"TV {self}"
    

class Remote(ABC):
    @abstractmethod
    def volume_up(self) -> None:
        pass
    
    @abstractmethod
    def volume_down(self) -> None:
        pass
    

class BasicRemote(Remote):
    
    def __init__(self, device: Device) -> None:
        self.device = device
        
    def volume_up(self) -> None:
        self.device.volume += 1
        print(f"{self.device.get_name()} volume up {self.device.volume}")
        
    def volume_down(self) -> None:
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume down {self.device.volume}")
        
        
        
        
if __name__ == "__main__":
    radio = Radio()
    tv = TV()
    
    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)
    
    radio_remote.volume_up()
    
    tv_remote.volume_down()