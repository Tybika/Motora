import paths
from handler import Handler
from pymongo import MongoClient

class Database(Handler):
    def __init__(self):
        super.__init__()
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)
        self.database = self.client["motora"]
        self.athletes = self.database["athletes"]

    def get_athletes(self, resquest_data=None):
        if resquest_data:
            return self.athletes.find({resquest_data.id: resquest_data.id})
        else:
            return self.athletes.find({})
    
    def get_vectors(self):
        return self.athletes.find({}, {'_id': 0, 'vector': 1})
    
    def get_classifieds(self):
        pass

    def update_document(self, request_data):
        identifier = request_data.id.items()
        data = request_data.data.items()
        filter = {identifier[0] : identifier[1]}
        update = {'$set' : {}}
        
        self.athletes.update_one(filter, update)

    def new_document(self, data: dict):
        self.athletes.insert_one({})

    def handle(self, request):
        if self.check_type(request):
            if not self.next == None:
                # agir no request e chamar o próximo 
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
for item in algo.items(): 
    print(item[1].items())