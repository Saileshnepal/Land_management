def write_rented_land(land_id, months):
    try:
        with open("rented_lands.txt", "a") as file:
            for _ in range(months):
                file.write(land_id + "\n")
    except IOError:
        print("Error: Unable to write to file.")

def write_returned_land(land_id):
    try:
        with open("rented_lands.txt", "r") as file:
            lines = file.readlines()
        with open("rented_lands.txt", "w") as file:
            for line in lines:
                if line.strip() != land_id:
                    file.write(line)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to write to file.")
