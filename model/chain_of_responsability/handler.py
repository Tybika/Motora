import paths

from abc import ABC, abstractmethod
from response import Response

class Handler(ABC):
    def __init__(self):
        self.next = None

    def set_next(self, next: object):
        self.next = next

    def new_response(self, type: str, request: object):
        response = Response()
        response.set_type(type)
        response.set_data(request.data)
        return response

    @abstractmethod
    def handle(self, request: object):
        # Handle chain or final, should be overwritten  
        if not self.next == None:
            pass
        else:
            return self.new_response()
            
