from projects.models.base_model import BaseModel


class City(BaseModel):
    """
    A class called City that inherits from BaseModel
    """
    def __init__(self):
        self.state_id = ""
        self.name = ""

