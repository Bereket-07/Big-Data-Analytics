import pandas as pd
def basic_data_cleaning(df):
    print("handle missing values:")
    df.ffill(inplace=True)
    print("missing values handeled successfully")
    print("remove duplicates:")
    df.drop_duplicates(inplace=True)
    print("duplicates removed successfully")
    print("converting date column to datetime:")