class motor:
    def __init__(self, merek):
        self.merek = merek
    
class pengendara:
    def __init__(self, nama, motor):
        self.nama = nama
        self.motor = motor
    
    def info(self):
        print(f"{self.nama} mengendarai motor {self.motor.merek}")
        
a = motor("Yamaha")
b = pengendara("Wildan Fadillah", a)
b.info()