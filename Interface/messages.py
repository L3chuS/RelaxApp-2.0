
"""Translate from English to Spanish all internal messages from the backend or interface."""

# ERRORS FROM COMMS.PY
ERROR_SERVER_CONNECTION = "La conexión con el servidor ha fallado."
ERROR_SERVER_TIMEOUT = "La solicitud ha superado el tiempo de espera."
ERROR_SERVER_GENERAL = "Error al procesar la solicitud. Vuelve a intentarlo más tarde."

# ERRORS FROM SERIALIZERS.PY
ERROR_SERIALIZERS_INVALID_FIRST_NAME = "El nombre no puede estar vacío o no es válido."
ERROR_SERIALIZERS_INVALID_LAST_NAME = "El apellido no puede estar vacío o no es válido."
ERROR_SERIALIZERS_INVALID_USERNAME = "El nombre de usuario no puede estar vacío o no es válido."
ERROR_SERIALIZERS_USERNAME_MAX_LENGTH = "El nombre de usuario no puede tener más de 25 caracteres."
ERROR_SERIALIZERS_FIRST_LAST_NAME_EMAIL_MAX_LENGTH = "Uno de los campos introducidos tiene más de 100 caracteres. Revísalo antes de continuar."
ERROR_SERIALIZERS_INVALID_EMAIL = "El email no puede estar vacío o no es válido."
ERROR_SERIALIZERS_INVALID_PASSWORD = "La contraseña no puede estar vacía o no es válida."
ERROR_SERIALIZERS_TOKEN_MISSING  = "El código no puede estar vacío."
ERROR_SERIALIZERS_PASSWORD1_MISSING = "Completa el primer campo de la contraseña."
ERROR_SERIALIZERS_PASSWORD2_MISSING = "Completa el segundo campo de la contraseña."
ERROR_SERIALIZERS_USERNAME_BLANK = "El campo del usuario no puede estar vacío."
ERROR_SERIALIZERS_PASSWORD_BLANK = "El campo de la contraseña no puede estar vacío."
ERROR_SERIALIZERS_GENERAL = "Uno o varios campos contienen valores no válidos."
ERROR_SERIALIZERS_PROFILE_NAME_MISSING = "El campo del nombre del perfil no puede estar vacío."
ERROR_SERIALIZERS_VC_SC_BOTH_EMPTY = "Para crear un perfil, es necesario configurar al menos uno de los siguientes apartados: descanso visual o estiramientos."
ERROR_SERIALIZERS_PROFILE_IMPORT_ERROR = "El archivo que intentas abrir está dañado o ha sido modificado y no se puede abrir. Inténtalo con otro archivo."

# MESSAGES FROM VIEWS.PY
MESSAGE_LOGIN_CORRECT = "Iniciando sesión..."
MESSAGE_REGISTER_USER_CREATED = "El usuario se ha creado correctamente."
MESSAGE_PW_RESET_CONF_SUCCESS = "La contraseña ha sido actualizada correctamente."

# ERRORS FROM VIEWS.PY
ERROR_LOGIN_USERNAME_NOT_EXISTS = "El nombre de usuario no existe en nuestro sistema."
ERROR_LOGIN_INVALID_PASSWORD = "La contraseña no es correcta. Vuelve a intentarlo."
                                  
ERROR_REGISTER_USERNAME_EXISTS = "El nombre de usuario ya existe en nuestro sistema. Elije otro."
ERROR_REGISTER_EMAIL_EXISTS = "El email ya existe en nuestro sistema. Elije otro."

ERROR_PW_RESET_CONF_INVALID_TOKEN = "El token proporcionado no es correcto. Comprueba los valores introducidos o solicita uno nuevo."
ERROR_PW_RESET_CONF_TOKEN_USED = "El token proporcionado ya ha sido utilizado. Solicita uno nuevo."
ERROR_PW_RESET_CONF_TOKEN_EXPIRED = "El token proporcionado ya ha expirado. Recuerda que solo es válido por 2 minutos."
ERROR_PW_RESET_CONF_PW_NOT_MATCH = "Las contraseñas indicadas no son iguales."

