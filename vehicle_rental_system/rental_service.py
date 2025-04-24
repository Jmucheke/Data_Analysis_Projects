class RentalService:
    def __init__(self):
        self.vehicles = []   # To store Vehicle objects
        self.customers = []  # To store Customer objects

    def add_vehicle(self, vehicle):
        # Add a vehicle to the rental system
        self.vehicles.append(vehicle)
        print("Vehicle %s %s added to the rental service." % (vehicle.brand, vehicle.model))

    def list_available_vehicles(self):
        # List all vehicles not currently rented
        available = [v for v in self.vehicles if not v.is_rented]
        if available:
            print("Available vehicles:")
            for v in available:
                print(v)
        else:
            print("No vehicles available.")

    def add_customer(self, customer):
        # Add a customer to the system
        self.customers.append(customer)
        print("Customer %s added to the rental service." % customer.name)