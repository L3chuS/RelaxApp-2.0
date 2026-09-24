from django.core.exceptions import ValidationError

    # # This method checks if the lenght of the profile name is shorter than 1 or larger than 20 characters.
    # def check_profile_lenght(self, value):
    #     if len(value) > 20 or len(value) == 0:
    #         return False

    # # This method checks if the profile name is duplicated.
    # def check_profile_duplicated(self, profile):
    #     database.query(f"SELECT Profile_Name FROM {databases['database1']}.{tables['settings_table']} WHERE login = '{user['login']}' and Profile_Name = '{profile}'")
    #     profile_name = database.value
    #     if profile_name != []:
    #         return True

# This method checks if all values set by the user are correct.
def check_timer_settings(value):

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

# # This method checks if all sound values set by the user are correct.
# def check_sounds_settings(self, value):
#     if value == "":
#         return None
#     sound_path = os.path.isfile(value)
#     extension_sound_path = os.path.splitext(value)

#     if sound_path == False:
#         return False

#     extension = False
#     for values in audio_accepted_files:
#         if extension_sound_path[1] in values[1]:
#             extension = True
#             break

#     if extension == False:
#         return False

#     return True