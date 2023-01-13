from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import save_df_to_csv
from custom_modules.import_functions import import_cars
import json
from tqdm import tqdm

# take the input
from_file = input("From file? (y/N)\n").upper() or 'N'

if from_file == 'Y':

    # open the config file
    with open("config.json", "r") as file:
        config_str = file.read()
    
    # convert string to dict
    config_dict = json.loads(config_str)

    # extract the list from the dict
    brands_list = config_dict['brands']
    
    for selected_brand in tqdm(brands_list):
        print(f"Importing {selected_brand}")
        # import the cars
        cars_list = import_cars(selected_brand)

        # convert the list of cars to a pandas DataFrame
        cars_df = convert_list_to_df(cars_list)

        # export the cars data
        save_df_to_csv(selected_brand, cars_df)

        
elif from_file == 'N':
    selected_brand = input("Which brand you would like to import:\n")

    # import the cars
    cars_list = import_cars(selected_brand)

    # convert the list of cars to a pandas DataFrame
    cars_df = convert_list_to_df(cars_list)

    # export the cars data
    save_df_to_csv(selected_brand, cars_df)


