import psutil
import platform
from logger import setup_logger
from config import load_config
from notifications import send_notification
import time

logger = setup_logger()

def start_monitoring():
    try:
        system_type = platform.system()
        config = load_config()
        logger.info(f"Monitoring started on {system_type}")
        
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            
            logger.info(f"CPU Usage: {cpu_usage}%")
            logger.info(f"Memory Usage: {memory_usage}%")
            
            if cpu_usage > config['CPU_THRESHOLD']:
                send_notification(f"Warning: High CPU usage! ({cpu_usage}%)")
            
            if memory_usage > config['MEMORY_THRESHOLD']:
                send_notification(f"Warning: High Memory usage! ({memory_usage}%)")
                
            time.sleep(config['CHECK_INTERVAL'])
            
    except Exception as e:
        logger.error(f"Monitoring failed: {str(e)}")
        send_notification("Monitoring error: " + str(e))

if __name__ == "__main__":
    logger.info("Test log message")
    start_monitoring()
