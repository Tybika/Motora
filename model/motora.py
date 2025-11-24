from request import Request
from response import Response

class Motora:
    def __init__(self):
        self.controller = None

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

    