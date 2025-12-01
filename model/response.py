class Response:
    def __init__(self):
        self.type = ""
        self.data = {}
    
    def default_type(self):
        types = {
            True : ["success", "s"],
            False: ["error", "e"]
            }
        return types
    
    def set_type(self, type: str | bool):
        for key, values in self.default_type().items():
            if type in values or type == key:
                self.type = key
                return True
        return False

    def set_data(self, data: dict):
        self.data = data
