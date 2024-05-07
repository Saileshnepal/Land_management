import operations

def main():
    while True:
        print("\nWelcome to Land Rental System")
        print("1. Display available lands")
        print("2. Rent land(s)")
        print("3. Return land(s)")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            operations.display_available_lands()
        elif choice == '2':
            operations.rent_land()
        elif choice == '3':
            operations.return_land()
        elif choice == '4':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
