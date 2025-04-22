class Customer:
    def __init__(self, name, has_truck_license=False):
        self.name = name
        self.has_truck_license = has_truck_license
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle):
        # Rent a vehicle if eligible (one rental at a time)
        pass

    def return_vehicle(self):
        # Return the currently rented vehicle
        pass