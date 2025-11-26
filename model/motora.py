import paths

from request import Request
from response import Response
from database import Database
from sanitizer import Sanitizer
from map_data import MapData
from classifier import Classifier

class Motora:
    def __init__(self):
        self.controller = None

        # Instancia handlers
        self.query = Database()
        self.sanit = Sanitizer()
        self._map = MapData()
        self.classify = Classifier()
        self.persist = Database()

        # Encadeia handlers
        self.query.set_next(self.sanit)
        self.sanit.set_next(self._map)
        self._map.set_next(self.classify)
        self.classify.set_next(self.persist)
        
    def set_controller(self, controller: object):
        self.controller = controller

    def request(self, type: str, **kwargs):
        request = Request()

        match type:
            case "create", "new", "n", "c":
                request.set_operation("c")
            case "read", "retrieve", "get", "query", "r", "g", "q":
                request.set_operation("r")
            case "update", "u":
                request.set_operation("u")
            case "delete", "erase", "d", "e":
                request.set_operation("d")
            case _:
                request = None

        #pense isso melhor, acho que args combina menlhor ou uma única variavel
        if kwargs:
            request.set_data_id(**kwargs)

        return request         

    def process(self):#, request_type: str, data, **kwargs):
        print("Processing")
        # request = self.request(request_type, **kwargs)
        # self.query.handle()

    