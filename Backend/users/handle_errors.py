
def format_serializers_code_errors(error):
    """Convert serializer error codes into a unified identifier.

    Combines the field name and its validation error code into a single
    string, such as 'password_blank', for consistent error handling.
    """

    for key, err in error.items():
        key = f"{key}_{err[0]}"
        return key
    
