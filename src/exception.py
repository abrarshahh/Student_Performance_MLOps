import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message including the filename, line number, and error description.

    Parameters:
    error: The exception object that was raised.
    error_detail (sys): The sys module passed for retrieving exception details.

    Returns:
    str: A formatted string containing error details.
    """
    
    # Extract traceback object from the exception details
    _, _, exe_tb = error_detail.exc_info()

    # Retrieve the filename where the error occurred
    file_name = exe_tb.tb_frame.f_code.co_filename

    # Retrieve the line number where the error occurred
    line_no = exe_tb.tb_lineno

    # Format the error message with file name, line number, and error details
    error_message = (
        f"Error occurred in the Python script: {file_name}\n"
        f"Line number: {line_no}\n"
        f"Error message: {str(error)}"
    )

    return error_message

class CustomException(Exception):
    """
    A custom exception class that provides detailed error messages.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with detailed error information.

        Parameters:
        error_message: The original error message.
        error_detail (sys): The sys module passed for retrieving exception details.
        """
        
        # Initialize the base class (Exception)
        super().__init__(error_message)
        
        # Store a detailed error message using the helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the detailed error message when the exception is printed or logged.

        Returns:
        str: The detailed error message.
        """
        
        return self.error_message