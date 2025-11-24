import paths
from handler import Handler
from pymongo import MongoClient

class Database(Handler):
    def __init__(self):
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)
        self.database = self.client["test_db"]
        self.athletes = self.database["athletes"]

    def get_athletes(self, criteria: str = None, data: str = None):
        if criteria and data:
            return self.athletes.find({criteria: data})
        else:
            return self.athletes.find({})
    
    def get_vectors(self):
        return self.athletes.find({}, {'_id': 0, 'vector': 1})
    
    def gen_vector(self):
        pass

    def update_document(self, request_data):
        identifier = request_data.id.items()
        data = request_data.data.items()
        filter = {identifier[0] : identifier[1]}
        update = {'$set' : {}}
        
        self.athletes.update_one(filter, update)

    def handle(self, request):
        if self.check_type(request):
            if not self.next == None:
                # retornar 
                pass
            else:
                return self.new_response()
        else:
            raise TypeError
        
algo = {'data': {
        'id': {'name': 'charlota'},
        'data': {'stature': 162, 
                 'name' : 'carlota'}
}}
print(algo.items())