class Customer:
    def __init__(self, name, has_truck_license=False):
        self.name = name
        self.has_truck_license = has_truck_license
        self.rented_vehicle = None
        
    def display(self):
        print(self.name + " (Truck License: " + str(self.has_truck_license) + ")")
        if self.rented_vehicle:
            print(f"Currently rented vehicle: {self.rented_vehicle}")
        else:
            print("No vehicle rented yet.")

    def rent_vehicle(self, vehicle):
        # Rent a vehicle if eligible (one rental at a time)
        if self.rented_vehicle:
            print("%s already has a rented vehicle and must return it first." % self.name)
        else:
            vehicle.rent(self)

    def return_vehicle(self):
        # Return the currently rented vehicle
        if self.rented_vehicle:
            self.rented_vehicle.return_vehicle()
            self.rented_vehicle = None
        else:
            print(f"{self.name} has no vehicle to return.")
    
