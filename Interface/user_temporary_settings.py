import os
from utils import get_resource_path
os.path.join(get_resource_path("sounds"))
sounds_path = os.path.join(get_resource_path("sounds"))

class TemporaryProfile:
    
    visual_configuration = ""
    stretch_configuration = ""
    final_sounds_configuration = os.path.join(sounds_path, "Final.mp3")
    lapse_sounds_configuration = os.path.join(sounds_path, "Lapse.mp3")
     
    @classmethod   
    def clear(cls):
        cls.visual_configuration = ""
        cls.stretch_configuration = ""
        cls.final_sounds_configuration = os.path.join(sounds_path, "Final.mp3")
        cls.lapse_sounds_configuration = os.path.join(sounds_path, "Lapse.mp3")
        
class Session:
    token = None
    username = None
    
    @classmethod
    def clear(cls):
        cls.token = None
        cls.username = None