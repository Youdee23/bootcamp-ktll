from projects.models.base_model import BaseModel


class User(BaseModel):
    """
    A class called User that inherits from BaseModel
    """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


