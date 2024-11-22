import logging
import os
from datetime import datetime

# Generate a unique log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory path where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists; create it if it doesn't
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log message format
    level=logging.INFO,  # Log level (INFO logs informational messages and higher levels)
)