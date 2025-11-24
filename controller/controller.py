class Controller:
    def __init__(self):
        self.model = None
        self.view = None
    
    def set_model(self, model: object):
        self.model = model
    
    def set_view(self, view: object):
        self.view = view

    def test_connection(self):
        self.model.process()

    def get_general_data(self):
        return self.model.process("retrieve")
    
    def get_type_combo(self):
        return self.model.process("retrieve")
    
    def get_athlete_data(self):
        return self.model.process("retrieve")
    
    def save_data(self):
        self.model.process("new")

    def alter_data(self, data: dict):
        self.model.process("update", {"id": data.id, "data": data.data })