ERROR_ACCOUNT_REMOVE_UNEXPECTED = "Hubo un error al intentar eliminar la cuenta. Vuelve a intentarlo más tarde."

ERROR_PROFILES_PROFILE_EXISTS = "El nombre del perfil que intentas agregar ya existe. Elija uno distinto."
ERROR_PROFILES_PROFILE_LIMIT = "No se pueden agregar más de 3 perfiles. Elimina alguno de los que ya tienes configurados."
ERROR_PROFILES_GENERAL = "Ha ocurrido un problema al gestionar tus perfiles. Vuelve a intentarlo más tarde."

# ERRORS FROM VALIDATORS.PY
ERROR_VALIDATORS_INVALID_TIME = "Los campos deben contener dos números entre 0 y 60 para poder guardarse."
ERROR_VALIDATORS_EXTRA_HOURS = "No puedes configurar una duración superior a 16 h. Recuerda que debes dormir al menos 8 h."
ERROR_VALIDATORS_MINIMUM_TIME = "La duración debe ser de al menos 1 minuto."
ERROR_VALIDATORS_OVER_LAPSE = "El tiempo de descanso no puede ser superior al intervalo de alertas configurado."
ERROR_VALIDATORS_OVER_DURATION = "El tiempo de intervalo no puede ser superior a la duración configurada."
ERROR_VALIDATORS_NO_BREAK = "El tiempo de descanso debe tener al menos 30 segundos."
ERROR_VALIDATORS_NO_LAPSE = "El tiempo de intervalo entre alertas debe tener al menos 1 minuto."
ERROR_VALIDATORS_INVALID_SOUND = "La configuración de los sonidos no es válida."

# MESSAGES FROM RelaxApp_MessageBox_Options
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_REGISTRATION = "¿Estás seguro de que deseas dar de alta al usuario indicado?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_REGISTRATION = "¿Estás seguro de que deseas cancelar el alta del usuario indicado?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_PW_CHANGE = "¿Estás seguro de que deseas actualizar la contraseña?"
MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_PW_CHANGE = "¿Estás seguro de que deseas cancelar el cambio de contraseña?"
MESSAGE_RELAXAPP_MB_OPTIONS_SIGN_OUT = "¿Estás seguro de que deseas cerrar la sesión de '{username}'?"
MESSAGE_RELAXAPP_MB_OPTIONS_REMOVE_ACCOUNT = "Esta opción permite eliminar definitivamente la cuenta de '{username}'. ¿Estás seguro de que deseas continuar?"
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_IMPORTED = "El perfil se ha importado correctamente y se ha establecido como predeterminado."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_EXPORT_EMPTY = "La exportación no es posible ya que no tienes ningún perfil configurado actualmente."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_STARTAPP_EMPTY = "No puedes iniciar RelaxApp con la opción de perfiles si no tienes ninguno configurado. Configura un perfil o crea una configuración temporal."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_INVALID = "El perfil que intentas importar no es válido. Revísalo antes de continuar."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_UNICODE_ERROR = "El archivo que intentas abrir utiliza una codificación incompatible. Comprueba el archivo antes de continuar."
MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_FILE_ERROR = "El archivo que intentas abrir no existe o se encuentra dañado."
MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_VALUES = "Cada opción elegida debe tener valores configurados antes de iniciar la aplicación."
MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_SETTINGS = "Debes seleccionar al menos una opción antes de iniciar la aplicación."

# MESSAGES FROM RelaxApp_User_Main_Menu_Sounds
MESSAGE_RELAXAPP_USER_MM_SOUNDS_TOOLTIP = "Debes elegir un sonido de alarma en la columna 1 para que suene al finalizar el contador y otro en la columna 2 para que suene entre alertas."
MESSAGE_RELAXAPP_USER_MM_SOUNDS_NO_SOUND = "No puedes guardar una configuración con un sonido propio sin cargarlo previamente."

