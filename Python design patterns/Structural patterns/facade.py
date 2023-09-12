class ComplexSystemStore:
    
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.cache = {}
        print(f"Reading data from file {filepath}")
        
    def store(self, key: str, value: str):
        self.cache[key] = value
        
    def  read(self, key: str):
        return self.cache.get(key)
    
    def commit(self):
        print(f"Storing cache data to {self.filepath}")
        
        
@dataclass
class User:
    login: str
    
# Facade
class UserRepository:
    def __init__(self) -> None:
        self.system_preferences = ComplexSystemStore("/data/default.prefs")
    
    def save(self, user: User):
        self.system_preferences.store("USER_KEY", user.login)
        self.system_preferences.commit()
        
        