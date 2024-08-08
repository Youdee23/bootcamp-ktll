import uuid
from datetime import datetime
from __init__ import storage
from projects.models.engine import file_storage


class BaseModel:
    """ A class called BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Instantiating the class with new attributes
        id: The unique id for each BaseModel; it will be converted to a string
        created_at: The current date and time the instance is created
        updated_at: The current date and time an instance is created and 
        it will be updated everytime an object is changed.
        *args: It takes a variable number of positional arguments
        **kwargs: It takes a variable number of keyword arguments  
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # if not self.__class__.__name__.__dict__:
        #     print(storage.new()) 

        if kwargs:
            kwargs = {}
            for k, v in vars(self).items():
                kwargs[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>'
    
    def save(self):
        """ Updates the attribute updated_at with the current date_time"""
        self.updated_at = datetime.now()  # to get the current date/time
        storage.save()
        
    def to_dict(self):
        """ Returns a dictionary of all key/values of __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict[__class__] = self.__class__.__name__
        instance_dict['created_at'] = instance_dict['created_at'].isoformat()
        instance_dict['updated_at'] = instance_dict['updated_at'].isoformat()
        return instance_dict
    
    
    



    


    
    
