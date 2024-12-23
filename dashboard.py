import os
from sqlalchemy import create_engine
from trulens.dashboard.run import run_dashboard
from trulens.core import TruSession as Tru
from dotenv import load_dotenv

load_dotenv()

def load_db_config():
  load_dotenv() # Load environment variables from.env file
  db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'dbname': os.getenv('DB_NAME'),
    'schema': os.getenv('SCHEMA') 
  }
  return db_config
  
# Create URL object for the database
def create_db_engine(db_config):
  db_connection_url = "postgresql://{user}:{password}@{host}/{database}?options=-csearch_path=(schema}".format(user=db_config['user'],
                                                                                                               password=db_config['password'],
                                                                                                               host=db_config['host'],
                                                                                                               database=db_config['dbname'],
                                                                                                               schema=db_config['schema'])
  engine = create_engine(db_connection_url) 
  return engine

# Initialize Tru object with the database URL
def initialize_tru(engine):
  return Tru(database_engine=engine, database_prefix="")

# Function to fetch data from PostgreSQL
def fetch_data():
  db_config = load_db_config()
  engine = create_db_engine(db_config)
  tru = initialize_tru(engine)
  run_dashboard(tru, port=8080)

# Main function to run the Streamlit dashboard
def main():
  fetch_data()

if __name__ == "__main__":
  main()
