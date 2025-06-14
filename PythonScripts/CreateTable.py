import sqlalchemy as sal
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
DB_NAME = os.getenv("db_name")
DB_USER = os.getenv("db_user")
DB_PASSWORD = os.getenv("db_passwd")
DB_HOST = os.getenv("db_host")

# --- Logging Setup ---
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/pipeline.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# --- Create Tables Function ---
def create_tables():
    try:
        engine_url = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
        engine = sal.create_engine(engine_url)

        create_queries = [
            """
            CREATE TABLE IF NOT EXISTS name (
                nameID SERIAL PRIMARY KEY,
                name_title VARCHAR(10),
                first_name VARCHAR(30),
                last_name VARCHAR(30)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS location (
                locationID SERIAL PRIMARY KEY,
                street_number INTEGER,
                street_name VARCHAR(30),
                city VARCHAR(30),
                state VARCHAR(30),
                country VARCHAR(30),
                postcode VARCHAR(20),
                coordinates_latitude REAL, 
                coordinates_longitude REAL,
                timezone_offset VARCHAR(10),
                timezone_description VARCHAR(50)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS login (
                uuid VARCHAR(50) PRIMARY KEY, 
                username VARCHAR(30),
                password VARCHAR(30),
                salt VARCHAR(10),
                md5 VARCHAR(100),
                sha1 VARCHAR(100),
                sha256 VARCHAR(100)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS dob (
                dobID SERIAL PRIMARY KEY,
                date TIMESTAMPTZ,
                age INTEGER
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS registered (
                registeredID SERIAL PRIMARY KEY,
                date TIMESTAMPTZ,
                age INTEGER 
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS picture (
                pictureID SERIAL PRIMARY KEY,
                large VARCHAR(255), 
                medium VARCHAR(255),
                thumbnail VARCHAR(255)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS person (
                ID SERIAL PRIMARY KEY,
                nameID INTEGER REFERENCES name(nameID),
                gender VARCHAR(7),
                locationID INTEGER REFERENCES location(locationID),
                email VARCHAR(50),
                uuid VARCHAR(50) REFERENCES login(uuid), 
                dobID INTEGER REFERENCES dob(dobID),
                registeredID INTEGER REFERENCES registered(registeredID),
                phone VARCHAR(20),
                cell VARCHAR(20),
                pictureID INTEGER REFERENCES picture(pictureID),
                nationality VARCHAR(2)
            );
            """
        ]

        with engine.begin() as conn:
            for i, query in enumerate(create_queries, 1):
                try:
                    conn.execute(sal.text(query))
                    print(f"Table {i} created successfully.")
                except Exception as e:
                    logging.error(f"Failed to create table {i}: {e}", exc_info=True)
                    print(f"Error creating table {i}. Check logs.")
        
    except Exception as conn_err:
        logging.error("Could not connect to database.", exc_info=True)
        print("Connection failed. Check credentials or database status.")

create_tables()