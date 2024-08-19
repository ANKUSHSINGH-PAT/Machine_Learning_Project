import sys
from logger import logging

def error_message_detail(error, error_detail: sys):
    exc_tb = error_detail.exc_info()[2]  # Get the traceback object
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in file: {filename}, line number: {line_number}, "
        f"error message: {str(error)}"
    )
    return error_message


class CustomError(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
         
if __name__ == "__main__":
    try:
        n=1/0
    except Exception as e:
        logging.info(f"Exception occurred while running: {e}")
        raise CustomError(e,sys)

    
