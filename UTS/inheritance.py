class animal:
    def speak(self):
        return "Suara Hewan"

class cat(animal):
    def speak(self):
        return "MEONGGGGG!!!!"
    
kucing = cat()
print(kucing.speak()) 