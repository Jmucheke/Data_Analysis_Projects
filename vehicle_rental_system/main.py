from rental_service import RentalService 
from vehicle import Vehicle
from truck import Truck
from customer import Customer

rental_service = RentalService()

# Add vehicles
car = Vehicle("Toyota", "Camry", "Car")
motorcycle = Vehicle("Honda", "CBR500R", "Motorcycle")
truck = Truck("Ford", "F-150", "Truck")
rental_service.add_vehicle(car)
rental_service.add_vehicle(motorcycle)
rental_service.add_vehicle(truck)

print("\n")

# Add customers
alice = Customer("Alice")
bob = Customer("Bob", has_truck_license=True)
rental_service.add_customer(alice)
rental_service.add_customer(bob)

print("\n")

# Renting vehicles
alice.rent_vehicle(truck)   # Should fail
bob.rent_vehicle(truck)     # Should succeed
alice.rent_vehicle(car)  # Should succeed 

print("\n")

# Returning vehicle and renting again
alice.return_vehicle()
alice.rent_vehicle(motorcycle)  # Now should succeed


# List available vehicles after operations
rental_service.list_available_vehicles()