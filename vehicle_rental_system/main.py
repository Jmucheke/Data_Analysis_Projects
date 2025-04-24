from rental_service import RentalService 
from vehicle import Vehicle
from truck import Truck
from customer import Customer

rental_service = RentalService()

def main():
    def display_menu():
        print("Welcome to the Vehicle Rental Service!")
        print("="*40)
        print("1. Add Vehicle")
        print("2. Add Customer")
        print("3. Rent Vehicle")
        print("4. Return Vehicle")
        print("5. List Available Vehicles")
        print("6. Exit")
        
    
    def add_vehicle():
        brand = input("Enter vehicle brand: ")
        model = input("Enter vehicle model: ")
        type_ = input("Enter vehicle type (Car/Motorcycle/Truck): ")
        if type_.lower() == "truck":
            vehicle = Truck(brand, model, type_)
        else:
            vehicle = Vehicle(brand, model, type_)
        rental_service.add_vehicle(vehicle)
        
    def add_customer():
        name = input("Enter customer name: ")
        has_truck_license = input("Does the customer have a truck license? (yes/no): ").lower() == "yes"
        customer = Customer(name, has_truck_license)
        rental_service.add_customer(customer)
    
    def rent_vehicle():
        customer_name = input("Enter customer name: ")
        vehicle_model = input("Enter vehicle model to rent: ")
        customer = next((c for c in rental_service.customers if c.name == customer_name), None)
        vehicle = next((v for v in rental_service.vehicles if v.model == vehicle_model and not v.is_rented), None)
        if customer and vehicle:
            customer.rent_vehicle(vehicle)
        else:
            print("Invalid customer or vehicle.")
            
    def return_vehicle():
        customer_name = input("Enter customer name: ")
        customer = next((c for c in rental_service.customers if c.name == customer_name), None)
        if customer:
            customer.return_vehicle()
        else:
            print("Customer not found.")
            
    def list_available_vehicles():
        rental_service.list_available_vehicles()
        
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_vehicle()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            rent_vehicle()
        elif choice == "4":
            return_vehicle()
        elif choice == "5":
            list_available_vehicles()
        elif choice == "6":
            print("Exiting the Vehicle Rental Service. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    

if __name__ == "__main__":
    app = main()