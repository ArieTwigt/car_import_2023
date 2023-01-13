import os
import pandas as pd

# export the data
def save_df_to_csv(selected_brand: str, cars_df: pd.DataFrame) -> None:
    '''
    Exports a Pandas DataFrame to disk

    parameters:
    * brand
    * cars_df
    
    
    '''
    brand_folder = selected_brand
    file_name = selected_brand

    # create the subfolder for the particular brand
    os.makedirs(f"export/{brand_folder}", exist_ok=True)

    # export the csv to the folder
    print("Exporting")
    
    folder_file_name = f"export/{brand_folder}/{file_name}.csv"
    cars_df.to_csv(folder_file_name,
                sep=";",
                index=False)

    print(f"✅ Succesfully exported to {folder_file_name}")