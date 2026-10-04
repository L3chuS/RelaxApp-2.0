# MESSAGE FROM VIEWS.PY
MESSAGE_LOGIN_CORRECT = "Iniciando sesión..."
MESSAGE_REGISTER_USER_CREATED = "El usuario ha sido creado exitosamente."
MESSAGE_PW_RESET_CONF_SUCCESS = "Su contraseña ha sido actualizada correctamente."

# ERRORS FROM VIEWS.PY
ERROR_SERIALIZERS_INVALID_FIRST_NAME = "El nombre no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_LAST_NAME = "El apellido no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_USERNAME = "El nombre de usuario no puede estar vacío o es inválido."
ERROR_SERIALIZERS_USERNAME_MAX_LENGTH = "El nombre de usuario no puede tener más de 25 caracteres."
ERROR_SERIALIZERS_FIRST_LAST_NAME_EMAIL_MAX_LENGTH = "Uno de los campos cumplimentados tiene más de 100 caracteres. Revíselo antes de continuar."
ERROR_SERIALIZERS_INVALID_EMAIL = "El email no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_PASSWORD = "La contraseña no puede estar vacía o es inválida."
ERROR_SERIALIZERS_TOKEN_MISSING  = "El código no puede estar vacío."
ERROR_SERIALIZERS_PASSWORD1_MISSING = "Complete el primer campo de la contraseña."
ERROR_SERIALIZERS_PASSWORD2_MISSING = "Complete el segundo campo de la contraseña."
ERROR_SERIALIZERS_USERNAME_BLANK = "El campo del usuario no puede estar vacío."
ERROR_SERIALIZERS_PASSWORD_BLANK = "El campo de la contraseña no puede estar vacía."
ERROR_SERIALIZERS_GENERAL = "Los campos no se han cumplimentado correctamente."
ERROR_SERIALIZERS_PROFILE_NAME_MISSING = "El campo del nombre del perfil no puede estar vacío."
ERROR_SERIALIZERS_VC_SC_BOTH_EMPTY = "Para crear un perfil es necesario configurar al menos un valor del descanso visual o los estiramientos."
ERROR_SERIALIZERS_PROFILE_IMPORT_ERROR = "El archivo que intenta abrir está dañado o ha sido modificado y no puede abrirse. Compruebe con otro archivo."

ERROR_LOGIN_USERNAME_NOT_EXISTS = "El nombre de usuario no existe en nuestro sistema."
ERROR_LOGIN_INVALID_PASSWORD = "La contraseña no es correcta. Vuelva a intentarlo."
                                  
ERROR_REGISTER_USERNAME_EXISTS = "El nombre de usuario ya existe en nuestro sistema y no puede ser duplicado."
ERROR_REGISTER_EMAIL_EXISTS = "El email ya existe en nuestro sistema y no puede ser duplicado."

ERROR_PW_RESET_CONF_INVALID_TOKEN = "El token proporcionado no es correcto. Confirme los valores introducidos o vuelva a solicitar otro."
ERROR_PW_RESET_CONF_TOKEN_USED = "El token proporcionado ya ha sido utilizado. Vuelva a solicitar uno nuevamente."
ERROR_PW_RESET_CONF_TOKEN_EXPIRED = "El token proporcionado ya ha expirado. Recuerde que sólo es válido por 2 minutos."
ERROR_PW_RESET_CONF_PW_NOT_MATCH = "Las contraseñas indicadas no son iguales."

ERROR_ACCOUNT_REMOVE_UNEXPECTED = "Hubo un error al intentar eliminar su cuenta. Vuelva a intentarlo más tarde."

ERROR_PROFILES_PROFILE_EXISTS = "El nombre del perfil que intenta agregar ya existe. Elija uno distinto."
ERROR_PROFILES_PROFILE_LIMIT = "No se pueden agregar mas de 3 perfiles. Elimine alguno de los que tiene ya configurados."
ERROR_PROFILES_GENERAL = "Hubo un problema con la gestión de sus perfiles. Vuelva a intentarlo nuevamente."

ERROR_VALIDATORS_INVALID_TIME = "Los campos tienen que tener 2 números entre el 0 y el 60 para guardarlos."
ERROR_VALIDATORS_EXTRA_HOURS = "No puedes configurar mas de 16hs de duración. Recuerda que mínimo debes dormir 8hs."
ERROR_VALIDATORS_MINIMUM_TIME = "Debes configurar al menos 1 minuto de duración."
ERROR_VALIDATORS_OVER_LAPSE = "El tiempo de descanso no puede ser superior al intervalo de alertas configurado."
ERROR_VALIDATORS_OVER_DURATION = "El tiempo de intervalo no puede ser superior a la duración configurada."
ERROR_VALIDATORS_NO_BREAK = "El tiempo de descanso debe tener al menos 30 segundos."
ERROR_VALIDATORS_NO_LAPSE = "El tiempo de intervalo entre alertas debe tener al menos 1 minuto."
ERROR_VALIDATORS_INVALID_SOUND = "La configuración de los sonidos no es válida."

# ERRORS FROM COMMS.PY
ERROR_SERVER_CONNECTION = "La conexión con el servidor ha fallado."
ERROR_SERVER_TIMEOUT = "La solicitud ha superado el tiempo de espera."
ERROR_SERVER_GENERAL = "Error al procesar su solicitud. Vuelva a intentarlo mas tarde."

# MESSAGES FROM RelaxApp_MessageBox_Options
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_REGISTRATION = "¿Está seguro que desea dar de alta el usuario indicado?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_REGISTRATION = "¿Está seguro que desea cancelar el alta del usuario indicado?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_PW_CHANGE = "¿Está seguro que desea actualizar su contraseña?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_PW_CHANGE = "¿Está seguro que desea cancelar el cambio de contraseña?"
MESSAGE_RELAXAPP_MB_OPTIONS_SIGN_OUT = "¿Está seguro que desea cerrar la sesión de '{username}'?"
MESSAGE_RELAXAPP_MB_OPTIONS_REMOVE_ACCOUNT = "Esta opción permite eliminar completamente la cuenta de '{username}'. ¿Está seguro que desea continuar?"
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_IMPORTED = "El perfil ha sido importado exitósamente y se ha establecido como predeterminado."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_EXPORT_EMPTY = "La exportación no es posible ya que no tienes ningún perfil configurado actualmente."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_STARTAPP_EMPTY = "No es posible iniciar RelaxApp si eliges la opción de perfiles y no tienes ninguno configurado. Configura uno o crea valores temporales."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_INVALID = "El perfil que intenta importar es inválido. Revíselo antes de continuar."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_UNICODE_ERROR = "El archivo que intenta abrir utiliza una codificación no compatible. Revíselo antes de continuar."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_FILE_ERROR = "El archivo que intenta abrir no existe o se encuentra dañado."
MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_VALUES = "Cada opción elegida debe tener valores configurados antes de iniciar la aplicación."
MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_SETTINGS = "Debes seleccionar al menos una opción antes de iniciar la aplicación."


# MESSAGES FROM RelaxApp_User_Main_Menu_Sounds
MESSAGE_RELAXAPP_USER_MM_SOUNDS_TOOLTIP = "Debes elegir un sonido de alarma en la columna 1 que sonará al finalizar el contador y otro en la columna 2 para que se ejecute \
entre cada alerta."
MESSAGE_RELAXAPP_USER_MM_SOUNDS_NO_SOUND = "No puedes guardar una configuración con un sonido propio sin cargarlo previamente."

