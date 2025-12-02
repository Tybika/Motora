import paths
from handler import Handler

class MapData(Handler):
    def data_structure(self):
        return ({"name": "",
                "age": 0,
                "sex": 0,
                "weigth": 0,
                "heigth": 0,
                "flex": 0,
                "cardio": 0,
                "vector": 0
                })

    def drop_empty(self, data: dict):
        drops = []
        for key in data:
            if not key == "sex" and data[key] == 0:
                drops.append(key)

        for e in drops:
            data.pop(e)

    def handle(self, request):
        try:
            data = request.data["data"]

            if request.operation == 1 or request.operation == 3:
                mapped = self.data_structure()

                if type(data) == list:
                    mapped["name"] = data[0]
                    mapped["age"] = data[1]
                    mapped["sex"] = data[2]
                    mapped["weigth"] = data[3]
                    mapped["heigth"] = data[4]
                    mapped["flex"] = data[5]
                    mapped["cardio"] = data[6]
                    mapped["vector"] = data[1:]

                elif type(data) == dict:
                    vector = [0, 0, 0, 0, 0, 0]
                    for key in data:
                        match key:
                            case "name":
                                mapped["name"] = data[key]
                            case "age": 
                                mapped["age"] = data[key]
                                vector[0] = data[key]
                            case "sex":
                                mapped["sex"] = data[key]
                                vector[1] = data[key]
                            case "weigth": 
                                mapped["weigth"] = data[key]
                                vector[2] = data[key]
                            case "heigth": 
                                mapped["heigth"] = data[key]
                                vector[3] = data[key]
                            case "flex":
                                mapped["flex"] = data[key]
                                vector[4] = data[key]
                            case "cardio":
                                mapped["cardio"] = data[key]
                                vector[5] = data[key]
                            case _:
                                pass
                            
                    mapped["vector"] = data            
                
                self.drop_empty(mapped)
                request.set_data_data(mapped)
                request.add_state("mapped")

            elif request.operation == 2:
                _list = []

                if "count" in data:
                    _list = [document["count"], document["last"]]

                elif type(data) == dict:
                    _list = [
                        document["name"], document["age"], document["sex"], 
                        document["weigth"], document["heigth"], 
                        document["class-flex"], document["class-cardio"]
                        ]

                else:
                    for document in data:
                        _list.append([
                            document["name"], document["age"], document["sex"], 
                            document["weigth"], document["heigth"], 
                            document["class-flex"], document["class-cardio"]
                            ])
                
                request.data["data"] = _list
                request.add_state("listed")

            if self.next and not request.is_complete():
                return self.next.handle(request)
            else:
                return self.new_response("success", request)
        
        except Exception as e:
            print(e)
            return self.new_response("error", request)