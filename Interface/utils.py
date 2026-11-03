# External imports.
import os
import sys

# def get_resource_path(relative_path):
#     """Function to get absolute path."""
#     try:
#         # When .exe is executed.
#         base_path = sys._MEIPASS
#     except AttributeError:
#         # When script is executed.
#         base_path = os.path.dirname(__file__)
#     return os.path.join(base_path, relative_path)

def get_resource_path(relative_path):
    """Return the absolute path of an application resource."""

    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)