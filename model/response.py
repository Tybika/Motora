class Response:
    def __init__(self):
        self.type = ""
        self.data = {}
    
    def default_type(self):
        types = {
            "1": [True, "success", "s"],
            "2": [False, "error", "e"]
            }
        return types
    
    def set_type(self, type: str):
        for key, values in self.default_type().items():
            if type in values:
                self.type = key
                return True
            
        return False

    def set_data():
        pass
