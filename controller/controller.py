class Controller:
    def __init__(self):
        self.model = None
        self.view = None
    
    def set_model(self, model: object):
        self.model = model
    
    def set_view(self, view: object):
        self.view = view

    def test_connection(self):
        print("NEW:", self.model.process("n", data=["Mimi", "59", "Feminino", "49,7", "1,5", "-16,8", "452"]))
        print("READ:",self.model.process('r'))
        print("UPDATE:",self.model.process('u', data_id={'name': "Mimi"}, data=["Mimizinha", "", "", "", "", "", ""]))
        print("READ2:",self.model.process('r'))

    def get_general_data(self):
        return self.model.process("retrieve")
    
    def get_search_options(self):
        return self.model.get_options("search")
    
    def get_sex_options(self):
        return self.model.get_options("sex")
    
    def get_athlete_data(self, identifier: dict = None):
        return self.model.process("query", data_id=identifier)
    
    def save_data(self, data):
        self.model.process("create", data=data)

    def alter_data(self, data: dict):
        self.model.process("update", {"id": data.id, "data": data.data })