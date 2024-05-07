def read_lands():
    try:
        with open("available_lands.txt", "r") as file:
            lines = file.readlines()
            lands = [line.strip().split(",") for line in lines]
            return lands
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def read_rented_lands():
    try:
        with open("rented_lands.txt", "r") as file:
            lines = file.readlines()
            rented_lands = [line.strip() for line in lines]
            return rented_lands
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def find_land_by_id(land_id):
    lands = read_lands()
    for land in lands:
        if land[0] == land_id:
            return land
    return None

def find_rented_months(land_id):
    rented_lands = read_rented_lands()
    if land_id in rented_lands:
        return rented_lands.count(land_id)
    else:
        return None
