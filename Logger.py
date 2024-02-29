import logging
import datetime
import json


class CustomFormatter(logging.Formatter):
    def format(self, record):
        created_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_data = {
            "created_datetime": created_datetime,
            "level": record.levelname,
            "filename": record.filename,
            "lineno": record.lineno,
            "message": record.msg,
            "function_name": record.funcName,
            "module": record.module,
            "process_id": record.process,
            "thread_id": record.thread,
            "process_name": record.processName,
            "thread_name": record.threadName
        }
        return json.dumps(log_data)

# Configure logging with a custom formatter and write to a file
logger = logging.getLogger(__name__)
formatter = CustomFormatter()
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)  # Set the logger level to INFO

# Note: Avoid using basicConfig as it automatically configures the root logger.
# Instead, configure the logger and handlers separately as shown above.
