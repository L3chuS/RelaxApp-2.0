# External imports.
import os

# Internal imports.
from utils import get_resource_path

"""Temporary values for a current instance."""

os.path.join(get_resource_path("sounds"))
sounds_path = os.path.join(get_resource_path("sounds"))

class TemporaryProfile:
    """Store temporary profile settings for the current session."""
    
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
    """Store temporary token and username for the current session."""
    
    token = None
    username = None
    
    @classmethod
    def clear(cls):
        cls.token = None
        cls.username = None