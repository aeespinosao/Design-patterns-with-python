class NetworkService:
    
    def __init__(self, url: str = "", auth: str = "", cache: int = 0) -> None:
        self.components = {}
        
        if url:
            self.components["URL"] = url
        
        if auth:
            self.components["Authorization"] = auth
        
        if cache:
            self.components["Cache-Control"] = cache
            
    def show(self):
        print(self.components)
        
        
if __name__ == "__main__":
    s1 = NetworkService(url="google.com")
    s1.show()
    
    s2 = NetworkService(url="youtube.com", auth="abc123", cache=6000)
    s2.show()