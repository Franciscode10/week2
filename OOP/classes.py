class Fligth:
    #Method for specify the capacity of passenger in the plane
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    #Method for adding passengers
    def add_passenger(self, passengerName):
        if self.check_capacity() > 0:
            self.passengers.append(passengerName)
            print(f"{passengerName} was added to the fligth")
        else:
            print(f"No more space in this plane!, sorry {passengerName}")

    #Method for updating the capacity when a someone buys a ticket
    def check_capacity(self):
        self.updateCapacity = self.capacity - len(self.passengers)
        return self.updateCapacity

vuelo = Fligth(6)

listPassenger = ["Fran", "Juan", "Guada", "Luz", "Pa", "Ma", "Tia", "Lita", "Nona", "Messi", "Dimaria"]

for i in listPassenger:
    vuelo.add_passenger(i)


cantidad = vuelo.capacity

if cantidad <= 0:
    print("This fligth is not avaible")
else:
    text = None
    if cantidad == 1:
        text = "the only passenger is"
    else:
        text = "they are"
    print(f"The number of passengers is: {len(vuelo.passengers)} and {text} {vuelo.passengers}.And the capacity is: {vuelo.capacity}")



