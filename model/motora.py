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
        self.new_responsability_chain()

    def set_controller(self, controller: object):
        self.controller = controller

    def get_options(self, group:str):
        options = {
            "sex" : ["Feminino", "Masculino"],
            "search" : ["Nome", "Sexo"]
            }

        if group in options:
            return options[group]

    def new_responsability_chain(self):
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

    def request(self, type: str, id: dict, data: list):
        request = Request()

        match type:
            case "create" | "new" | "n" | "c":
                request.set_operation(1)
                if not data:
                    request = None
                request.set_data_data(data)

            case "read" | "retrieve" | "get" | "query" | "r" | "g" | "q":
                request.set_operation(2)
                request.set_data_id(id)

            case "update" | "u":
                request.set_operation(3)
                if not id or not data:
                    request = None
                request.set_data_data(data)

            case "delete" | "erase" | "d" | "e":
                request.set_operation(4)
                if not id:
                    request = None

        if request:
            request.set_data_id(id)
        return request         

    def process(self, request_type: str, data_id: dict = None, data: list = None):
        request = self.request(request_type, data_id, data)

        # Se o request , dispara corrente
        if request:
            response = self.query.handle(request)
            print(response)
        else:
            response = Response()
            response.set_type("error")
        
        if response.type:
            return response.data
        else:
            raise Exception("só no final")
    