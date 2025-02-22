# The sys module in Python provides functions and variables used to manipulate the Python runtime environment.
import sys
from src.logger import logging
# src is userdefined package consisting of module logger

# This func is used whenever an exception/error gets raised we can print our own message(user defined). 
# Simply we can print the error in our convinience for better understanding.
#It takes 2 parameters * error * error_detail which is basically present in 'sys' what moudle we are imported
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename #present in userdefined exception documentation, It simply returns the filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        # super() since inheriting from exception
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        # error_detail is the message occurs when an error occured in runtime hence it its 'sys'.
    
    def __str__(self):
        return self.error_message
    
    
# if __name__=="__main__":
    
#     try:
#         x=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)