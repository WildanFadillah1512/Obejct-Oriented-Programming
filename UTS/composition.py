class Engine:
    def start(self):
        return "mesin menyala"

class car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        return self.engine.start()
    
mobil = car()
print(mobil.start())