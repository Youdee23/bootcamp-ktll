import json
import os
# import base_model


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
        obj.update({f"{type(obj).__name__}.{obj.id}": obj})
    
    def save(self):
        """ Serializes __objects to a json file """
        with open(self.__file_path, "w") as js_file:
            json.dump(self.__objects, js_file)

    def reload(self):
        """ Deserializes json file to __objects """
        try:
            with open(self.__file_path) as js_file:
                data = json.load(js_file)
                for k, v in data.items():
                    self.__objects[k] = v
        except FileNotFoundError:
            pass
        
        
        
        
          
# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, '/file.json')
# print(script_dir)
# print(file_path)

