
def format_serializers_code_errors(error):

    for key, err in error.items():
        key = f"{key}_{err[0]}"
        return key
    
