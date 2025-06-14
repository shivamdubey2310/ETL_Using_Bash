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
    """
        helper function for separating Data from raw_data.csv
    
    params:
    ------
        
        df : raw_data.csv dataframe
        table_name : name of the table 
        mapDict : col names and indices to fetch them

    """

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
            {"ID": None, 
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
            "dobID": None,
            "date": 22,
            "age": 23
        },

        "registered": {
            "registeredID": None,
            "date": 24,
            "age": 25
        },

        "picture": {
            "pictureID": None,
            "large": 30,
            "medium": 31,
            "thumbnail": 32
        }
    }
    
    for table_name, col_names in table_col_map.items():
        separatingData2(df, table_name, col_names)

    # separatingData2(df, list(table_col_map.keys())[0], table_col_map.get("dob"))
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------


def removingDuplicatesAndGeneratingSerials(table_names):
    """
        a function to remove duplicates and generate serials for columns with all NaN values,
        or for columns ending with 'ID' that contain any NaN values.
    """

    for table in table_names:
        file_name = f"data/{table}_raw.csv"
        try:
            # Reading the file in read mode
            with open(file_name, "r") as fileReader:
                df = pd.read_csv(fileReader)
                df.drop_duplicates(inplace=True)  # Removing duplicates

                for col in df.columns:
                    # Generate serials if all values are NaN, or if column name ends with 'ID' and there are any NaN values
                    if df[col].isna().all() or (col.lower().endswith('id') and df[col].isna().any()):
                        df[col] = list(range(1, len(df[col]) + 1))

            # Writing the cleaned DataFrame back to the file
            with open(file_name, "w") as fileWriter:
                df.to_csv(fileWriter, index=False)

        except Exception as e:
            logging.error(f"Error in opening file {file_name}: {e}")
        
    

# ---------------------------------------------------------------------------------------------

def transform():
    logging.info("Inside the transform function")
    
    table_names = ['person', 'name', 'location', 'login', 'dob', 'registered', 'picture']
    
    # separatingData()
    logging.info("Completed separating Data")
    
    # removingDuplicatesAndGeneratingSerials(table_names)
    logging.info("Completed duplicate removal and serial generation Data")

transform()