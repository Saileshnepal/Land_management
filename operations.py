import read
import write

def display_available_lands():
    lands = read.read_lands()
    print("\nAvailable Lands:")
    for land in lands:
        print(land)

def rent_land():
    try:
        land_id = input("\nEnter the ID of the land you want to rent: ")
        months = int(input("Enter the number of months you want to rent for: "))
        rented_lands = read.read_rented_lands()

        if land_id in rented_lands:
            print("Land already rented. Please choose another land.")
            return

        land = read.find_land_by_id(land_id)
        if land:
            write.write_rented_land(land_id, months)
            print("Land rented successfully.")
        else:
            print("Invalid land ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number of months.")

def return_land():
    try:
        land_id = input("\nEnter the ID of the land you want to return: ")
        months_rented = read.find_rented_months(land_id)

        if months_rented is None:
            print("Land not rented. Nothing to return.")
            return

        returned_months = int(input("Enter the number of months you rented the land for: "))
        bill = calculate_bill(months_rented, returned_months)
        write.write_returned_land(land_id)
        print("Land returned successfully.")
        print(f"Your bill amount: {bill}")
    except ValueError:
        print("Invalid input. Please enter a valid number of months.")

def calculate_bill(months_rented, returned_months):
    price_per_month = 50000
    delayed_months = max(0, returned_months - months_rented)
    total_price = returned_months * price_per_month
    fine_price = 0.1 * delayed_months * price_per_month
    return total_price + fine_price
