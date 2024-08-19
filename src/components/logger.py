import os
from datetime import datetime
import logging

# Create a timestamped log file name
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file_name = f"log_{timestamp}.log"

# Define the logs directory path
logs_directory = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_directory, exist_ok=True)

# Define the full path to the log file
log_file_path = os.path.join(logs_directory, log_file_name)

# Set up logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    logging.info('Starting script')
    # Your code here
    logging.info('Script completed')
