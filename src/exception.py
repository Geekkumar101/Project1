import sys
import logging

def error_meassage_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ## this return 3 data which is class,object and the exception traceback
    file_name=exc_tb.tb_frame.f_code.co_filename ## this will give the file name where the exception is occuring
    error_message=f"Error has occured in python script name {file_name} at line number {exc_tb.tb_lineno} error message {str(error)}"


    return error_message

class CustomException(Exception):
    def __init__(self,error_meaasage,error_detail:sys):
        super().__init__(error_meaasage)
        self.error_message=error_meassage_details(error_meaasage,error_detail=error_detail)

    def __str__(self):
        return self.error_message


    