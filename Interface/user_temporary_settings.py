
class TemporaryProfile:
    
    visual_configuration = ""
    stretch_configuration = ""
    final_sounds_configuration = ""
    lapse_sounds_configuration = ""
     
    @classmethod   
    def clear(cls):
        cls.visual_configuration = ""
        cls.stretch_configuration = ""
        cls.final_sounds_configuration = ""
        cls.lapse_sounds_configuration = ""

    @classmethod
    def display_values(cls):
        print("---------------------------------")
        print("La configuración es:")
        print("* visual_configuration:       ", cls.visual_configuration)
        print("* stretch_configuration:      ", cls.stretch_configuration)
        print("* final_sounds_configuration: ", cls.final_sounds_configuration)
        print("* lapse_sounds_configuration: ", cls.lapse_sounds_configuration)
        print("---------------------------------")
        
class Session:
    token = None
    username = None
    
    @classmethod
    def clear(cls):
        cls.token = None
        cls.username = None