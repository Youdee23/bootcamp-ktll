import uuid
import datetime


class BaseModel():
    """ A class called BaseModel"""
    def __init__(self, id, created_at, updated_at):
        """
        Instantiating the class with new attributes
        id: The unique id for each BaseModel; it will be converted to a string
        created_at: The current date and time the instance is created
        updated_at: The current date and time an instance is created and 
        it will be updated everytime an object is changed.  
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self, id):
        return f' BaseModel {self.id} {self.__dict__}'
    
    def save(self, date_time):
        """ Updates the attribute updated_at with the current date_time"""
        

    def to_dict(self):
        """ Returns a dictionary of all key/values of __dict__ of the instance"""
        instance_dict = self.__dict__
        instance_dict['__class__'] = 'BaseModel'
        return instance_dict


    # def get_id(self, unique_id):
    #     """ Retrieves and returns a string of the new unique id for each BaseModel """
    #     unique_id = uuid.uuid4()
    #     return str(unique_id)
    
    # def get_created_at(self, date_time):
    #     """ Returns the current date and time an instance is created"""
    #     return date_time
    
    # def get_updated_at(self, date_time):
    #     """ Returns the updated date_time each time an object is changed"""
    #     return date_time
    


    
    
