import pandas as pd
import logging
import json

from dotenv import load_dotenv
load_dotenv()


# Customizing logging.basicConfig() to format logging 
logging.basicConfig(
    level = logging.DEBUG,
    filename = "logs/pipeline.log",
    encoding = "utf-8",
    filemode = "a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# ------------------------------------------------------------------------------------------------------------------
 
def separatingData2(df, table_name, mapDict):
    
    dictForDf = {}

    for col_name, col_index in mapDict.items():
        if col_index is not None and 0 <= col_index < df.shape[1]:
            dictForDf[col_name] = df.iloc[:, col_index]
        else:
            dictForDf[col_name] = pd.Series([None] * len(df))

    newDf = pd.DataFrame(dictForDf)

    # Saving tableData
    file_name = f"data/{table_name}_raw.csv"
    try:
        with open(file_name, "w") as fileWriter:
            newDf.to_csv(fileWriter, index=False)
    except Exception as e:
        logging.error(f"Error writing {table_name}_raw.csv : {e}")

# ---------------------------------------------------------------------------

def separatingData():
    """
        Separating raw data in different files.
    """

    logging.info("Inside the separatingData function")
    fileName = "data/raw_data.csv"
    
    try:
        with open(fileName, "r") as file:
            df = pd.read_csv(file)

    except Exception as e:
        logging.error(f"An exception occurred : {e}")
        print(f"An exception occurred : {e}")


    table_col_map = {
        "person":
            {"id_name": 28, 
             "id_value": 29, 
             "nameID": None, 
             "gender": 0, 
             "locationID": None, 
             "email": 14, 
             "uuid": 15, 
             "dobID": None, 
             "registeredID": None, 
             "phone": 26, 
             "cell": 27, 
             "pictureID": None, 
             "nationality": 33
            },

        "name": {
            "nameID": None,
            "name_title": 1,
            "first_name": 2,
            "last_name": 3
        },

        "location": {
            "locationID": None,
            "street_number": 4,
            "street_name": 5,
            "city": 6,
            "state": 7,
            "country": 8,
            "postcode": 9,
            "coordinates_latitude": 10,
            "coordinates_longitude": 11,
            "timezone_offset": 12,
            "timezone_description": 13
        },

        "login": {
            "uuid": 15,
            "username": 16,
            "password": 17,
            "salt": 18,
            "md5": 19,
            "sha1": 20,
            "sha256": 21,
        },

        "dob": {
            "date": 22,
            "age": 23
        },

        "registered": {
            "date": 24,
            "age": 25
        },

        "picture": {
            "large": 30,
            "medium": 31,
            "thumbnail": 32
        }
    }
    
    for table_name, col_names in table_col_map.items():
        separatingData2(df, table_name, col_names)

    # separatingData2(df, list(table_col_map.keys())[0], table_col_map.get("dob"))
# ---------------------------------------------------------------------------


def transform():
    logging.info("Inside the transform function")
    separatingData()
    

transform()