from fastapi import HTTPException, status




class AuthenticationError(HTTPException):

    def __init__(self, status_code, detail = "Error Authentication"):
        super().__init__(
            status.HTTP_401_UNAUTHORIZED, 
            detail = detail,
            headers = {"WWW-Authenticate": "Bearer"},
        )



class AuthorizationError(HTTPException):
    def __init__(self, detail: str = "Insufficient rights"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )

class InvalidError(HTTPException):

    def __init__(self, detail: str = "Incorrect email or password"):
        super().__init__(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = detail, 
            headers = {'WWW-Authenticate':'Bearer'}
        )

class NotFoundError(HTTPException):
    def __init__(self, detail = "Not Found"):
        super().__init__(status_code = status.HTTP_404_NOT_FOUND, detail = detail)