# A python script to create table

import sqlalchemy as sal
import logging

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



def createDb():
    try:
        # Connecting to default 'postgres' DB to create 'RandomUserETL'
        admin_engine = sal.create_engine('postgresql+psycopg2://Shiva:1807@localhost/postgres')
        with admin_engine.connect() as connection:
            try:
                connection.execute(sal.text('CREATE DATABASE "RandomUserETL" OWNER "Shiva"'))
                print("Database 'RandomUserETL' created.")
            except Exception:
                logging.warning("Database 'RandomUserETL' may already exist.", exc_info=True)

        # connecting to the new database
        user_engine = sal.create_engine('postgresql+psycopg2://Shiva:1807@localhost/RandomUserETL')
        with user_engine.connect() as connection:
            try:
                connection.execute(sal.text(query))
                print(f"Table {i+1} created.")
            except Exception as e:
                logging.error(f"Could not create table {i+1}.", exc_info=True)
                return

    except Exception as conn_err:
        logging.error("An error occurred during database or table creation.", exc_info=True)