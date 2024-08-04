import json
import os
import base_model


class FileStorage:
    """ A class called FileStorage """
    script_dir = os.path.dirname(__file__)
    __file_path = os.path.join(script_dir, '/file.json')
    __objects = {}
    
    def all(self, cls=None):
        """ Returns the dictionary `__objects` """
        return self.__objects
    
    def new(self, obj):
        """ Updates the `__objects` dict """
        obj.update({f"{str(self.__class__.__name__)}.{self.id}": self.id})
    
    def save(self):
        """ Serializes instances to a json file """
        json.dumps(self.__objects, default=lambda __objects: __objects.__dict__)
    
    def reload(self):
        """ Deserializes json file to instances """
        if self.__file_path:
            json.loads(self.__file_path)
        else:
            pass
        
          
# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, '/file.json')
# print(script_dir)
# print(file_path)

