from __future__ import annotations
from abc import ABC, abstractmethod

class HandlerChain(ABC):
    
    def __init__(self, input_header: HandlerChain) -> None:
        self.next_header = input_header
        
    @abstractmethod
    def add_header(self, input_header: str):
        pass

    def do_next(self, input_header: str):
        if self.next_header:
            return self.next_header.add_header(input_header)
        
        return input_header
    

class AuthenticationHeader(HandlerChain):
     
    def __init__(self, token: str, next_header: HandlerChain = None) -> None:
        super().__init__(next_header)
        self.token = token
    
    def add_header(self, input_header: str):
        h = f"{input_header}\nAuthorization: {self.token}"
        return self.do_next(h)

class ContentTypeHeader(HandlerChain):
    
    def __init__(self, content_type: str, next_header: HandlerChain = None) -> None:
        super().__init__(next_header)
        self.content_type = content_type 
    
    def add_header(self, input_header: str):
        h = f"{input_header}\nContentType: {self.content_type}"
        return self.do_next(h)
    
class BodyPayloadHeader(HandlerChain):
    
    def __init__(self, body: str, next_header: HandlerChain = None) -> None:
        super().__init__(next_header)
        self.body = body 
        
    def add_header(self, input_header: str):
        h = f"{input_header}\n{self.body}"
        return self.do_next(h)
    
    
if __name__ == "__main__":
    authentication_header = AuthenticationHeader("12345")
    content_type_header = ContentTypeHeader("json")
    body_header = BodyPayloadHeader("{'a':'b'}")
    
    authentication_header.next_header = content_type_header
    content_type_header.next_header = body_header
    
    message_with_auth = authentication_header.add_header("test with auth")
    message_without_auth = content_type_header.add_header("test without auth")
    
    print(message_with_auth)
    print()
    print(message_without_auth)