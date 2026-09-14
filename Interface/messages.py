# MESSAGE FROM VIEWS.PY
MESSAGE_LOGIN_CORRECT = "Iniciando sesión..."
MESSAGE_REGISTER_USER_CREATED = "El usuario ha sido creado exitosamente."
MESSAGE_PW_RESET_CONF_SUCCESS = "Su contraseña ha sido actualizada correctamente."

# ERRORS FROM VIEWS.PY
ERROR_SERIALIZERS_INVALID_FIRST_NAME = "El nombre no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_LAST_NAME = "El apellido no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_USERNAME = "El nombre de usuario no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_EMAIL = "El email no puede estar vacío o es inválido."
ERROR_SERIALIZERS_INVALID_PASSWORD = "La contraseña no puede estar vacía o es inválida."
ERROR_SERIALIZERS_TOKEN_MISSING  = "El código no puede estar vacío."
ERROR_SERIALIZERS_PASSWORD1_MISSING = "Complete el primer campo de la contraseña."
ERROR_SERIALIZERS_PASSWORD2_MISSING = "Complete el segundo campo de la contraseña."
ERROR_SERIALIZERS_GENERAL = "Los campos no se han cumplimentado correctamente."

ERROR_LOGIN_USERNAME_NOT_EXISTS = "El nombre de usuario no existe en nuestro sistema."
ERROR_LOGIN_INVALID_PASSWORD = "La contraseña no es correcta. Vuelva a intentarlo."

ERROR_REGISTER_USERNAME_EXISTS = "El nombre de usuario ya existe en nuestro sistema y no puede ser duplicado."
ERROR_REGISTER_EMAIL_EXISTS = "El email ya existe en nuestro sistema y no puede ser duplicado."

ERROR_PW_RESET_CONF_INVALID_TOKEN = "El token proporcionado no es correcto. Confirme los valores introducidos o vuelva a solicitar otro."
ERROR_PW_RESET_CONF_TOKEN_USED = "El token proporcionado ya ha sido utilizado. Vuelva a solicitar uno nuevamente."
ERROR_PW_RESET_CONF_TOKEN_EXPIRED = "El token proporcionado ya ha expirado. Recuerde que sólo es válido por 2 minutos."
ERROR_PW_RESET_CONF_PW_NOT_MATCH = "Las contraseñas indicadas no son iguales."

# ERRORS FROM COMMS.PY
ERROR_SERVER_CONNECTION = "La conexión con el servidor ha fallado."
ERROR_SERVER_TIMEOUT = "La solicitud ha superado el tiempo de espera."
ERROR_SERVER_GENERAL = "Error al procesar su solicitud. Vuelva a intentarlo mas tarde."
