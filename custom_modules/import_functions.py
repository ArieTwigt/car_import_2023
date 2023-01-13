import requests

def import_cars(brand: str):
    '''
    Calls the API to return a list of cars
    
    '''
    brand_upper = brand.upper()
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    print("Importing car data")
    response = requests.get(endpoint)

    if response.status_code != 200:
        print("Error")

    cars_list = response.json()
    
    return cars_list