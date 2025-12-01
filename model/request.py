class Request:
    def __init__(self):
        self.operation = 0
        self.data = {
            "id": {},
            "data": {}
            }
        self.states = []
    
    def default_op(self):
        operations = {
            1: ["c", "n", "create", "new"],
            2: ["r", "g", "q", "read", "retrieve", "get", "query"],
            3: ["u", "update"],
            4: ["d", "e", "delete", "erase"]
        }
        return operations
    
    def set_operation(self, op_name: str | int):
        for key, values in self.default_op().items():
            if op_name == key or op_name in values:
                self.operation = key
                return True
        return False

    def set_data_id(self, data: dict):
        self.data["id"] = data
    
    def set_data_data(self, data: any):
        self.data["data"] = data

    def add_state(self, statename: str):
        self.states.append(statename)

    def is_complete(self):
        states = { 
            1: set(["sanitized", "mapped", "classfied", "stored"]),
            2: set(["presented", "listed"]),
            3: set(["sanitized", "mapped", "classfied", "stored"]),
            4: set([])
            }
        
        obj_states = set(self.states)

        for key in states:
            if key == self.operation:
                s_set = set(states[key])
                if obj_states == s_set:
                    return True
        return False