from projects.models.base_model import BaseModel


class User(BaseModel):
    """
    A class called User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

