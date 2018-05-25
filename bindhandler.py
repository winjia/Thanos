
class BindHandler():
    def __init__(self):
        pass

    def get(self):
        pass

    
    def post(self):
        name = self.get_argument("compname")
        phone = self.get_argument("phonenum")
        if len(name)==0:
            self.write("error")
        if len(phone)==0:
            self.write("error")
