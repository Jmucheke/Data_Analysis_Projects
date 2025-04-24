from vehicle import Vehicle


class Truck(Vehicle):
        
    def rent(self, customer):
        # Prevent renting unless the customer has a truck license
        if customer.has_truck_license:
            Vehicle.rent(self, customer)
        else:
            print(f"{customer.name} cannot rent {self.brand} {self.model} without a truck license.")