import pandas as pd

# convert the cars list to a data frame
def convert_list_to_df(cars_list):
    cars_df = pd.DataFrame(cars_list)
    return cars_df