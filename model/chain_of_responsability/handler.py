from abc import ABC, abstractmethod
from response import Response

class Handler(ABC):
    def __init__(self):
        self.next = None
    
    # Return True if data is an object
    def check_type(self, data: any):
        if type(data) == object:
            return True
        else:
            raise TypeError

    def set_next(self, next: object):
        if self.check_type(next):
            self.next = next

    def new_response(self, type: str, request: object):
        response = Response()
        response.set_type(type)
        response.set_data(request.data)
        return response

    @abstractmethod
    def handle(self, request: object):
        if self.check_type(request):
            # Handle chain or final, should be overwritten  
            if not self.next == None:
                pass
            else:
                return self.new_response()
        else:
            raise TypeError
            
