import paths
from handler import Handler
from pymongo import MongoClient
from bson.objectid import ObjectId

class Database(Handler):
    def __init__(self):
        super().__init__()
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)
        self.database = self.client["motora"]
        self.athletes = self.database["athletes"]

    def get_athletes(self, request_data):
        if not request_data["id"]:
            return list(self.athletes.find({}, {'_id': 0}))  
        else:
            return self.athletes.find_one(request_data["id"])
    
    def get_meta(self):
        meta = {"count": 0, "last": ""}
        meta["count"] = self.athletes.countDocuments(self.athletes.find({}))

        # Utiliza o kwarg sort ao invés do filtro usando documento {}
        latest = self.athletes.find_one(sort=["_id", -1])

        meta["last"] = latest["_id"].generation_time
        return meta


    def update_document(self, request_data):
        filter = request_data["id"]
        update = {"$set" : request_data["data"]}
        self.athletes.update_one(filter, update)

    def new_document(self, request_data: dict):
        self.athletes.insert_one(request_data["data"])
    
    def del_document(self, request_data: dict):
        self.athletes.delete_one(request_data["id"])

    def handle(self, request):
        try:
            op = request.operation

            if op == 1 and "classfied" in request.states:
                self.new_document(request.data)
                request.add_state("stored")

            elif op == 2:
                if "meta" in request.id:
                    request.set_data_data(self.get_meta())
                else:
                    request.set_data_data(self.get_athletes(request.data))

            elif op == 3 and "classfied" in request.states:
                self.update_document(request.data)
                request.add_state("stored")

            elif op == 4:
                self.del_document(request.data)

            if self.next and not request.is_complete():
                self.next.handle(request)
            else:
                return self.new_response("success", request)
            
        except Exception as e:
            print(e)
            return self.new_response("error", request)