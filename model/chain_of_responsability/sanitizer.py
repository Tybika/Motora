import paths
from datetime import datetime, timezone, timedelta
from handler import Handler
from request import Request

class Sanitizer(Handler):
    def sanit_name(self, name:str):
        no_space = name
        no_space.strip()

        if no_space.isalpha():
            return name.title()
        
        return 0

    def sanit_num(self, number: str, isdecimal = False):
        if isdecimal and len(number) > 0:
            number = number.replace(",", ".")

        if number.isnumeric() or (isdecimal and len(number) > 0):
            if isdecimal:
                return round(float(number), 2)
            return int(number)
        
        return 0

    def sanit_sex(self, sex: str):
        sex.lower()
        if sex == "feminino":
            return 1
        return 0
    
    def present_date(self, date: datetime):
        _date = date.astimezone(timezone(timedelta(hours=-3)))
        _date = _date.strftime("%d/%m/%Y")
        return _date

    
    def present_num(self, number: int | float):
        return str(number).replace(".", ",")
    
    def present_sex(self, sex: int):
        if sex == 1:
            return("Feminino")
        return("Masculino")
    
    def present_class(self, _class: int):
        match _class:
            case 0:
                return ("Muito Fraco")
            case 1:
                return ("Fraco")
            case 2:
                return ("Razoável")
            case 3:
                return ("Bom")
            case 4:
                return ("Muito Bom")
            case 5:
                return ("Excelente")

    def handle(self, request):
        try:
            data = request.data["data"]
            
            if request.operation == 1 or request.operation == 3:
                id = request.data["id"]
                if id and "name" in id:
                    id["name"] = self.sanit_name(id["name"])
                if id and "sex" in id:
                    id["sex"] = self.sanit_name(id["sex"])


                if type(data) == dict:
                    for key in data:
                        match key:
                            case "name":
                                data[key] = self.sanit_name(data[key])
                            case "age" | "cardio":
                                data[key] = self.sanit_num(data[key])
                            case "weigth" | "heigth" | "flex":
                                data[key] = self.sanit_num(data[key], True)
                            case "sex":
                                data[key] = self.sanit_sex(data[key])

                if type(data) == list:
                    data[0] = self.sanit_name(data[0])
                    data[1] = self.sanit_num(data[1])
                    data[2] = self.sanit_sex(data[2])
                    data[3] = self.sanit_num(data[3], True)
                    data[4] = self.sanit_num(data[4], True)
                    data[5] = self.sanit_num(data[5], True)
                    data[6] = self.sanit_num(data[6], True)

                print("sanitized:", data)
                request.add_state("sanitized")

            elif request.operation == 2:
                for result in data:
                    for key in result:
                        match key:
                            case "count":
                                result[key] = self.present_num(result[key])
                            case "latest":
                                result[key] = self.present_date(result[key])
                            case "age" | "cardio" | "weigth" | "heigth" | "flex":
                                result[key] = self.present_num(result[key])
                            case "sex":
                                result[key] = self.present_sex(result[key])
                            case "class-flex" | "class-cardio":
                                result[key] = self.present_class(result[key])

                request.add_state("presented")

            if self.next and not request.is_complete():
                self.next.handle(request)
            else:
                return self.new_response("success", request)
            
        except Exception as e:
            print(e)
            return self.new_response("error", request)