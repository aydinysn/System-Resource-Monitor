import logging

def setup_logger():
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    
    file_handler = logging.FileHandler('monitor_log.txt')
    file_handler.setFormatter(formatter)
    
   
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
   
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
   
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
   
    logger.propagate = False
    
    return logger
