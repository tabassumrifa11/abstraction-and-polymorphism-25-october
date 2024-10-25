class Ferrari:
    def model(self):
        print("La Ferrari")
        
        
    def fuel_type(self):
        print("Petrol")
        
        
    def max_speed(self):
        print("Max speed is 350")
        
        
    
class BMW:
    def model(self):
        print("A8")
        
        
    def fuel_type(self):
        print("Diesel")
        
        
    def max_speed(self):
        print("Max speed is 240")
        
        
        
class Toyota:
    def model(self):
        print("RAV4")
        
        
    def fuel_type(self):
        print("Petrol")
        
        
    def max_speed(self):
        print("Max speed is 180")
        
        
        
class Nissan:
    def model(self):
        print("Nissan X-Trail")
        
        
    def fuel_type(self):
        print("Petrol")
        
        
    def max_speed(self):
        print("Max speed is 140")
        
        
        
    
class Honda:
    def model(self):
        print("CR-V")
        
        
    def fuel_type(self):
        print("Petrol")
        
        
    def max_speed(self):
        print("Max speed is 130")
        
        
        
class Hyundai:
    def model(self):
        print("Tucson")
        
        
    def fuel_type(self):
        print("Petrol")
        
        
    def max_speed(self):
        print("Max speed is 190")
        
        
        
class Audi:
    def model(self):
        print("A7")
        
        
    def fuel_type(self):
        print("Diesel")
        
        
    def max_speed(self):
        print("Max speed is 250")
        
        
        
        
ferrari = Ferrari()
bmw = BMW()
toyota = Toyota()
honda = Honda()
hyundai = Hyundai()
audi = Audi()



for car in(ferrari, bmw, toyota, honda, hyundai, audi):
    car.model()
    car.fuel_type()
    car.max_speed()
    print()