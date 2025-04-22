from datetime import datetime, timedelta  

class Vehicle:
    def __init__(self, brand, model, vehicle_type):
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.is_rented = False
        self.rental_due_date = None

    def rent(self, customer):
        # Allow a customer to rent the vehicle if available
        pass

    def return_vehicle(self):
        # Return the vehicle and clear the due date
        pass

    def __str__(self):
        return "%s %s (%s)" % (self.brand, self.model, self.vehicle_type)