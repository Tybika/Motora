class Request:
    def __init__(self):
        self.operation = ""
        self.data = {
            "id": {},
            "data": {}
            }
        self.author
        self.states = []
    
    def default_op(self):
        operations = {
            1: "create",
            2: "query",
            3: "update",
            4: ["d", "e", "delete", "erase"]
        }
        return operations
    
    def set_operation(self, op_name: str | int):
        for key, values in self.default_op().items():
            if op_name == key or op_name in values:
                self.operation = key
                return True
        return False

    def set_data_id(self, data: any):
        self.data["id"] = data
        
    def get_data(self):
        return self.data['data']

    def addstate(statename):
        pass
