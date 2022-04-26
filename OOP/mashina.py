class Car():
    engine = False

    def __init__(self, model):
        self.model = model
        self.benzin = 100

    def engine_on(self):
        Car.engine = True
        print("Engine is on!")

    def engine_off(self):
        Car.engine = False
        print("Engine is off!")

    def go_to(self):
        if Car.engine == True:
            km = int(input("Enter the distance: "))
            if self.benzin >= km:
                self.benzin -= km
                print("Destination has been reached")
            else:
                print("The amount of petrol to pass the entered distance is low")
        else:
            print("Please turn engine on!")

    def set(self, amount):
        if self.benzin + amount >= 100:
            print(f"Full tank. {amount - (100 - self.benzin)} petrol left unused")
            self.benzin = 100
        else:
            print(f"{self.benzin + amount} Tank")

    def view_car(self):
        if Car.engine == True:
            print(f"Engine: ON\nPetrol: {self.benzin}")
        else:
            print(f"Engine: OFF\nPetrol: {self.benzin}")


moshina = Car("Lamborghini Urus")

while 0.1:
    print("\nCAR\n1. Engine on\n2. Engine off\n3. Go to ...\n4. Fill petrol\n5. View car")

    tanlov = int(input("\n>>> "))

    if tanlov == 1:
        Car.engine_on(moshina)
    elif tanlov == 2:
        Car.engine_off(moshina)
    elif tanlov == 3:
        moshina.go_to()

    if tanlov == 4:
        ammount = int(input("Amount >>> "))
        moshina.set(ammount)

    if tanlov == 5:
        Car.view_car(moshina)