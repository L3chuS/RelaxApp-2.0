# External imports.
from django.core.exceptions import ValidationError
import os

"""Use to have all specific validations of the backend. Use by serializers to validate values."""

# Set all valid audio extension.
audio_accepted_files = (("Audio Files", "*.mp3"),("Audio Files", "*.ogg"), ("Audio Files", "*.wav"),
                        ("Audio Files", "*.m4a"), ("Audio Files", "*.wma"), ("Audio Files", "*.flac"))


def check_timer_settings(value):
    """Validate values provided by the user.

    Raises a ValidationError if the configuration is invalid.
    """

    try:
        lenght_HH = value[:2]
        lenght_MM = value[2:4]
        lapse = value[4:6]
        break_time_MM = value[6:8]
        break_time_SS = value[8:10]
        sound = value[10:]
    except:
        return ValidationError(
            "The time given is invalid.", 
            code="INVALID_TIME"
            )

    valid_numbers = [str(x).zfill(2) for x in range(61)]

    if lenght_HH not in valid_numbers or lenght_MM not in valid_numbers or \
    lapse not in valid_numbers or break_time_MM not in valid_numbers or \
    break_time_SS not in valid_numbers:
        raise ValidationError(
            "The time given is invalid.", 
            code="INVALID_TIME"
            )

    elif int(lenght_HH) * 60 + int(lenght_MM) > 960:
        raise ValidationError(
            "The time given can't be higher than 16hs.", 
            code="EXTRA_HOURS"
            )

    elif int(lenght_HH) * 60 + int(lenght_MM) < 1:
        raise ValidationError(
            "The time given must be higher than 1 minute.", 
            code="MINIMUM_TIME"
            )

    elif int(lapse) == 0:
        raise ValidationError(
            "The lapse must be at least 1 minute.", 
            code="NO_LAPSE"
            )

    elif int(lapse) > int(lenght_HH) * 60 + int(lenght_MM):
        raise ValidationError(
            "The lapse can't be higher than the time.", 
            code="OVER_DURATION"
            )
        
    elif int(break_time_MM) == 0 and int(break_time_SS) < 30:
        raise ValidationError(
            "The break time must be at least 30 seconds.", 
            code="NO_BREAK"
            )

    elif int(break_time_MM) * 60 + int(break_time_SS) > \
    int(lapse) * 60:
        raise ValidationError(
            "The break time can't be higher than the lapse.", 
            code="OVER_LAPSE"
            )

    elif sound != "True" and sound != "False":
        raise ValidationError(
            "The sounds settings are invalid.", 
            code="INVALID_SOUND"
            )
    return

def check_sound_settings(value):  
    """Validate the sound file paths and their supported formats.

    Raises a ValidationError if the configuration is invalid.
    """
    
    if value == "":
        raise ValidationError(
            "The path given is empty.", 
            code="SOUND_EMPTY_PATH"
            )

    print("Esto es el path de value: ", value, "text")
    
    sound_path = os.path.isfile(value)
    extension_sound_path = os.path.splitext(value)   
    
    if sound_path == False:
        raise ValidationError(
            "The path given is invalid.", 
            code="SOUND_INVALID_PATH"
            )

    extension = False
    
    for values in audio_accepted_files:
        if extension_sound_path[1] in values[1]:
            extension = True
            break

    if extension == False:
        raise ValidationError(
            "The extension of the file given is invalid.", 
            code="SOUND_INVALID_EXTENSION"
            )

    return
