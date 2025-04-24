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
        if not self.is_rented:
            self.is_rented = True
            self.rental_due_date = datetime.now().date() + timedelta(days=7)
            customer.rented_vehicle = self
            print("%s rented %s %s, due back on %s." % (customer.name, self.brand, self.model, self.rental_due_date))
        else:
            print(f"{self.brand} {self.model} is already rented.")

    def return_vehicle(self):
        # Return the vehicle and clear the due date
        if self.is_rented:
            self.is_rented = False
            self.rental_due_date = None
            print("%s %s has been returned." % (self.brand, self.model))            
        else:
            print(f"{self.brand} {self.model} is not currently rented.")

    def __str__(self):
        return "%s %s (%s)" % (self.brand, self.model, self.vehicle_type)