from fastapi import HTTPException, status



class ValidError(HTTPException):

    def __init__(self, status_code = 400, detail = "No Valid Data", headers = None):
        super().__init__(
            status_code = status_code, 
            detail = detail, 
            headers = headers
            )
    
        






