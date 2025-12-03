class Controller:
    def __init__(self):
        self.model = None
        self.view = None
    
    def set_model(self, model: object):
        self.model = model
    
    def set_view(self, view: object):
        self.view = view

    def get_general_data(self):
        response = self.model.process("retrieve")
        if not type(response) == bool:
            return response
        else: 
            self.view.alert()
    
    def get_plot_data(self):
        response = self.model.process("retrieve", data_id={"plot": ''})

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()
    
    def get_metadata(self):
        response = self.model.process("retrieve", data_id={"meta": ''})

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()

    def get_search_options(self):
        response = self.model.get_options("search")

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()
    
    def get_sex_options(self):
        response = self.model.get_options("sex")

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()
    
    def get_athlete_data(self, identifier: dict = None):
        response = self.model.process("query", data_id=identifier)

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()
    
    def save_data(self, data):
        response = self.model.process("create", data=data)
        if not type(response) == bool:
            return response
        else: 
            self.view.alert()

    def alter_data(self, data: dict):
        response = self.model.process("update", {"id": data.id, "data": data.data })

        if not type(response) == bool:
            return response
        else: 
            self.view.alert()