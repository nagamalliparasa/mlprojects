import logging
import os 
from datetime import datetime

LOG_file=f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_file)
os.makedirs(logs_path,exist_ok=True)

LOG_file_path=os.path.join(logs_path,LOG_file)

logging.basicConfig(
    filename=LOG_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")