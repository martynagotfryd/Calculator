import json
import os
from pymongo import MongoClient

DB_DIR = 'db'
DB_FILE = 'data.json'

# MongoDB connection
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)  # Update with correct MongoDB URI
db = client['calculator_database']
collection = db['calculation_history']

# Function to check if the database location and file exist
def check_database_existence():
    if os.path.exists(DB_DIR) and os.path.isfile(os.path.join(DB_DIR, DB_FILE)):
        # Check if file is not empty
        if os.path.getsize(os.path.join(DB_DIR, DB_FILE)) > 0:
            return True
    return False

# Function to read data from JSON file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to write data to JSON file
def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Function to store game result in MongoDB
def store_history(number1, number2, operation, result):
    collection.insert_one({'number1': number1, 'number2': number2, 'operation': operation, 'result': result})


# Function to initialize the database with JSON data
def initialize_database_from_file(filename):
    if check_database_existence():
        data = read_data_from_file(filename)
        if data:  # Check if data is not empty
            for doc in data:
                if '_id' in doc:
                    del doc['_id']  # Remove the _id field to avoid duplicate key errors
            collection.insert_many(data)

# Function to convert MongoDB documents to JSON-serializable format
def convert_to_json_serializable(documents):
    for doc in documents:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return documents

# Function to dump data to JSON upon application closure
def dump_data_to_file(filename):
    data = list(collection.find())
    data = convert_to_json_serializable(data)  # Convert MongoDB documents to JSON-serializable format
    write_data_to_file(data, filename)

# Function to initialize the database
def initialize_database():
    if not check_database_existence():
        # Create database directory if it doesn't exist
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)
        # Create empty data file
        with open(os.path.join(DB_DIR, DB_FILE), 'w') as file:
            json.dump([], file)
    else:
        initialize_database_from_file(os.path.join(DB_DIR, DB_FILE))

# Function to handle end of session update
def end_session_update(number1, number2, operation, result):
    # Store game result in MongoDB
    store_history(number1, number2, operation, result)
    # Dump data to JSON file
    dump_data_to_file(os.path.join(DB_DIR, DB_FILE))