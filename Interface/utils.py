# External imports.
import os
import sys

def get_resource_path(relative_path):
    """Function to get absolute path."""
    try:
        # When .exe is executed.
        base_path = sys._MEIPASS
    except AttributeError:
        # When script is executed.
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)