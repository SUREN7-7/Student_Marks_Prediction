import logging
import os
from datetime import datetime

# A log is a record of events, messages, or errors that occur in a system or application

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"      
#LOG_FILE = "02_22_2025_14_30_45.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)     
#"C:/Users/YourName/Project/logs/02_22_2025_14_30_45.log"

os.makedirs(logs_path,exist_ok=True)
#This line creates the "logs" directory if it doesn’t already exist.
#exist_ok True denotes that it has to append even though the dir is exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


# if __name__=="__main__":
#     logging.info("Logging has started")