# External imports.
import tkinter as tk
import customtkinter as ctk
import ctypes
import time
import threading
import pygame
from PIL import Image
from tktooltip import ToolTip
import datetime
import os
from utils import get_resource_path
import webbrowser
import json

# Internal imports.
import comms
import messages
from user_temporary_settings import *

"""Create all inteface of RelaxApp."""

# Get the windows resolution regardless of rescaling
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

# Get the image and sounds folders path.
image_path = get_resource_path("images")
sounds_path = get_resource_path("sounds")

# Set appearance.
appearance = ctk.set_appearance_mode("dark")
color_theme = ctk.set_default_color_theme("green")

# Dictionary to set colors of the app.
colors = {"black":"#242424",
          "white":"white",
          "soft_grey":"#2b2b2b",
          "dark_green":"#0a4e50",
          "soft_green":"#118589"}

# Set App font.
font = "Segoe Print"

# Set all valid audio extension.
audio_accepted_files = (("Audio Files", "*.mp3"),("Audio Files", "*.ogg"), ("Audio Files", "*.wav"),
                        ("Audio Files", "*.m4a"), ("Audio Files", "*.wma"), ("Audio Files", "*.flac"))


class RelaxApp_Structure:
    """Define the application's general structure, including its title, dimensions, and main frame."""

    def __init__(self, root):

        self.root = root

        # Set the width, height, configuration and location of the windows.
        width = 350
        height = 500
        width_resolution = self.root.winfo_screenwidth() // 2 - width // 2 - width // 3
        height_resolution = self.root.winfo_screenheight() // 2 - height
        self.dimentions = self.root.geometry(f"{width}x{height}+{width_resolution}+{height_resolution}")
        self.maximize = self.root.resizable(False,False)

        # The main frame is created.
        self.general_frame = ctk.CTkFrame(self.root, height=485, width=336, fg_color=colors["soft_grey"],
                                          corner_radius=10)
        self.general_frame.place(rely=0.015, relx=0.02)

        # Set the title and the logo of the app.
        self.title = self.root.title("RelaxApp")
        self.root.after(200, lambda: self.root.iconbitmap(os.path.join(image_path, "logo.ico")))

        # The main menu is run.
        RelaxApp_Initial_Frame(self.root, self.general_frame)

    def close_create(self, new_window, root, clean_frame, *args):
        """Close the current window and create a new root window.

        Remove the specified widgets from the screen.
        """
        
        self.root = root
        # All widget are remove from the frame.
        for wid in clean_frame.winfo_children():
            wid.destroy()
        # New class is run.
        app = new_window(self.root, clean_frame, *args)

    def close_create2(self, new_window, root, clean_frame, *args):
        """Create a new root window and recreate the main frame after the current root is destroyed."""
        
        self.root = root
        for wid in clean_frame.winfo_children():
            wid.destroy()

        self.general_frame = ctk.CTkFrame(clean_frame, height=485, width=336, fg_color=colors["soft_grey"],
                                          corner_radius=10)
        self.general_frame.place(rely=0.0, relx=0.0)

        app = new_window(self.root, self.general_frame, *args)

    def clean_MMP_widgets(self, clean_MMP_frame):
        """Remove widgets from the main menu profile frame."""
        
        for element in clean_MMP_frame:
            for wid in element.winfo_children():
                wid.destroy()
        return clean_MMP_frame

    def hide_unhide_window(self, root):
        """Hide the root window while the application is running and restore it when returning."""
        
        self.root = root
        self.root.withdraw()


class RelaxApp_MessageBox_Structure:
    """Define the general structure of pop-up windows, including their dimensions, titles, and frames."""

    def __init__(self):

        # New pop-ups is created.
        self.window_MS = ctk.CTkToplevel()
        self.window_MS.grab_set()

        # Set the width, height, configuration and location of the windows.
        width = 550
        height = 150
        width_resolution = self.window_MS.winfo_screenwidth() // 2 - width // 2 - width // 3
        height_resolution = self.window_MS.winfo_screenheight() // 2 - height
        self.dimensions = self.window_MS.geometry(f"{width}x{height}+{width_resolution}+{height_resolution}")
        self.maximize = self.window_MS.resizable(False,False)

        # Set a frame at the background.
        self.frame_MS = ctk.CTkFrame(self.window_MS, height=200, width=550, fg_color=colors["soft_grey"])
        self.frame_MS.pack(pady=10, padx=10, fill="both")

        # Set the title and the logo of the app.
        self.title = self.window_MS.title("RelaxApp")
        self.window_MS.after(200, lambda: self.window_MS.iconbitmap(os.path.join(image_path, "logo.ico")))

    def clean_MB_widgets(self, clean_MB_frame):
        """Remove widget from the main menu profile."""
        
        counter = 1
        for wid in clean_MB_frame.winfo_children():
            if counter != 1:
                wid.destroy()
            counter += 1


class RelaxApp_User_Settings_Structure:
    """Define the general structure of the user's settings window, including its appearance, dimensions, and title."""
       
    def __init__(self):

        # New pop-ups is created.
        self.window_User_SS = ctk.CTkToplevel()
        self.window_User_SS.grab_set()

        # Set the width, height, configuration and location of the windows.
        width = 260
        height = 300
        width_resolution = self.window_User_SS.winfo_screenwidth() // 2 - width // 2 - width // 3
        height_resolution = self.window_User_SS.winfo_screenheight() // 2 - height
        self.dimensions = self.window_User_SS.geometry(f"{width}x{height}+{width_resolution}+{height_resolution}")
        self.maximize = self.window_User_SS.resizable(False,False)

        # Set a frame at the background.
        self.frame_User_SS = ctk.CTkFrame(self.window_User_SS, height=300, width=260, fg_color=colors["soft_grey"])
        self.frame_User_SS.pack(pady=10, padx=10, fill="both")

        # Set the title and the logo of the app.
        self.title = self.window_User_SS.title("RelaxApp")
        self.window_User_SS.after(200, lambda: self.window_User_SS.iconbitmap(os.path.join(image_path, "logo.ico")))


class RelaxApp_Running_Structure:
    """Define the general structure of the running window, including its appearance, dimensions, and title."""

    def __init__(self):

        # New pop-ups is created.
        self.window_RS = ctk.CTkToplevel()
        self.window_RS.grab_set()

        # Set the width, height, configuration and location of the windows.
        width = 280
        height = 400
        width_resolution = self.window_RS.winfo_screenwidth() // 2 - width // 2 - width // 3
        height_resolution = self.window_RS.winfo_screenheight() // 2 - height
        self.dimensions = self.window_RS.geometry(f"{width}x{height}+{width_resolution}+{height_resolution}")
        self.maximize = self.window_RS.resizable(False,False)

        # Set a frame at the background.
        self.frame_RS = ctk.CTkFrame(self.window_RS, height=400, width=280, fg_color=colors["soft_grey"])
        self.frame_RS.pack(pady=10, padx=10, fill="both")

        # Set the title and the logo of the app.
        self.title = self.window_RS.title("RelaxApp")
        self.window_RS.after(200, lambda: self.window_RS.iconbitmap(os.path.join(image_path, "logo.ico")))


class RelaxApp_Profile_Name_Structure:
    """Define the general structure of the profile name window, including its appearance, dimensions, and title."""

    def __init__(self, root):
        self.root = root

        # New pop-ups is created.
        self.window_PFS = ctk.CTkToplevel()
        self.window_PFS.grab_set()

        # Set the width, height, configuration and location of the windows.
        width = 310
        height = 50
        width_resolution = self.window_PFS.winfo_screenwidth() // 2 - width // 2 - width // 3
        height_resolution = self.window_PFS.winfo_screenheight() // 2 - height - 45
        self.dimensions = self.window_PFS.geometry(f"{width}x{height}+{width_resolution}+{height_resolution}")
        self.maximize = self.window_PFS.resizable(False,False)

        # Set a frame at the background.
        self.frame_PFS = ctk.CTkFrame(self.window_PFS, height=100, width=310, fg_color=colors["soft_grey"])
        self.frame_PFS.pack(pady=10, padx=10, fill="both")

        # Set the title and the logo of the app.
        self.title = self.window_PFS.title("RelaxApp")
        self.window_PFS.after(200, lambda: self.window_PFS.iconbitmap(os.path.join(image_path, "logo.ico")))


class Requests_Status():
    """Defines the general functions to check the connection with backend and the responses returned."""
     
    def check_server_connection(response_dict):
        """Connection with the server is checked."""
        
        if response_dict["connection_status"]:
            response = response_dict["response"]
            return response, None

        else:
            message = Set_Messages.server_messages(response_dict["error_link"])
            print(response_dict["error"])
            return None, message

    def check_request_status(response, status, type):
        """The status of the request is checked. A message or error is returned."""
        values = response.json()
        valid = False
        
        if response.status_code == status:
            message = Set_Messages.response_messages(values["message_link"])
            print(values["message"])
            valid = True
        else:
            if values["error_type"] == "VIEWS":
                # Message from backend is translated.
                message = Set_Messages.response_messages(values["error_link"])
                print(values["error"])
                
            elif values["error_type"] == "SERIALIZERS":
                # The first key error from serializers is gotten.
                key = values["error_link"].upper()
                # Message from backend is translated.
                message = Set_Messages.serializers_messages(key)
                print("* ERROR: ", values["error"])
                
            elif values["error_type"] == "VALIDATORS":
                message = Set_Messages.validators_messages(values["error_link"])
                print("* ERROR: ", values["error"])
        
        if type in (
            "sign_in",
            "get_profile_list",
            "accept_button_MB",
        ):
            if valid:
                return True, values, message
            return False, None, message

        elif type in (
            "send_code",
            "remove_profile",
            "save_settings",
            "accept_profile_name",
            "save_settings_MM",
        ):
            if valid:
                return True, None
            return False, message
        
        elif type in (
            "import_profile"
        ):
            if valid:
                return True, None,  message
            return False, values, message


class Set_Messages():       
    """Defines the general functions to convert messages from backend in English to the interface in Spanish."""
    
    def server_messages(type):
        """Messages related to the server connection."""
        
        if type == "ERROR_SERVER_CONNECTION":
            return messages.ERROR_SERVER_CONNECTION
        elif type == "ERROR_SERVER_TIMEOUT":
            return messages.ERROR_SERVER_TIMEOUT
        else:
            return messages.ERROR_SERVER_GENERAL
       
    def serializers_messages(key):
        """Messages related to the serializers errors."""
        
        if key == "USERNAME_BLANK":
            return messages.ERROR_SERIALIZERS_USERNAME_BLANK
        elif key == "PASSWORD_BLANK":
            return messages.ERROR_SERIALIZERS_PASSWORD_BLANK
        elif key == "FIRST_NAME_BLANK":
            return messages.ERROR_SERIALIZERS_INVALID_FIRST_NAME
        elif key == "LAST_NAME_BLANK":
            return messages.ERROR_SERIALIZERS_INVALID_LAST_NAME
        elif key == "USERNAME_MAX_LENGTH":
            return messages.ERROR_SERIALIZERS_USERNAME_MAX_LENGTH
        
        elif key in (
            "FIRST_NAME_MAX_LENGTH",
            "LAST_NAME_MAX_LENGTH",
            "EMAIL_MAX_LENGTH",
        ):
            return messages.ERROR_SERIALIZERS_FIRST_LAST_NAME_EMAIL_MAX_LENGTH
        elif key == "EMAIL_BLANK" or key == "EMAIL_INVALID":
            return messages.ERROR_SERIALIZERS_INVALID_EMAIL
        elif key == "CODE_BLANK":
            return messages.ERROR_SERIALIZERS_TOKEN_MISSING
        elif key == "PASSWORD1_BLANK":
            return messages.ERROR_SERIALIZERS_PASSWORD1_MISSING
        elif key == "PASSWORD2_BLANK":
            return messages.ERROR_SERIALIZERS_PASSWORD2_MISSING
        elif key == "PASSWORD_NO_MATCH_INVALID":
            return messages.ERROR_PW_RESET_CONF_PW_NOT_MATCH
        elif key == "PROFILE_NAME_BLANK":
            return messages.ERROR_SERIALIZERS_PROFILE_NAME_MISSING
        elif key == "PROFILE_VALUES_EMPTY_INVALID":
            return messages.ERROR_SERIALIZERS_VC_SC_BOTH_EMPTY
        else:
            return messages.ERROR_SERIALIZERS_GENERAL
    
    def response_messages(type):
        """Messages related to the views errors."""
        
        if type == "MESSAGE_LOGIN_CORRECT":
            return messages.MESSAGE_LOGIN_CORRECT
        elif type == "ERROR_LOGIN_USERNAME_NOT_EXISTS":
            return messages.ERROR_LOGIN_USERNAME_NOT_EXISTS
        elif type == "ERROR_LOGIN_INVALID_PASSWORD":
            return messages.ERROR_LOGIN_INVALID_PASSWORD

        elif type == "MESSAGE_REGISTER_USER_CREATED":
            return messages.MESSAGE_REGISTER_USER_CREATED
        elif type == "ERROR_REGISTER_USERNAME_EXISTS":
            return messages.ERROR_REGISTER_USERNAME_EXISTS
        elif type == "ERROR_REGISTER_EMAIL_EXISTS":
            return messages.ERROR_REGISTER_EMAIL_EXISTS
        
        elif type == "MESSAGE_PW_RESET_CONF_SUCCESS":
            return messages.MESSAGE_PW_RESET_CONF_SUCCESS
        elif type == "ERROR_PW_RESET_CONF_INVALID_TOKEN":
            return messages.ERROR_PW_RESET_CONF_INVALID_TOKEN
        elif type == "ERROR_PW_RESET_CONF_TOKEN_USED":
            return messages.ERROR_PW_RESET_CONF_TOKEN_USED
        elif type == "ERROR_PW_RESET_CONF_TOKEN_EXPIRED":
            return messages.ERROR_PW_RESET_CONF_TOKEN_EXPIRED
        elif type == "ERROR_ACCOUNT_REMOVE_UNEXPECTED":
            return messages.ERROR_ACCOUNT_REMOVE_UNEXPECTED
        
        elif type == "ERROR_PROFILES_PROFILE_EXISTS":
            return messages.ERROR_PROFILES_PROFILE_EXISTS
        elif type == "ERROR_PROFILES_PROFILE_LIMIT":
            return messages.ERROR_PROFILES_PROFILE_LIMIT
        elif type == "ERROR_PROFILES_GENERAL":
            return messages.ERROR_PROFILES_GENERAL
        
    def validators_messages(key):
        """Messages related to the validators errors."""
        
        if key == "INVALID_TIME":
            return messages.ERROR_VALIDATORS_INVALID_TIME
        elif key == "EXTRA_HOURS":
            return messages.ERROR_VALIDATORS_EXTRA_HOURS
        elif key == "MINIMUM_TIME":
            return messages.ERROR_VALIDATORS_MINIMUM_TIME
        elif key == "OVER_DURATION":
            return messages.ERROR_VALIDATORS_OVER_DURATION
        elif key == "OVER_LAPSE":
            return messages.ERROR_VALIDATORS_OVER_LAPSE
        elif key == "NO_LAPSE":
            return messages.ERROR_VALIDATORS_NO_LAPSE
        elif key == "NO_BREAK":
            return messages.ERROR_VALIDATORS_NO_BREAK
        elif key == "INVALID_SOUND":
            return messages.ERROR_VALIDATORS_INVALID_SOUND
       

class Validate_CMD:
    """Used to validate the user's personal settings entries in the main menu."""

    def validate_hours(text):
        """Funtions to validate lenght of the hours entries."""
        if len(text) == 0:
            return True
        elif text == "HH":
            return True
        elif len(text) < 3 and text.isdigit():
            return True
        else:
            return False

    def validate_min_sec(text):
        """Funtions to validate lenght of the minutes and seconds entries."""
        if len(text) == 0:
            return True
        elif text == "MM" or text == "SS":
            return True
        elif len(text) < 3 and text.isdigit():
            return True
        else:
            return False

    def validate_lenght_name(text):
        """Funtions to validate lenght of the profile name not to be larger than 20 characters."""
        
        if len(text) == 0:
            return True
        elif text == "Nombre del Perfil":
            return True
        elif len(text) < 21:
            return True
        else:
            return False

    def validate_sound_path(value):
        sound_path = os.path.isfile(value)
        
        if sound_path == False:
            return False
        return True


class RelaxApp_Initial_Frame():
    """This class defines all buttons and options availables into the first frame."""

    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # User label.
        self.user = ctk.CTkLabel(self.frame, text="Usuario", font=(font,19))
        self.user.place(rely=0.40, relx=0.5, anchor="center")

        # User entry.
        self.entry_user = ctk.CTkEntry(self.frame,font=(font,15), corner_radius=10)
        self.entry_user.place(rely=0.47, relx=0.5, anchor="center")
        self.entry_user.insert(0, "Ej: Usuario")
        self.entry_user.bind("<Button-1>", lambda remove: self.entry_user.delete(0, tk.END))

        # Password label.
        self.password = ctk.CTkLabel(self.frame, text="Contraseña", font=(font,19))
        self.password.place(rely=0.54, relx=0.5, anchor="center")

        # Password entry.
        self.entry_password = ctk.CTkEntry(self.frame,font=(font,15), corner_radius=10, show="*")
        self.entry_password.place(rely=0.61, relx=0.5, anchor="center",)
        self.entry_password.insert(0, "**********")
        self.entry_password.bind("<Button-1>", lambda remove: self.entry_password.delete(0, tk.END))

        # Login button.
        self.button_start = ctk.CTkButton(self.frame, text="Entrar", font=(font,20), command= self.sign_in,
                                          corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                          hover_color=colors["dark_green"])
        self.button_start.place(rely=0.72, relx=0.5, anchor="center")

        # "Register User" button.
        self.button_new_user = ctk.CTkButton(self.frame, width=10, height=10, text="Registrar Usuario", font=(font,12),
                                             command=self.sign_up, corner_radius=10, hover=True, fg_color=colors["soft_grey"],
                                             hover_color=colors["dark_green"])
        self.button_new_user.place(rely=0.9, relx=0.04)

        # "Forget password" button.
        self.button_forget_pw = ctk.CTkButton(self.frame, width=10, height=10, text="Olvidé contraseña", font=(font,12),
                                              command=self.change_password, corner_radius=10, hover=True, fg_color=colors["soft_grey"],
                                              hover_color=colors["dark_green"])
        self.button_forget_pw.place(rely=0.9, relx=0.6)

    def sign_in(self):
        """Method to login."""
        
        valid_request = False
        get_login = self.entry_user.get()
        get_password = self.entry_password.get()

        data = {
            "username" : get_login,
            "password" : get_password
        }

        # Request to login is started.
        response_dict = comms.login(data)
        response, message = Requests_Status.check_server_connection(response_dict) 

        if response != None:

            status_expected = 200
            valid_request, values, message = Requests_Status.check_request_status(response, status_expected, "sign_in")

        # Label "self.login" is checked if exists or not to clean it from the interface.
        if hasattr(self, "login"):
            self.login.destroy()

        # Label to show information about the login whether the access is successful or not
        self.login = ctk.CTkLabel(self.frame, text=message, font=(font,12))
        self.login.place(rely=0.81, relx=0.5, anchor="center")

        if valid_request:
            Session.token = values["token"]
            Session.username = get_login
            RelaxApp_Structure.close_create(self, RelaxApp_User_Main_Menu, self.root, self.frame) 
        
    def sign_up(self):
        """Method to register users"""
        
        RelaxApp_Structure.close_create(self, RelaxApp_User_Registration, self.root, self.frame)

    def change_password(self):
        """Method to change password."""
        
        RelaxApp_Structure.close_create(self, RelaxApp_User_Change_Password, self.root, self.frame)


class RelaxApp_User_Registration():
    """This class opens a new window for users registrations."""

    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Top bar of the register menu.
        self.top_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                    corner_radius=10)
        self.top_bar.place(rely=0.02, relx=0.03)

        # Bottom bar of the register menu.
        self.bottom_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                       corner_radius=10)
        self.bottom_bar.place(rely=0.95, relx=0.03)

        # Label of the register menu.
        self.top_text = ctk.CTkLabel(self.frame, text="Complete todos los campos indicados:", font=(font,14))
        self.top_text.place(rely=0.08, relx=0.03)

        # Label to register the name.
        self.name = ctk.CTkLabel(self.frame, text="Nombre:", font=(font,14))
        self.name.place(rely=0.2, relx=0.03)

        # Name entry.
        self.name_entry = ctk.CTkEntry(self.frame, font=(font,14), width=180, height=10, corner_radius=10)
        self.name_entry.place(rely=0.2, relx=0.42)
        self.name_entry.bind("<Button-1>", lambda remove: self.name_entry.delete(0, tk.END))

        # Label to register the last name.
        self.last_name = ctk.CTkLabel(self.frame, text="Apellido:", font=(font,14))
        self.last_name.place(rely=0.3, relx=0.03)

        # Last name entry.
        self.last_name_entry = ctk.CTkEntry(self.frame, font=(font,14), width=180, height=10, corner_radius=10)
        self.last_name_entry.place(rely=0.3, relx=0.42)
        self.last_name_entry.bind("<Button-1>", lambda remove: self.last_name_entry.delete(0, tk.END))

        # Label to register the username.
        self.username = ctk.CTkLabel(self.frame, text="Nombre Usuario:", font=(font,14))
        self.username.place(rely=0.4, relx=0.03)

        # Username entry.
        self.username_entry = ctk.CTkEntry(self.frame, font=(font,14), width=180, height=10, corner_radius=10)
        self.username_entry.place(rely=0.4, relx=0.42)
        self.username_entry.bind("<Button-1>", lambda remove: self.username_entry.delete(0, tk.END))

        # Label to register the email.
        self.email = ctk.CTkLabel(self.frame, text="Email:", font=(font,14))
        self.email.place(rely=0.5, relx=0.03)
        
        # Email entry.
        self.email_entry = ctk.CTkEntry(self.frame, font=(font,14), width=180, height=10, corner_radius=10)
        self.email_entry.place(rely=0.5, relx=0.42)
        self.email_entry.bind("<Button-1>", lambda remove: self.email_entry.delete(0, tk.END))
                
        # Label to register the password.
        self.password = ctk.CTkLabel(self.frame, text="Contraseña:", font=(font,14))
        self.password.place(rely=0.6, relx=0.03)

        # Password entry.
        self.password_entry = ctk.CTkEntry(self.frame, font=(font,14), width=180, height=10, corner_radius=10,
                                           show="*")
        self.password_entry.place(rely=0.6, relx=0.42)
        self.password_entry.bind("<Button-1>", lambda remove: self.password_entry.delete(0, tk.END))

        # Button to accept the user registration.
        self.create_button = ctk.CTkButton(self.frame, text="Dar de Alta", font=(font,14), command= self.accept_sign_up,
                                           corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                           hover_color="#0a4e50")
        self.create_button.place(rely=0.75, relx=0.5, anchor="center")

        # Button to cancel the user registration.
        self.cancel_button = ctk.CTkButton(self.frame, text="Cancelar", font=(font,14), command= self.cancel_sign_up,
                                           corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                           hover_color=colors["dark_green"])
        self.cancel_button.place(rely=0.85, relx=0.5, anchor="center")

    def accept_sign_up(self):
        """Method to start user registration."""
        
        get_first_name = self.name_entry.get()
        get_last_name = self.last_name_entry.get()
        get_username = self.username_entry.get()
        get_email = self.email_entry.get()
        get_password = self.password_entry.get()

        data = {
            "first_name" : get_first_name,
            "last_name" : get_last_name,
            "username" : get_username,
            "email" : get_email,
            "password" : get_password,
        }
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_REGISTRATION
        RelaxApp_MessageBox_Options(self.root, self.frame, "Sign up", data=data, action="Accept", message=MB_message)

    def cancel_sign_up (self):
        """This method cancel the user registration and turns back to the main menu."""
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_REGISTRATION
        RelaxApp_MessageBox_Options(self.root, self.frame, "Cancel", action="Accept", message=MB_message)


class RelaxApp_User_Change_Password():
    """This class opens a new window to change the password."""

    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Top bar of the change password menu.
        self.top_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                    corner_radius=10)
        self.top_bar.place(rely=0.02, relx=0.03)

        # Bottom bar of the change password menu.
        self.bottom_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                       corner_radius=10)
        self.bottom_bar.place(rely=0.95, relx=0.03)

        # Label of the change password menu.
        self.top_text = ctk.CTkLabel(self.frame, text="Introduzca el correo vinculado a la cuenta:", font=(font,14))
        self.top_text.place(rely=0.1, relx=0.03)
        
        # Label to set the email.
        self.email = ctk.CTkLabel(self.frame, text="Email:", font=(font,14))
        self.email.place(rely=0.25, relx=0.03, anchor="w")
               
        # Username entry.
        self.email_entry = ctk.CTkEntry(self.frame, font=(font,14), width=230, height=10, corner_radius=10)
        self.email_entry.place(rely=0.25, relx=0.95, anchor="e")
        # self.email_entry.place(rely=0.2, relx=0.25, anchor="e")
        self.email_entry.bind("<Button-1>", lambda remove: self.email_entry.delete(0, tk.END))
        
        # Label of the change password menu.
        self.middle_text = ctk.CTkLabel(self.frame, text="Se le enviará un código de recuperación al correo indicado.", font=(font,14), 
                                        wraplength=335, justify="left")
        self.middle_text.place(rely=0.35, relx=0.03)

        # Button to send the code to change the password.
        self.change_pw_button = ctk.CTkButton(self.frame, text="Enviar código", font=(font,14), command= self.send_code,
                                              corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                              hover_color=colors["dark_green"])
        self.change_pw_button.place(rely=0.65, relx=0.5, anchor="center")

        # Button to cancel to change the password.
        self.cancel_change_pw_button = ctk.CTkButton(self.frame, text="Cancelar", font=(font,14), command= self.cancel_change_pw,
                                                     corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.cancel_change_pw_button.place(rely=0.75, relx=0.5, anchor="center")

    def send_code(self):
        """Method to send a code to start the change of the password."""

        get_email_pw_menu = self.email_entry.get()
        
        data = {"email" : get_email_pw_menu}
        
        # Request to reset the password is started.
        response_dict = comms.reset_password(data)
        response, message = Requests_Status.check_server_connection(response_dict) 

        if response != None:

            status_expected = 200
            valid_request, message = Requests_Status.check_request_status(response, status_expected, "send_code")

            if valid_request:
                # Second step to make a reset of the password is called.
                RelaxApp_Structure.close_create(self, RelaxApp_User_Confirm_Change_Password, self.root, self.frame, get_email_pw_menu)
            else:
                # Pop-up window is displayed error from serializers is displayed in Spanish.
                RelaxApp_MessageBox_Options(self.root, self.frame, "Invalid Change PW", action="Return", message=message)
               
        else:
            # Pop-up window error from the server connection is displayed in Spanish.
            RelaxApp_MessageBox_Options(self.root, self.frame, "Server Problem", action="Return", message=message)
             
    def cancel_change_pw (self):
        """This method cancel the change of password and turns back to the main menu."""
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_PW_CHANGE
        RelaxApp_MessageBox_Options(self.root, self.frame, "Cancel Change PW", action="Accept", message=MB_message)


class RelaxApp_User_Confirm_Change_Password():
    """This class opens a new window to confirm the change of the password."""

    def __init__(self, root, frame, email):
        self.root = root
        self.frame = frame
        self.email = email

        # Top bar of the change password menu.
        self.top_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                    corner_radius=10)
        self.top_bar.place(rely=0.02, relx=0.03)

        # Bottom bar of the change password menu.
        self.bottom_bar = ctk.CTkLabel(self.frame, text=None, fg_color=colors["dark_green"], width=310, height=0,
                                       corner_radius=10)
        self.bottom_bar.place(rely=0.95, relx=0.03)

        # Label of the change password menu.
        self.top_text = ctk.CTkLabel(self.frame, text="Introduzca el código que se ha enviado y cree la nueva contraseña:", 
                                     font=(font,14), wraplength=315, justify="left")
        self.top_text.place(rely=0.08, relx=0.03)

        # Label to set the code.
        self.code = ctk.CTkLabel(self.frame, text="Código Enviado:", font=(font,14))
        self.code.place(rely=0.25, relx=0.03)
        
        # Code entry.
        self.code_entry = ctk.CTkEntry(self.frame, font=(font,14), width=165, height=10, corner_radius=10)
        self.code_entry.place(rely=0.25, relx=0.47)
        self.code_entry.bind("<Button-1>", lambda remove: self.code_entry.delete(0, tk.END))

        # Label to set the new password.
        self.pw1 = ctk.CTkLabel(self.frame, text="Nueva Contraseña:", font=(font,14))
        self.pw1.place(rely=0.35, relx=0.03)

        # Password entry 1.
        self.pw1_entry = ctk.CTkEntry(self.frame, font=(font,14), width=165, height=10, corner_radius=10,
                                      show="*")
        self.pw1_entry.place(rely=0.35, relx=0.47)
        self.pw1_entry.bind("<Button-1>", lambda remove: self.pw1_entry.delete(0, tk.END))

        # Label to confirm the new password.
        self.pw2 = ctk.CTkLabel(self.frame, text="Repetir Contraseña:", font=(font,14))
        self.pw2.place(rely=0.45, relx=0.03)

        # Password entry 2.
        self.pw2_entry = ctk.CTkEntry(self.frame, font=(font,14), width=165, height=10, corner_radius=10,
                                      show="*")
        self.pw2_entry.place(rely=0.45, relx=0.47)
        self.pw2_entry.bind("<Button-1>", lambda remove: self.pw2_entry.delete(0, tk.END))

        # Button to confirm to change the password.
        self.change_pw_button = ctk.CTkButton(self.frame, text="Cambiar Contraseña", font=(font,14), command= self.accept_change_pw,
                                              corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                              hover_color=colors["dark_green"])
        self.change_pw_button.place(rely=0.65, relx=0.5, anchor="center")

        # Button to cancel to change the password.
        self.cancel_change_pw_button = ctk.CTkButton(self.frame, text="Cancelar", font=(font,14), command= self.cancel_change_pw,
                                                     corner_radius=90, width=100, height=20, hover=True, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.cancel_change_pw_button.place(rely=0.75, relx=0.5, anchor="center")

    def accept_change_pw(self):
        """Method to confirm the change of the password."""

        get_code_pw_menu = self.code_entry.get()
        get_password1_pw_menu = self.pw1_entry.get()
        get_password2_pw_menu = self.pw2_entry.get()
        
        data = {
            "email" : self.email,
            "code" : get_code_pw_menu,
            "password1" : get_password1_pw_menu,
            "password2" : get_password2_pw_menu
        }
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_ACCEPT_PW_CHANGE
        RelaxApp_MessageBox_Options(self.root, self.frame, "Confirm Change PW", data=data, action="Accept", message=MB_message)
 
    def cancel_change_pw (self):
        """This method cancel the change of password and turns back to the main menu."""
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_CONFIRM_CANCEL_PW_CHANGE
        RelaxApp_MessageBox_Options(self.root, self.frame, "Cancel Confirm Change PW", action="Accept", message=MB_message)
        

class RelaxApp_User_Main_Menu():
    """This class contains the user's main menu. It allows to start the app, set, save and load settings and knows about RelaxApp."""

    def __init__(self, root, frame):

        self.root = root
        self.frame = frame
        
        # Frame at the back.
        self.frame.configure(fg_color=colors["black"])

        # Frame at the top that contains menu options.
        self.frame_top_menu = ctk.CTkFrame(self.frame, height=30, width=340, fg_color=colors["soft_grey"],
                                           corner_radius=3)
        self.frame_top_menu.place(rely=0.0)

        # Main frame that contains all user options.
        self.frame_main = ctk.CTkFrame(self.frame, height=450, width=336, fg_color=colors["soft_grey"],
                                       corner_radius=10)
        self.frame_main.place(rely=0.07)

        # Archieve button menu.
        self.archieve_menu_button = tk.Menubutton(self.frame_top_menu, text="Archivo", font=(font,9), width=5,
                                                  height=2, background=colors["soft_grey"], foreground=colors["white"],
                                                  activebackground=colors["dark_green"], activeforeground=colors["white"])
        self.archieve_menu_button.place(rely=0.5, relx=0, anchor="w")

        # Help button menu.
        self.help_button = tk.Menubutton(self.frame_top_menu, text="Ayuda", font=(font,9), width=4,
                                         height=2, background=colors["soft_grey"], foreground=colors["white"],
                                         activebackground=colors["dark_green"], activeforeground=colors["white"])
        self.help_button.place(rely=0.5, relx=0.18, anchor="w")

        # Profile button menu.
        self.profile_button = tk.Menubutton(self.frame_top_menu, text="Cuenta", font=(font,9), width=4,
                                            height=2, background=colors["soft_grey"], foreground=colors["white"],
                                            activebackground=colors["dark_green"], activeforeground=colors["white"])
        self.profile_button.place(rely=0.5, relx=0.34, anchor="w")

        # Sign out button menu.
        self.sign_out_button = ctk.CTkButton(self.frame_top_menu, width=10, height=50, text="Cerrar Sesión",
                                             font=(font,12), command=self.sign_out, hover=True, fg_color=colors["soft_grey"],
                                             hover_color=colors["dark_green"])
        self.sign_out_button.place(rely=0.5, relx=1, anchor="e")

        # Archieve menu cascade.
        self.menu_archieve = tk.Menu(self.archieve_menu_button, tearoff=0)
        self.archieve_menu_button.config(menu=self.menu_archieve)

        # Help menu cascade.
        self.menu_help = tk.Menu(self.help_button, tearoff=0)
        self.help_button.config(menu=self.menu_help)

        # Profile menu cascade.
        self.menu_profile = tk.Menu(self.profile_button, tearoff=0)
        self.profile_button.config(menu=self.menu_profile)

        # Labels of archieve menu cascade.
        self.menu_archieve.add_command(label=" Importar Perfil  ", font=(font,9), command=self.import_profile,
                                       background=colors["soft_grey"], foreground=colors["white"], activebackground=colors["dark_green"],
                                       hidemargin=True)
        self.menu_archieve.add_command(label=" Exportar Perfil  ", font=(font,9), command=self.export_profile,
                                       background=colors["soft_grey"], foreground=colors["white"], activebackground=colors["dark_green"],
                                       hidemargin=True)

        # Label of help menu cascade.
        self.menu_help.add_command(label=" Conozca RelaxApp  ", font=(font,9), command=self.about_us, background=colors["soft_grey"],
                                   foreground=colors["white"], activebackground=colors["dark_green"], hidemargin=True)

        # Label of profile menu cascade.
        self.menu_profile.add_command(label=" Eliminar Cuenta  ", font=(font,9), command=self.remove_account, background=colors["soft_grey"],
                                      foreground=colors["white"], activebackground=colors["dark_green"], hidemargin=True)

        # Options label.
        self.options = ctk.CTkLabel(self.frame_main, text="Configurar", font=(font, 16), corner_radius=10, height=35)
        self.options.place(rely=0.2, relx=0.5, anchor="center")

        # Button to create profiles.
        self.profile_options = ctk.CTkButton(self.frame_main, text="Perfiles", font=(font, 14),
                                             command=self.create_profile, corner_radius=10, height=35,
                                             hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                             state="disabled")
        self.profile_options.place(rely=0.3, relx=0.25, anchor="w")

        # Variable to save the information of "profile_options_CB" when is marked or unmarked.
        self.profile_options_choice = ctk.IntVar()

        # Checkbox to activate or deactivate "profile_options".
        self.profile_options_CB = ctk.CTkCheckBox(self.frame_main, text=None, variable=self.profile_options_choice , width=20, height=20, hover=True,
                                                  command=self.checkbox_option1, state="disabled",
                                                  fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.profile_options_CB.place(rely=0.3, relx=0.8, anchor="e")

        # Button to set visual options.
        self.visual_options = ctk.CTkButton(self.frame_main, text="Descanso Visual", font=(font, 14),
                                            command=self.set_visual_options, corner_radius=10, height=35,
                                            hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.visual_options.place(rely=0.4, relx=0.25, anchor="w")

        # Variable to save the information of "visual_options_CB" when is marked or unmarked.
        self.visual_options_choice = ctk.IntVar()

        # Checkbox to activate or deactivate "visual_options".
        self.visual_options_CB = ctk.CTkCheckBox(self.frame_main, text=None, variable=self.visual_options_choice , width=20, height=20, hover=True,
                                                 command=self.checkbox_option2, fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.visual_options_CB.place(rely=0.4, relx=0.8, anchor="e")

        # Image of a restart simbol.
        self.restart_button = ctk.CTkImage(Image.open(os.path.join(image_path, "Restart.png")))

        # Button to restart VO values set.
        self.restart_button1 = ctk.CTkButton(self.frame_main, text=None, image=self.restart_button, width=20, height=20, hover=True,
                                             command=lambda: self.restart_values("VO"), fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.restart_button1.place(rely=0.4, relx=0.9, anchor="e")

        # Button to set stretch options.
        self.stretch_options = ctk.CTkButton(self.frame_main, text="Estirar", font=(font, 14),
                                             command=self.set_stretch_options, corner_radius=10, height=35,
                                             hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.stretch_options.place(rely=0.5, relx=0.25, anchor="w")

        # Variable to save the information of "stretch_options_CB" when is marked or unmarked.
        self.stretch_options_choice = ctk.IntVar()

        # Checkbox to activate or deactivate "stretch_options".
        self.stretch_options_CB = ctk.CTkCheckBox(self.frame_main, text=None, variable=self.stretch_options_choice, width=20, height=20, hover=True,
                                                  command=self.checkbox_option3,
                                                  fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.stretch_options_CB.place(rely=0.5, relx=0.8, anchor="e")

        # Button to restart SO values set.
        self.restart_button2 = ctk.CTkButton(self.frame_main, text=None, image=self.restart_button, width=20, height=20, hover=True,
                                             command=lambda: self.restart_values("SO"), fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.restart_button2.place(rely=0.5, relx=0.9, anchor="e")

        # Button to set sounds options.
        self.sounds_options = ctk.CTkButton(self.frame_main, text="Sonidos", font=(font, 14),
                                            command=self.set_sounds_options, corner_radius=10, height=35,
                                            hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.sounds_options.place(rely=0.6, relx=0.25, anchor="w")

        # Button to set start RelaxApp.
        self.start_relaxapp_button = ctk.CTkButton(self.frame_main, text="Iniciar", font=(font, 20),
                                                   command=self.start_relaxapp, height=70, corner_radius=50,
                                                   hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.start_relaxapp_button.place(rely=0.8, relx=0.5, anchor="center")
 
        self.update_profile_button()
        

    def get_profile_default(self, type):
        """This method gets the profile set as default if exists."""
        
        response_dict = comms.get_profiles()
        
        response, message = Requests_Status.check_server_connection(response_dict)

        if response != None:
            status_expected = 200
            valid_request, values, message = Requests_Status.check_request_status(response, status_expected, "get_profile_list")
           
            if valid_request:
                # Message when there´s no profile as default.
                if values["profiles_list"] == []:
                    if type == "export_profile":
                        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_EXPORT_EMPTY
                    elif type == "start_relaxapp":
                        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_STARTAPP_EMPTY
                        
                    RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=MB_message)
                
                # Default profile is returned.
                else:             
                    for profile in values["profiles_list"]:
                        if profile["default_profile"] == True:
                            
                            profile = {
                                "profile_name": profile["profile_name"],
                                "visual_configuration": profile["visual_configuration"],
                                "stretch_configuration": profile["stretch_configuration"],
                                "final_sounds_configuration": profile["final_sounds_configuration"],
                                "lapse_sounds_configuration": profile["lapse_sounds_configuration"]
                            }
                            return profile
        else:
            RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=message)

    def update_profile_button(self):
        """This method modify the state of the profile button."""

        # Profile button is set as active or deactive when there is at least one configuration set.
        if TemporaryProfile.visual_configuration != "" or TemporaryProfile.stretch_configuration != "":

            self.profile_options.configure(state="normal")
            self.profile_options_CB.configure(state="normal")
            return 
        
        len_profiles = RelaxApp_User_Main_Menu_Profiles.get_profile_list(self)

        # Profile button is set as active or deactive when a profile exists.
        if len(len_profiles) >= 1:
            self.profile_options.configure(state="normal")
            self.profile_options_CB.configure(state="normal")
            return
        
        self.profile_options.configure(state="disabled")
        self.profile_options_CB.configure(state="disabled")
       
    # Next 3 functions unmark values when user choose between use a profile or not.
    def checkbox_option1(self):
        self.visual_options_choice.set(0)
        self.stretch_options_choice.set(0)

    def checkbox_option2(self):
        self.profile_options_choice.set(0)

    def checkbox_option3(self):
        self.profile_options_choice.set(0)

    def create_profile(self):
        """This method creates profiles."""

        RelaxApp_User_Main_Menu_Profiles(self)

    def import_profile(self):
        """This method import a profile."""
      
        try:
            import_file = ctk.filedialog.askopenfilename(title="Importar Perfil")

            with open(import_file, mode="r", encoding="utf-8") as file:
                
                profile = json.load(file)
                
                # Sounds files are check if their exist in the system.
                valid_final_sounds_conf = Validate_CMD.validate_sound_path(profile["final_sounds_configuration"])
                valid_lapse_sounds_conf = Validate_CMD.validate_sound_path(profile["lapse_sounds_configuration"])
                
                if not valid_final_sounds_conf or not valid_lapse_sounds_conf:
                    print("* ERROR: The sound path given is invalid.")
                    message = messages.ERROR_VALIDATE_CMD_INVALID_SOUND_PATH
                    RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=message)
                    return
                
                response_dict = comms.create_profile(profile)
                
                response, message = Requests_Status.check_server_connection(response_dict)
                
                if response != None:                   
                    
                    status_expected = 201
                    valid_request, values, message = Requests_Status.check_request_status(response, status_expected, "import_profile")
                    if valid_request:
                        self.update_profile_button()
                        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_IMPORTED
                        RelaxApp_MessageBox_Options(self.root, self.frame, None, action="Return", message=MB_message)
                        return
                    else:
                        if values["error_type"] == "SERIALIZERS":
                            message = messages.ERROR_SERIALIZERS_PROFILE_IMPORT_ERROR
                        # Pop-up window is displayed error from serializers is displayed in Spanish.
                        RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=message)
                        return
                
                message = Set_Messages.server_messages(response_dict["error_link"])
        
                # Pop-up window error from the server connection is displayed in Spanish.
                RelaxApp_MessageBox_Options(self.root, self.frame, "Server Problem", action="Return", message=message)
     
        except json.JSONDecodeError:
            MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_INVALID
            RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=MB_message)
        
        except UnicodeDecodeError:
            MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_UNICODE_ERROR
            RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=MB_message)
            
        except OSError:
            MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_PROFILES_FILE_ERROR
            RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=MB_message)
   
    def export_profile(self):
        """This method saves profiles set as default."""
        
        profile = self.get_profile_default("export_profile")
      
        if profile:
            try:
                
                save_file = ctk.filedialog.asksaveasfilename(title="Exportar Perfil")
                # Bucle to go through each value saved in the profile.
                with open(save_file, mode="w", encoding="utf-8") as file:
                    json.dump(profile, file, indent=4, ensure_ascii=False)
                
            except OSError:
                pass

    def about_us(self):
        """This method open the webpage of RelaxApp."""
        webbrowser.open("https://github.com/L3chuS/Relaxapp.git")

    def remove_account(self):
        """This method removes profiles set."""
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_REMOVE_ACCOUNT.format(username=Session.username)
        RelaxApp_MessageBox_Options(self.root, self.frame, "Remove Account", action="Accept", message=MB_message)

    def sign_out(self):
        """This method signs out of the App."""
        
        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_SIGN_OUT.format(username=Session.username)
        RelaxApp_MessageBox_Options(self.root, self.frame, "Sign Out", action="Accept", message=MB_message)

    def set_visual_options(self):
        """This method sets visual options of the App."""
        
        self.visual_options_values = True
        RelaxApp_User_Main_Menu_Settings(self.root, self.frame, self, self.visual_options_values)

    def set_stretch_options(self):
        """This method sets stretch options of the App."""
        
        self.stretch_options_values = True
        RelaxApp_User_Main_Menu_Settings(self.root, self.frame, self, None, self.stretch_options_values)

    def restart_values(self, value):
        """This method restarts values set."""
        
        if value == "VO":
            TemporaryProfile.visual_configuration = ""
        elif value == "SO":
            TemporaryProfile.stretch_configuration = ""

        self.update_profile_button()
                
    def set_sounds_options(self):
        """This method sets sounds options of the App."""
        
        RelaxApp_User_Main_Menu_Sounds(self.frame)

    def start_relaxapp(self):
        """This method starts the App."""
        
        self.visual_set = False
        self.stretch_set = False
        self.value_VO = ""
        self.value_SO = ""

        MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_VALUES

        # Get if "self.visual_options_CB" is checked.
        if self.profile_options_choice.get() == 1:

            profile = self.get_profile_default("start_relaxapp")
           
            self.value_VO = profile["visual_configuration"]
            self.value_SO = profile["stretch_configuration"]
            
            if self.value_VO != "":
                self.visual_set = True
            if self.value_SO != "":
                self.stretch_set = True
            if self.value_VO == "" and self.value_SO == "":           
                RelaxApp_MessageBox_Options(self.root, self.frame, "start_relaxapp", action="Return", message=MB_message)
                return
            
            self.final_sound = profile["final_sounds_configuration"]
            self.lapse_sound = profile["lapse_sounds_configuration"]

        # Get if "self.visual_options_CB" is checked.
        if self.visual_options_choice.get() == 1:
            
            self.visual_set = True
            self.value_VO = TemporaryProfile.visual_configuration

            if self.value_VO == "":
                RelaxApp_MessageBox_Options(self.root, self.frame, "start_relaxapp", action="Return", message=MB_message)
                return

        # Get if "self.stretch_options_CB" is checked.
        if self.stretch_options_choice.get() == 1:
            
            self.stretch_set = True
            self.value_SO = TemporaryProfile.stretch_configuration

            if self.value_SO == "":
                RelaxApp_MessageBox_Options(self.root, self.frame, "start_relaxapp", action="Return", message=MB_message)
                return

        if self.visual_set == False and self.stretch_set == False:
            MB_message = messages.MESSAGE_RELAXAPP_MB_OPTIONS_STARTAPP_NO_SETTINGS
            RelaxApp_MessageBox_Options(self.root, self.frame, "start_relaxapp", action="Return", message=MB_message)
            return
            
        if self.visual_options_choice.get() == 1 or self.stretch_options_choice.get() == 1:
            
            self.final_sound = TemporaryProfile.final_sounds_configuration
            self.lapse_sound = TemporaryProfile.lapse_sounds_configuration

        RelaxApp_Structure.hide_unhide_window(self, self.root)
        RelaxApp_Running(self.root, self.frame, self.visual_set, self.stretch_set, self.value_VO, self.value_SO, self.final_sound, self.lapse_sound)


class RelaxApp_User_Main_Menu_Profiles(RelaxApp_User_Settings_Structure):
    """A new window is opened to set the user's personal profiles of the App. Inherit all structure from parent."""

    def __init__(self, instance):
        super().__init__()

        self.MM_instance = instance
        
        # Frame at the back.
        self.frame_User_SS.configure(fg_color=colors["black"])
        self.frame_User_SS.pack(pady=0, padx=0, fill="both")

        # Frame that contains the tittle of the class.
        self.frame1 = ctk.CTkFrame(self.frame_User_SS, height=50, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame1.pack(pady=10, padx=10)

        # Frame that contains the create and remove buttons.
        self.frame2 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame2.pack(pady=1, padx=10)

        # Frame that contains the first profile.
        self.frame3 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame3.pack(pady=1, padx=10)

        # Frame that contains the second profile.
        self.frame4 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame4.pack(pady=1, padx=10)

        # Frame that contains the third profile.
        self.frame5 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame5.pack(pady=1, padx=10)

        # Frame that contains the save and cancel buttons.
        self.frame6 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame6.pack(pady=10, padx=10)

        # Tittle label of the class.
        self.setting_title = ctk.CTkLabel(self.frame1, text="Perfil Predeterminado", font=(font, 15),
                                        corner_radius=5, fg_color=colors["soft_green"])
        self.setting_title.place(rely=0.5, relx=0.5, anchor="center")

        # Image of a create simbol.
        self.create_button = ctk.CTkImage(Image.open(os.path.join(image_path, "Create.png")))
        # Image of a remove simbol.
        self.remove_button = ctk.CTkImage(Image.open(os.path.join(image_path, "Remove.png")))

        # Button to create new profile.
        self.create_profile_button = ctk.CTkButton(self.frame2, text=None, image=self.create_button, width=0, command=self.create_profile,
                                                hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.create_profile_button.place(rely=0.5, relx=0.3, anchor="center")

        # Button to remove profile selected.
        self.remove_profile_button = ctk.CTkButton(self.frame2, text=None, image=self.remove_button, width=0, command=self.remove_profile,
                                                hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.remove_profile_button.place(rely=0.5, relx=0.7, anchor="center")

        # Save button.
        self.save_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Guardar", font=(font,14),
                                        command=self.save_settings, corner_radius=10, hover=True,
                                        fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.save_button.place(rely=0.5, relx=0.1, anchor="w")

        # Cancel button.
        self.cancel_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Cancelar", font=(font,14),
                                        command=self.cancel_settings, corner_radius=10, hover=True,
                                        fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.cancel_button.place(rely=0.5, relx=0.9, anchor="e")

        # Frames which will be cleaned when creating and removing profiles.
        self.dinamics_frames = (self.frame3, self.frame4, self.frame5)

        # Profile list is gotten to run or not the profile function.
        self.profile_list = self.get_profile_list()

        # Profiles are run if there's any.
        if self.profile_list == None:
            self.window_User_SS.destroy()
            return
        
        if len(self.profile_list) > 0:
            self.run_profiles(self.profile_list)
                  
    def get_profile_list(self):
        """This method gets all profiles names of the current user from the database."""

        response_dict = comms.get_profiles()
        
        response, message = Requests_Status.check_server_connection(response_dict)
        
        if response != None:
            status_expected = 200
            valid_request, values, message = Requests_Status.check_request_status(response, status_expected, "get_profile_list")
            
            if valid_request:
                return values["profiles_list"]
        
        RelaxApp_MessageBox_Options(self.frame_User_SS, self.window_User_SS, "Profile Error", action="Return", message=message)
            
    def get_profile_selected(self):
        """This method set the first profile and set it as default. Is used when none profiles is set as default."""

        profile_chosen = self.profile_choice.get()
        profile_ID = self.get_profiles_ID[profile_chosen]["id"]
            
        return profile_ID

    def create_RB_profile(self, profile_list, dinamics_frames, profile_choice):
        """This method creates the radio buttons based on the amount of profiles."""
        
        # Var to work with the radio buttons.
        self.profile_choice = ctk.IntVar(value=profile_choice)

        # Radio button 1 that contains the first profile set.
        profile_set1 = ctk.CTkRadioButton(dinamics_frames[0], text=None, value=0, variable=self.profile_choice, command=lambda:RelaxApp_User_Main_Menu_Profiles.get_profile_selected(self),
                                          hover=True, border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                          hover_color=colors["dark_green"])
        profile_set1.place(rely=0.5, relx=0.87, anchor="w")

        # Radio button 2 that contains the second profile set.
        if len(profile_list) > 1:
            profile_set2 = ctk.CTkRadioButton(dinamics_frames[1], text=None, value=1, variable=self.profile_choice, command=lambda:RelaxApp_User_Main_Menu_Profiles.get_profile_selected(self),
                                              hover=True, border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                              hover_color=colors["dark_green"])
            profile_set2.place(rely=0.5, relx=0.87, anchor="w")

        # Radio button 3 that contains the third profile set.
        if len(profile_list) > 2:
            profile_set3 = ctk.CTkRadioButton(dinamics_frames[2], text=None, value=2, variable=self.profile_choice, command=lambda:RelaxApp_User_Main_Menu_Profiles.get_profile_selected(self),
                                              hover=True, border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                              hover_color=colors["dark_green"])
            profile_set3.place(rely=0.5, relx=0.87, anchor="w")

    def run_profiles(self, profile_list):
        """This method writes all profiles set if there's any."""
        
        self.get_profiles_ID = []
        profile_choice = 0
        profile_counter = 0
        frame_counter = 3
        
        profile_list.reverse()
        
        for value in profile_list:
            if frame_counter == 3:
                frame = self.dinamics_frames[0]
            elif frame_counter == 4:
                frame = self.dinamics_frames[1]
            elif frame_counter == 5:
                frame = self.dinamics_frames[2]
                
            if value["default_profile"] == True:
                profile_choice = profile_counter
                
            self.get_profiles_ID.append({
                "id" : value["id"],
                "profile_name" : value["profile_name"]
            })
                
            profile_counter += 1
                
            profile_set = ctk.CTkLabel(frame, text=value["profile_name"], font=(font, 15))
            profile_set.place(rely=0.5, relx=0.02, anchor="w")
            frame_counter += 1

        if profile_list:
            RelaxApp_User_Main_Menu_Profiles.create_RB_profile(self, profile_list, self.dinamics_frames, profile_choice)

    def create_profile(self):
        """This method creates the profiles."""
        
        RelaxApp_Profile_Name(self, self.frame_User_SS, self.window_User_SS, self.dinamics_frames)
        
    def remove_profile(self):
        """This method removes the profile selected."""
        
        # The radiobutton is gotten to use it to get the profile ID.      
        profile_list = self.get_profile_list()
        
        if not profile_list:
            return

        profile_chosen = self.profile_choice.get()
        profile_ID = self.get_profiles_ID[profile_chosen]["id"]
        
        response_dict = comms.remove_profile(profile_ID)
        
        response, message = Requests_Status.check_server_connection(response_dict)
        
        if response != None:
            status_expected = 200
            valid_request, message = Requests_Status.check_request_status(response, status_expected, "remove_profile")
            if valid_request:
                self.MM_instance.update_profile_button()
                self.update_profiles()
                return 
    
        RelaxApp_MessageBox_Options(self.frame_User_SS, self.window_User_SS, "Profile Error", action="Return", message=message)
                
    def update_profiles(self):
        """This method updates the profile list."""
        
        profile_list = self.get_profile_list()                    
        RelaxApp_Structure.clean_MMP_widgets(self, self.dinamics_frames)
        self.run_profiles(profile_list)

    def save_settings(self):
        """This method saves the profile/s created and selected as default."""
        
        profile_list = self.get_profile_list()
        
        if profile_list:
            profile_ID = self.get_profile_selected()
            
            response_dict = comms.set_profile_dafault(profile_ID)
            
            response, message = Requests_Status.check_server_connection(response_dict)
            
            if response != None:
                status_expected = 200
                valid_request, message = Requests_Status.check_request_status(response, status_expected, "save_settings")
                if valid_request:
                    self.window_User_SS.destroy()
                    return

            RelaxApp_MessageBox_Options(self.frame_User_SS, self.window_User_SS, "Profile Error", action="Return", message=message)
        else:
            self.window_User_SS.destroy()
            
    def cancel_settings(self):
        """This method cancel the profile menu and close the window."""
        
        self.window_User_SS.destroy()
        

class RelaxApp_Profile_Name(RelaxApp_Profile_Name_Structure):
    """A new window is opened to set the user's personal profiles of the App. Inherit all structure from parent."""

    def __init__(self, profile, frame, window, dinamics_frames):
        super().__init__(frame)
        self.profile_menu = profile
        self.frame = frame
        self.window = window
        self.dinamics_frames = dinamics_frames

        # Image of an accept simbol.
        self.accept_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Accept.png")))
        # Image of a remove simbol.
        self.close_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Remove.png")))

        # Validate character limit.
        self.lenght_name = self.root.register(Validate_CMD.validate_lenght_name)

        # Profile name entry.
        self.profile_name_entry = ctk.CTkEntry(self.frame_PFS, font=(font,14), width=200, validate="key",
                                               validatecommand=(self.lenght_name, "%P"))
        self.profile_name_entry.place(rely=0.5, relx=0.01, anchor="w")
        self.profile_name_entry.insert(0, "Nombre del Perfil")
        self.profile_name_entry.bind("<Button-1>", lambda remove: self.profile_name_entry.delete(0, tk.END))

        # Accept button to create a profile.
        self.accept_button = ctk.CTkButton(self.frame_PFS, text=None, image=self.accept_image, width=0, command=self.accept,
                                           hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.accept_button.place(rely=0.5, relx=0.85, anchor="e")

        # Cancel button to not create a profile.
        self.close_button = ctk.CTkButton(self.frame_PFS, text=None, image=self.close_image, width=0, command=self.close,
                                          hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.close_button.place(rely=0.5, relx=0.99, anchor="e")

    def accept(self):
        """This method check the name given and create or not the new profile."""
        
        profile_name = self.profile_name_entry.get()
            
        data = {
            "profile_name" : profile_name,
            "visual_configuration" : TemporaryProfile.visual_configuration,
            "stretch_configuration" : TemporaryProfile.stretch_configuration,
            "final_sounds_configuration" : TemporaryProfile.final_sounds_configuration,
            "lapse_sounds_configuration" : TemporaryProfile.lapse_sounds_configuration
        }
        
        # Sounds files are check if their exist in the system.
        valid_final_sounds_conf = Validate_CMD.validate_sound_path(data["final_sounds_configuration"])
        valid_lapse_sounds_conf = Validate_CMD.validate_sound_path(data["lapse_sounds_configuration"])
                
        if not valid_final_sounds_conf or not valid_lapse_sounds_conf:
            print("* ERROR: The sound path given is invalid.")
            message = messages.ERROR_VALIDATE_CMD_INVALID_SOUND_PATH
            RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=message)
            return
        
        response_dict = comms.create_profile(data)
        
        response, message = Requests_Status.check_server_connection(response_dict)
        
        if response != None:
            status_expected = 201
            valid_request, message = Requests_Status.check_request_status(response, status_expected, "accept_profile_name")
            if valid_request:
                self.profile_menu.update_profiles()
                self.window_PFS.destroy()
                return
            else:
                # Pop-up window is displayed error from serializers is displayed in Spanish.
                RelaxApp_MessageBox_Options(self.root, self.frame, "Profile Error", action="Return", message=message)
                return
            
        message = Set_Messages.server_messages(response_dict["error_link"])
        
        # Pop-up window error from the server connection is displayed in Spanish.
        RelaxApp_MessageBox_Options(self.root, self.frame, "Server Problem", action="Return", message=message)
        
    def close(self):
        """This method cancel the profile name menu and returns to the profile menu."""
        
        self.window_PFS.destroy()


class RelaxApp_User_Main_Menu_Settings(RelaxApp_User_Settings_Structure):
    """A new window is opened to set the user's personal settings of the App. Inherit all structure from parent."""

    def __init__(self, root, frame, instance, visual_values=None, stretch_values=None):
        super().__init__()

        self.root = root
        self.frame = frame
        self.MM_instance = instance

        self.visual_options_values = visual_values
        self.stretch_options_values = stretch_values

        # An empty string which is going to save all values when user save a configuration.
        self.values = ""

        # Frame at the back.
        self.frame_User_SS.configure(fg_color=colors["black"])
        self.frame_User_SS.pack(pady=0, padx=0, fill="both")

        # Frame that contains the alert configuration label.
        self.frame1 = ctk.CTkFrame(self.frame_User_SS, height=50, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame1.pack(pady=10, padx=10)

        # Frame that contains the lenght configuration label.
        self.frame2 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame2.pack(pady=1, padx=10)

        # Frame that contains the lapse configuration label.
        self.frame3 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame3.pack(pady=1, padx=10)

        # Frame that contains the break time configuration label.
        self.frame4 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame4.pack(pady=1, padx=10)

        # Frame that contains the sound configuration checkbox.
        self.frame5 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame5.pack(pady=1, padx=10)

        # Frame that contains the save and cancel buttons.
        self.frame6 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame6.pack(pady=10, padx=10)

        # Alert configuration label.
        self.setting_title = ctk.CTkLabel(self.frame1, text="Configurar Alertas", font=(font, 15),
                                          corner_radius=5, fg_color=colors["soft_green"])
        self.setting_title.place(rely=0.5, relx=0.5, anchor="center")

        # Lenght label.
        self.lenght = ctk.CTkLabel(self.frame2, text="Duración", font=(font, 14))
        self.lenght.place(rely=0.5, relx=0.03, anchor="w")

        # Validate hours.
        self.hours_entry = self.root.register(Validate_CMD.validate_hours)

        # Validate minutes or seconds.
        self.min_sec_entry = self.root.register(Validate_CMD.validate_min_sec)

        # Lenght entry hours.
        self.lenght_entryHH = ctk.CTkEntry(self.frame2, font=(font,14), width=40, justify="center",
                                           validate="key", validatecommand=(self.hours_entry, "%P"))
        self.lenght_entryHH.place(rely=0.5, relx=0.76, anchor="e")
        self.lenght_entryHH.insert(0, "HH")
        self.lenght_entryHH.bind("<Button-1>", lambda remove: self.lenght_entryHH.delete(0, tk.END))

        # Two points separator.
        self.colon_lenght_entry = ctk.CTkLabel(self.frame2, text=":", font=(font, 14))
        self.colon_lenght_entry.place(rely=0.5, relx=0.79, anchor="e")

        # Lenght entry minutes.
        self.lenght_entryMM = ctk.CTkEntry(self.frame2, font=(font,14), width=40, justify="center",
                                           validate="key", validatecommand=(self.min_sec_entry, "%P"))
        self.lenght_entryMM.place(rely=0.5, relx=0.97, anchor="e")
        self.lenght_entryMM.insert(0, "MM")
        self.lenght_entryMM.bind("<Button-1>", lambda remove: self.lenght_entryMM.delete(0, tk.END))

        # Lapse label.
        self.lapse = ctk.CTkLabel(self.frame3, text="Intervalo Alertas", font=(font, 14))
        self.lapse.place(rely=0.5, relx=0.03, anchor="w")

        # Lapse entry.
        self.lapse_entry = ctk.CTkEntry(self.frame3, font=(font,14), width=40, justify="center",
                                        validate="key", validatecommand=(self.min_sec_entry, "%P"))
        self.lapse_entry.place(rely=0.5, relx=0.97, anchor="e")
        self.lapse_entry.insert(0, "MM")
        self.lapse_entry.bind("<Button-1>", lambda remove: self.lapse_entry.delete(0, tk.END))

        # Break time label.
        self.break_time = ctk.CTkLabel(self.frame4, text="Tiempo Descanso", font=(font, 14))
        self.break_time.place(rely=0.5, relx=0.03, anchor="w")

        # Break time entry minutes.
        self.break_time_entryMM = ctk.CTkEntry(self.frame4, font=(font,14), width=40, justify="center",
                                               validate="key", validatecommand=(self.min_sec_entry, "%P"))

        self.break_time_entryMM.place(rely=0.5, relx=0.76, anchor="e")
        self.break_time_entryMM.insert(0, "MM")
        self.break_time_entryMM.bind("<Button-1>", lambda remove: self.break_time_entryMM.delete(0, tk.END))

        # Two points separator.
        self.colon_break_time_entry = ctk.CTkLabel(self.frame4, text=":", font=(font, 14))
        self.colon_break_time_entry.place(rely=0.5, relx=0.79, anchor="e")

        # Break time entry seconds.
        self.break_time_entrySS = ctk.CTkEntry(self.frame4, font=(font,14), width=40, justify="center",
                                               validate="key", validatecommand=(self.min_sec_entry, "%P"))

        self.break_time_entrySS.place(rely=0.5, relx=0.97, anchor="e")
        self.break_time_entrySS.insert(0, "SS")
        self.break_time_entrySS.bind("<Button-1>", lambda remove: self.break_time_entrySS.delete(0, tk.END))

        # Sound alert label.
        self.sound_alert = ctk.CTkLabel(self.frame5, text="Activar Sonido", font=(font, 14))
        self.sound_alert.place(rely=0.5, relx=0.03, anchor="w")

        # Sound alert checkbox.
        self.sound_alert_choice = ctk.IntVar()
        self.sound_alert_CB = ctk.CTkCheckBox(self.frame5, text=None, variable=self.sound_alert_choice, width=20, height=20, hover=True,
                                              fg_color=colors["soft_green"], hover_color=colors["dark_green"])
        self.sound_alert_CB.place(rely=0.5, relx=1, anchor="e")

        # Save button.
        self.save_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Guardar", font=(font,14),
                                              command=self.save_settings, corner_radius=10, hover=True,
                                              fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.save_button.place(rely=0.5, relx=0.1, anchor="w")

        # Cancel button.
        self.cancel_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Cancelar", font=(font,14),
                                           command=self.cancel_settings, corner_radius=10, hover=True,
                                           fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.cancel_button.place(rely=0.5, relx=0.9, anchor="e")

    def save_settings(self):
        """This method saves settings in the user's main menu."""
        
        valid_values = False
        
        # Get when the sound checkbox is activated or not.
        if self.sound_alert_choice.get() == 1:
            self.sound = True
        else:
            self.sound = False

        lenght_HH = self.lenght_entryHH.get()
        lenght_MM = self.lenght_entryMM.get()
        lapse = self.lapse_entry.get()
        break_time_MM = self.break_time_entryMM.get()
        break_time_SS = self.break_time_entrySS.get()

        to_validate = lenght_HH + lenght_MM + lapse + break_time_MM + break_time_SS + str(self.sound)
        
        response_dict = comms.data_validate({"data": to_validate})

        response, message = Requests_Status.check_server_connection(response_dict)
        
        if response != None:
            status_expected = 200
            valid_request, message = Requests_Status.check_request_status(response, status_expected, "save_settings_MM")
            if valid_request:
                valid_values = True
            else:
                RelaxApp_MessageBox_Options(self.root, self.window_User_SS, "Invalid Data", action="Return", message=message)
        else:
            RelaxApp_MessageBox_Options(self.root, self.window_User_SS, "Server Problem", action="Return", message=message)

        # All entries are format to create the timer.
        if valid_values:

        # Convert 60 minutes in 1 hour.
            if lenght_MM == "60":
                lenght_MM = "00"
                lenght_HH = str(int(lenght_HH) + 1)
                if len(lenght_HH) == 1:
                    lenght_HH = "0" + str(lenght_HH)
            # Convert 60 seconds in 1 minute.
            if break_time_SS == "60":
                break_time_SS = "00"
                break_time_MM = str(int(break_time_MM) + 1)
                if len(break_time_MM) == 1:
                    break_time_MM = "0" + str(break_time_MM)

            # All entries are concatenated in one string.
            self.values += lenght_HH
            self.values += lenght_MM
            self.values += lapse
            self.values += break_time_MM
            self.values += break_time_SS
            self.values += str(self.sound)
        
            # Varible "self.values" is saved as a temporary configuration in TemporaryProfile.
            if self.visual_options_values == True: 
                TemporaryProfile.visual_configuration = self.values
            elif self.stretch_options_values == True:
                TemporaryProfile.stretch_configuration = self.values
            
            self.MM_instance.update_profile_button() 
            self.window_User_SS.destroy()

    def cancel_settings(self):
        """This method cancel the configuration and close the windows in the front."""
        
        self.window_User_SS.destroy()


class RelaxApp_User_Main_Menu_Sounds(RelaxApp_User_Settings_Structure):
    """This class opens a new window to set the user's personal sounds of the App. Inherit all structure from parent."""

    def __init__(self, root):
        super().__init__()
        self.root = root

        # An empty string which is going to save all values when user save a configuration.
        self.final_sound = ""
        self.lapse_sound = ""

        # Frame at the back.
        self.frame_User_SS.configure(fg_color=colors["black"])
        self.frame_User_SS.pack(pady=0, padx=0, fill="both")

        # Frame that contains the tittle of the window.
        self.frame1 = ctk.CTkFrame(self.frame_User_SS, height=50, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame1.pack(pady=10, padx=10)

        # Frame that contains the first sound to set.
        self.frame2 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame2.pack(pady=1, padx=10)

        # Frame that contains the second sound to set.
        self.frame3 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame3.pack(pady=1, padx=10)

        # Frame that contains the third sound to set.
        self.frame4 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame4.pack(pady=1, padx=10)

        # Frame that contains the fourth sound to set.
        self.frame5 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame5.pack(pady=1, padx=10)

        # Frame that contains the save and cancel buttons.
        self.frame6 = ctk.CTkFrame(self.frame_User_SS, height=40, width=250, fg_color=colors["soft_grey"], corner_radius=3)
        self.frame6.pack(pady=10, padx=10)

        # Tittle label.
        self.setting_title = ctk.CTkLabel(self.frame1, text="Configurar Sonidos", font=(font, 15),
                                          corner_radius=5, fg_color=colors["soft_green"])
        self.setting_title.place(rely=0.5, relx=0.5, anchor="center")

        # Image of a play simbol.
        self.play_button_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Play.png")).resize((40,40)))

        # Image of a play simbol.
        self.pause_button_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Pause.png")).resize((40,40)))

        # Sound by default 1 label.
        self.sound_alert_D1 = ctk.CTkLabel(self.frame2, text="Default 1", font=(font, 14))
        self.sound_alert_D1.place(rely=0.5, relx=0.03, anchor="w")

        # Button to play sound example.
        self.play_button_D1 = ctk.CTkButton(self.frame2, text=None, image=self.play_button_image, width=0, command=lambda: self.sound_default("Play", "Final"),
                                            hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.play_button_D1.place(rely=0.5, relx=0.35, anchor="w")

        # Button to pause sound example.
        self.pause_button_D1 = ctk.CTkButton(self.frame2, text=None, image=self.pause_button_image, width=0, command=lambda: self.sound_default("Pause", "Final"),
                                             hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.pause_button_D1.place(rely=0.5, relx=0.5, anchor="w")

        # Both variables get the selected choice by the user.
        self.sound_alert_choice1 = ctk.IntVar()
        self.sound_alert_choice2 = ctk.IntVar()

        # Checkbox to activate or deactivate sound by default 1 and set it as "final".
        self.sound_alert_D1_CB1 = ctk.CTkRadioButton(self.frame2, text=None, value=0, variable=self.sound_alert_choice1, hover=True,
                                                     border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.sound_alert_D1_CB1.place(rely=0.5, relx=0.72, anchor="w")

        # Checkbox to activate or deactivate sound by default 1 and set it as "lapse".
        self.sound_alert_D1_CB2 = ctk.CTkRadioButton(self.frame2, text=None, value=0, variable=self.sound_alert_choice2, hover=True,
                                                     border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.sound_alert_D1_CB2.place(rely=0.5, relx=0.87, anchor="w")

        # Sound by default 2 label.
        self.sound_alert_D2 = ctk.CTkLabel(self.frame3, text="Default 2", font=(font, 14))
        self.sound_alert_D2.place(rely=0.5, relx=0.03, anchor="w")

        # Button to play sound example.
        self.play_button_D2 = ctk.CTkButton(self.frame3, text=None, image=self.play_button_image, width=0, command=lambda: self.sound_default("Play", "Lapse"),
                                            hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.play_button_D2.place(rely=0.5, relx=0.35, anchor="w")

        # Button to pause sound example.
        self.pause_button_D2 = ctk.CTkButton(self.frame3, text=None, image=self.pause_button_image, width=0, command=lambda: self.sound_default("Pause", "Lapse"),
                                             hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.pause_button_D2.place(rely=0.5, relx=0.5, anchor="w")

        # Checkbox to activate or deactivate sound by default 2 and set it as "final".
        self.sound_alert_D2_CB1 = ctk.CTkRadioButton(self.frame3, text=None, value=1, variable=self.sound_alert_choice1, hover=True,
                                                     border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.sound_alert_D2_CB1.place(rely=0.5, relx=0.72, anchor="w")

        # Checkbox to activate or deactivate sound by default 2 and set it as "lapse".
        self.sound_alert_D2_CB2 = ctk.CTkRadioButton(self.frame3, text=None, value=1, variable=self.sound_alert_choice2, hover=True,
                                                     border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                     hover_color=colors["dark_green"])
        self.sound_alert_D2_CB2.place(rely=0.5, relx=0.87, anchor="w")

        # Sound load 1 label.
        self.sound_alert_load1 = ctk.CTkButton(self.frame4, width=10, height=10, text="Cargar 1", font=(font, 14), command=lambda: self.sound_load("1"),
                                               corner_radius=10, hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.sound_alert_load1.place(rely=0.5, anchor="w")

        # Button to play sound example.
        self.play_button_load1 = ctk.CTkButton(self.frame4, text=None, image=self.play_button_image, width=0, command=lambda: self.sound_loaded("Play", "1"),
                                               hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.play_button_load1.place(rely=0.5, relx=0.35, anchor="w")

        # Button to pause sound example.
        self.pause_button_load1 = ctk.CTkButton(self.frame4, text=None, image=self.pause_button_image, width=0, command=lambda: self.sound_loaded("Pause", "1"),
                                                hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.pause_button_load1.place(rely=0.5, relx=0.5, anchor="w")

        # Checkbox to activate or deactivate sound loaded 2 and set it as "final".
        self.sound_alert_load1_CB1 = ctk.CTkRadioButton(self.frame4, text=None, value=2, variable=self.sound_alert_choice1, hover=True,
                                                        border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                        hover_color=colors["dark_green"])
        self.sound_alert_load1_CB1.place(rely=0.5, relx=0.72, anchor="w")

        # Checkbox to activate or deactivate sound loaded 2 and set it as "lapse".
        self.sound_alert_load1_CB2 = ctk.CTkRadioButton(self.frame4, text=None, value=2, variable=self.sound_alert_choice2, hover=True,
                                                        border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                        hover_color=colors["dark_green"])
        self.sound_alert_load1_CB2.place(rely=0.5, relx=0.87, anchor="w")

        # Sound load 2 label.
        self.sound_alert_load2 = ctk.CTkButton(self.frame5, width=10, height=10, text="Cargar 2", font=(font, 14), command=lambda: self.sound_load("2"),
                                               corner_radius=10, hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.sound_alert_load2.place(rely=0.5, anchor="w")

        # Button to play sound example.
        self.play_button_load2 = ctk.CTkButton(self.frame5, text=None, image=self.play_button_image, width=0, command=lambda: self.sound_loaded("Play", "2"),
                                               hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.play_button_load2.place(rely=0.5, relx=0.35, anchor="w")

        # Button to pause sound example.
        self.pause_button_load2 = ctk.CTkButton(self.frame5, text=None, image=self.pause_button_image, width=0, command=lambda: self.sound_loaded("Pause", "2"),
                                                hover=True, fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.pause_button_load2.place(rely=0.5, relx=0.5, anchor="w")

        # Checkbox to activate or deactivate sound loaded 2 and set it as "final".
        self.sound_alert_load2_CB1 = ctk.CTkRadioButton(self.frame5, text=None, value=3, variable=self.sound_alert_choice1, hover=True,
                                                        border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                        hover_color=colors["dark_green"])
        self.sound_alert_load2_CB1.place(rely=0.5, relx=0.72, anchor="w")

        # Checkbox to activate or deactivate sound loaded 2 and set it as "lapse".
        self.sound_alert_load2_CB2 = ctk.CTkRadioButton(self.frame5, text=None, value=3, variable=self.sound_alert_choice2, hover=True,
                                                        border_width_unchecked=2, border_width_checked=5, fg_color=colors["soft_green"],
                                                        hover_color=colors["dark_green"])
        self.sound_alert_load2_CB2.place(rely=0.5, relx=0.87, anchor="w")

        # Save button.
        self.save_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Guardar", font=(font,14),
                                         command=self.save_settings, corner_radius=10, hover=True,
                                         fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.save_button.place(rely=0.5, relx=0.1, anchor="w")

        # Cancel button.
        self.cancel_button = ctk.CTkButton(self.frame6, width=10, height=10, text="Cancelar", font=(font,14),
                                           command=self.cancel_settings, corner_radius=10, hover=True,
                                           fg_color=colors["soft_grey"], hover_color=colors["dark_green"])
        self.cancel_button.place(rely=0.5, relx=0.9, anchor="e")

        # An information is showed when mouse is over "Configurar Sonidos".
        ToolTip(self.setting_title, msg=messages.MESSAGE_RELAXAPP_USER_MM_SOUNDS_TOOLTIP, parent_kwargs = { "bg": colors["black"]}, delay=0.5, font=(font,11), fg=colors["white"], bg=colors["soft_grey"], padx=10, pady=10)

    def sound_default(self, action, sound):
        """This method runs and stop defaults sounds."""
        
        pygame.mixer.init()
        if action == "Play":
            if sound == "Final":
                pygame.mixer.music.load(os.path.join(sounds_path, "Final.mp3"))
            elif sound == "Lapse":
                pygame.mixer.music.load(os.path.join(sounds_path, "Lapse.mp3"))

            pygame.mixer.music.play(loops=0)
        elif action == "Pause":
            pygame.mixer.quit()

    def sound_load(self, value):
        """This method loads sounds."""
        
        if value == "1":
            self.sound_loaded1_path = ctk.filedialog.askopenfilename(title="Cargar Sonido Final", filetypes=audio_accepted_files)
        elif value == "2":
            self.sound_loaded2_path = ctk.filedialog.askopenfilename(title="Cargar Sonido Alerta", filetypes=audio_accepted_files)

    def sound_loaded(self, action, value):
        """This method runs and stops loaded sounds."""
        
        try:
            pygame.mixer.init()
            if action == "Play" and value == "1":
                pygame.mixer.music.load(self.sound_loaded1_path)
                pygame.mixer.music.play(loops=0)
            elif action == "Play" and value == "2":
                pygame.mixer.music.load(self.sound_loaded2_path)
                pygame.mixer.music.play(loops=0)
            elif action == "Pause":
                pygame.mixer.quit()
        except:
            pass

    def save_settings(self):
        """This method saves the configuration."""
        
        try:
            # Final sound is choosen.
            if self.sound_alert_choice1.get() == 0:
                self.final_sound = os.path.join(sounds_path, "Final.mp3")
            elif self.sound_alert_choice1.get() == 1:
                self.final_sound = os.path.join(sounds_path, "Lapse.mp3")
            elif self.sound_alert_choice1.get() == 2:
                self.final_sound = self.sound_loaded1_path
            elif self.sound_alert_choice1.get() == 3:
                self.final_sound = self.sound_loaded2_path
        except:
            self.final_sound = ""

        try:
            # Lapse sound is choosen.
            if self.sound_alert_choice2.get() == 0:
                self.lapse_sound = os.path.join(sounds_path, "Final.mp3")
            elif self.sound_alert_choice2.get() == 1:
                self.lapse_sound = os.path.join(sounds_path, "Lapse.mp3")
            elif self.sound_alert_choice2.get() == 2:
                self.lapse_sound = self.sound_loaded1_path
            elif self.sound_alert_choice2.get() == 3:
                self.lapse_sound = self.sound_loaded2_path
        except:
            self.lapse_sound = ""

        # MessageBox is called when user try to save a configuration with a loaded sound before loading.
        if self.final_sound == "" or self.lapse_sound == "":
            MB_message = messages.MESSAGE_RELAXAPP_USER_MM_SOUNDS_NO_SOUND
            RelaxApp_MessageBox_Options(self.root, self.window_User_SS, "No Sound", action="Return", message=MB_message)
        else:
            TemporaryProfile.final_sounds_configuration = self.final_sound
            TemporaryProfile.lapse_sounds_configuration = self.lapse_sound
            self.window_User_SS.destroy()  
        pygame.mixer.quit()
        
    def cancel_settings(self):
        """This method cancel the configuration to returns to the main menu."""
        
        pygame.mixer.quit()
        self.window_User_SS.destroy()

    def show_info(self ,text):
        """This method shows information about how to use the sound settings."""
        
        self.text = text
        ctk.CTkLabel(self.root, text=f' "{self.text}" ', font=("Segoe Print", 22),
        fg_color=colors["soft_grey"]).pack()


class RelaxApp_Running(RelaxApp_Running_Structure):
    """This class start RelaxApp. All countdown are executed depending on previus values choosen. Inherit all structure from parent."""

    def __init__(self, root, frame, visual_set, stretch_set, value_VO, value_SO, final_sound, lapse_sound):

        super().__init__()

        self.root = root
        self.frame = frame
        pygame.mixer.init()
        self.start_time = time.perf_counter()

        # Variables to set which threading is started.
        self.visual_set = visual_set
        self.stretch_set = stretch_set
        self.value_VO = value_VO
        self.value_SO = value_SO
        self.final_sound = final_sound
        self.lapse_sound = lapse_sound

        # Variable to stop bucles when return button is used after countdown is finished.
        self.app_running = True
        # Variables to stop bucles when function TR_VO_countdown or TR_SO_countdown are finished.
        self.stop_countdown_VO = False
        self.stop_countdown_SO = False

        # Dictionary that contains each value of user's visual options settings.
        self.values_VO = {"time_left_HH" : self.value_VO[0:2],
                          "time_left_MM" : self.value_VO[2:4],
                          "next_alert_MM" : self.value_VO[4:6],
                          "breaktime_MM" : self.value_VO[6:8],
                          "breaktime_SS" : self.value_VO[8:10],
                          "sound_active" : self.value_VO[10::]}

        # Dictionary that contains each value of user's stretch options settings.
        self.values_SO = {"time_left_HH" : self.value_SO[0:2],
                          "time_left_MM" : self.value_SO[2:4],
                          "next_alert_MM" : self.value_SO[4:6],
                          "breaktime_MM" : self.value_SO[6:8],
                          "breaktime_SS" : self.value_SO[8:10],
                          "sound_active" : self.value_SO[10::]}

        # Initial values of all visual options settings.
        self.time_left_HH_VO = ctk.StringVar(value=self.values_VO["time_left_HH"])
        self.time_left_MM_VO = ctk.StringVar(value=self.values_VO["time_left_MM"])
        self.next_alert_MM_VO = ctk.StringVar(value=self.values_VO["next_alert_MM"])
        self.next_alert_SS_VO = ctk.StringVar(value="00")
        self.breaktime_MM_VO = ctk.StringVar(value=self.values_VO["breaktime_MM"])
        self.breaktime_SS_VO = ctk.StringVar(value=self.values_VO["breaktime_SS"])
        self.sound_active_VO = ctk.StringVar(value=self.values_VO["sound_active"])

        # Initial values of all stretch options settings.
        self.time_left_HH_SO = ctk.StringVar(value=self.values_SO["time_left_HH"])
        self.time_left_MM_SO = ctk.StringVar(value=self.values_SO["time_left_MM"])
        self.next_alert_MM_SO = ctk.StringVar(value=self.values_SO["next_alert_MM"])
        self.next_alert_SS_SO = ctk.StringVar(value="00")
        self.breaktime_MM_SO = ctk.StringVar(value=self.values_SO["breaktime_MM"])
        self.breaktime_SS_SO = ctk.StringVar(value=self.values_SO["breaktime_SS"])
        self.sound_active_SO = ctk.StringVar(value=self.values_SO["sound_active"])

        # Varibales that get the sound value set to active or deactive sound alert.
        self.sound_VO = self.sound_active_VO.get()
        self.sound_SO = self.sound_active_SO.get()

        # Variables that set the position in "Y" when both visual options and stretch options are active.
        self.frame_visual_rely = 0.25
        self.frame_stretch_rely = 0.62
        self.stretch_title_rely = 0.44

        # Variables that set the position in "Y" when visual options is deactive and stretch options is active.
        if self.visual_set == False and self.stretch_set == True:
            self.frame_stretch_rely = 0.25
            self.stretch_title_rely = 0.07

        if self.visual_set == True:
            # Frame that contains visual options.
            self.frame_visual = ctk.CTkFrame(self.frame_RS, height=100, width=250, fg_color=colors["black"],
                                                corner_radius=10)
            self.frame_visual.place(rely=self.frame_visual_rely, relx=0.5, anchor="center")

            # Main title of the frame.
            self.visual_title = ctk.CTkLabel(self.frame_RS, text="Descanso Visual", font=(font, 16))
            self.visual_title.place(rely=0.07, relx=0.5, anchor="center")

            # Vertical bar between time left and alert.
            self.bar_VO = ctk.CTkLabel(self.frame_visual, text=None, width=4, height=100, fg_color=colors["soft_grey"])
            self.bar_VO.place(relx=0.61)

            # Time left title.
            self.time_left_title_VO = ctk.CTkLabel(self.frame_visual, text="Tiempo Restante", font=(font, 14))
            self.time_left_title_VO.place(rely=0.15, relx=0.04, anchor="w")

            # Labels that contains "HH", ":" and "MM" of the time left.
            self.time_left_HH_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.time_left_HH_VO, font=(font, 24))
            self.time_left_HH_VO_label.place(rely=0.5, relx=0.11, anchor="w")

            self.colon_VO_1 = ctk.CTkLabel(self.frame_visual, text=":", font=(font, 28))
            self.colon_VO_1.place(rely=0.5, relx=0.27, anchor="w")

            self.time_left_MM_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.time_left_MM_VO, font=(font, 24))
            self.time_left_MM_VO_label.place(rely=0.5, relx=0.32, anchor="w")

            # Next alert title.
            self.next_alert_title_VO = ctk.CTkLabel(self.frame_visual, text="Alerta", font=(font, 14), justify="center")
            self.next_alert_title_VO.place(rely=0.15, relx=0.96, anchor="e")

            # Labels that contains "MM", ":" and "SS" of the next alert.
            self.next_alert_MM_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.next_alert_MM_VO, font=(font, 16))
            self.next_alert_MM_VO_label.place(rely=0.4, relx=0.81, anchor="e")

            self.colon_VO_2 = ctk.CTkLabel(self.frame_visual, text=":", font=(font, 16))
            self.colon_VO_2.place(rely=0.4, relx=0.85, anchor="e")

            self.next_alert_SS_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.next_alert_SS_VO, font=(font, 16))
            self.next_alert_SS_VO_label.place(rely=0.4, relx=0.96, anchor="e")

            # Break time title.
            self.breaktime_title_VO = ctk.CTkLabel(self.frame_visual, text="Descanso", font=(font, 14), justify="center")
            self.breaktime_title_VO.place(rely=0.6, relx=0.96, anchor="e")

            # Labels that contains "MM", ":" and "SS" of the break time.
            self.breaktime_MM_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.breaktime_MM_VO, font=(font, 16))
            self.breaktime_MM_VO_label.place(rely=0.8, relx=0.81, anchor="e")

            self.colon_VO_3 = ctk.CTkLabel(self.frame_visual, text=":", font=(font, 16))
            self.colon_VO_3.place(rely=0.8, relx=0.85, anchor="e")

            self.breaktime_SS_VO_label = ctk.CTkLabel(self.frame_visual, textvariable=self.breaktime_SS_VO, font=(font, 16))
            self.breaktime_SS_VO_label.place(rely=0.8, relx=0.96, anchor="e")

        if self.stretch_set == True:
            # Frame that contains stretch options.
            self.frame_stretch = ctk.CTkFrame(self.frame_RS, height=100, width=250, fg_color=colors["black"],
                                                corner_radius=10)
            self.frame_stretch.place(rely=self.frame_stretch_rely, relx=0.5, anchor="center")

            # Main title of the frame.
            self.stretch_title = ctk.CTkLabel(self.frame_RS, text="Estirar", font=(font, 16))
            self.stretch_title.place(rely=self.stretch_title_rely, relx=0.5, anchor="center")

            # Vertical bar between time left and alert.
            self.bar_SO = ctk.CTkLabel(self.frame_stretch, text=None, width=4, height=100, fg_color=colors["soft_grey"])
            self.bar_SO.place(relx=0.61)

            # Time left title.
            self.time_left_title_SO = ctk.CTkLabel(self.frame_stretch, text="Tiempo Restante", font=(font, 14))
            self.time_left_title_SO.place(rely=0.15, relx=0.04, anchor="w")

            # Labels that contains "HH", ":" and "MM" of the time left.
            self.time_left_HH_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.time_left_HH_SO, font=(font, 24))
            self.time_left_HH_SO_label.place(rely=0.5, relx=0.11, anchor="w")

            self.colon_SO_1 = ctk.CTkLabel(self.frame_stretch, text=":", font=(font, 28))
            self.colon_SO_1.place(rely=0.5, relx=0.27, anchor="w")

            self.time_left_MM_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.time_left_MM_SO, font=(font, 24))
            self.time_left_MM_SO_label.place(rely=0.5, relx=0.32, anchor="w")

            # Next alert title.
            self.next_alert_title_SO = ctk.CTkLabel(self.frame_stretch, text="Alerta", font=(font, 14), justify="center")
            self.next_alert_title_SO.place(rely=0.15, relx=0.96, anchor="e")

            # Labels that contains "MM", ":" and "SS" of the next alert.
            self.next_alert_MM_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.next_alert_MM_SO, font=(font, 16))
            self.next_alert_MM_SO_label.place(rely=0.4, relx=0.81, anchor="e")

            self.colon_SO_2 = ctk.CTkLabel(self.frame_stretch, text=":", font=(font, 16))
            self.colon_SO_2.place(rely=0.4, relx=0.85, anchor="e")

            self.next_alert_SS_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.next_alert_SS_SO, font=(font, 16))
            self.next_alert_SS_SO_label.place(rely=0.4, relx=0.96, anchor="e")

            # Break time title.
            self.breaktime_title_SO = ctk.CTkLabel(self.frame_stretch, text="Descanso", font=(font, 14), justify="center")
            self.breaktime_title_SO.place(rely=0.6, relx=0.96, anchor="e")

            # Labels that contains "MM", ":" and "SS" of the break time.
            self.breaktime_MM_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.breaktime_MM_SO, font=(font, 16))
            self.breaktime_MM_SO_label.place(rely=0.8, relx=0.81, anchor="e")

            self.colon_SO_3 = ctk.CTkLabel(self.frame_stretch, text=":", font=(font, 16))
            self.colon_SO_3.place(rely=0.8, relx=0.85, anchor="e")

            self.breaktime_SS_SO_label = ctk.CTkLabel(self.frame_stretch, textvariable=self.breaktime_SS_SO, font=(font, 16))
            self.breaktime_SS_SO_label.place(rely=0.8, relx=0.96, anchor="e")

        # Hidden button that init the countdown when this class is called.
        self.start = ctk.CTkButton(self.window_RS, text=None, command=self.threading(), hover=False, fg_color=colors["soft_grey"],
                                   bg_color=colors["soft_grey"])
        self.start.place(rely=0.9, relx=0.5, anchor="center")

        # Button that returns to the user's main menu.
        self.stop = ctk.CTkButton(self.window_RS, text="Volver", font=(font, 14), command=self.stop_app, width=80, height=20,
                                  corner_radius=10, hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                  bg_color=colors["soft_grey"])
        self.stop.place(rely=0.85, relx=0.1, anchor="w")

        # Button that stop music when is playing.
        self.pause_alarm = ctk.CTkButton(self.window_RS, text="Silenciar", font=(font, 14), command=self.stop_sound, width=60, height=20,
                                  corner_radius=10, hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                  bg_color=colors["soft_grey"])
        self.pause_alarm.place(rely=0.85, relx=0.9, anchor="e")

        # This variables are counting how many round have been lunched.
        self.init_TR_VO_multiplier = 0
        self.init_TR_SO_multiplier = 0
        self.init_VO_countdown_multiplier = 0
        self.init_SO_countdown_multiplier = 0

    def threading(self):
        """This method calls 4 of the 6 countdown."""

        # Call all countdown funtions.
        if self.visual_set == True:
            t1=threading.Thread(target=self.TR_VO_countdown)
            t1.start()
            t2= threading.Thread(target=self.NA_VO_countdown)
            t2.start()

        if self.stretch_set == True:
            t3=threading.Thread(target=self.TR_SO_countdown)
            t3.start()
            t4=threading.Thread(target=self.NA_SO_countdown)
            t4.start()

    def TR_VO_countdown(self):
        """This method starts the main countdown "Time Remaining" of the visual options."""

        # Hours and minutes of time remaining are gotten.
        TR_HH_value = int(self.time_left_HH_VO.get())
        TR_MM_value = int(self.time_left_MM_VO.get())

        while True:
            # This variable change when return button is pressed to stop or not the app.
            if self.app_running == False:
                self.stop_countdown_VO = True
                break
            else:
                # Verify if values have one or two digits in order to add a "0" in front.
                if TR_MM_value > 9:
                    self.time_left_MM_VO.set(TR_MM_value)
                else:
                    self.time_left_MM_VO.set("0" + str(TR_MM_value))
                if TR_HH_value > 9:
                    self.time_left_HH_VO.set(TR_HH_value)
                else:
                    self.time_left_HH_VO.set("0" + str(TR_HH_value))

                self.init_timer(60, "TR_VO")
                if TR_MM_value > 0:
                    TR_MM_value -= 1
                # When minute is cero one is subtracted from the hours.
                elif TR_HH_value > 0:
                    TR_HH_value -= 1
                    TR_MM_value = 59
                # When the main countdown is 0 all label change.
                if TR_HH_value == 0 and TR_MM_value == 0:
                    # Sound alert is called.
                    if self.sound_VO == "True":
                        self.play_sounds(1)
                    # Hours,minutes and colon of time remaining are hidden.
                    self.time_left_HH_VO.set("")
                    self.time_left_MM_VO.set("")
                    self.colon_VO_1.place_forget()
                    # New label is set to show that the countdown is finished.
                    finished_label_VO = ctk.CTkLabel(self.frame_visual, text="Finalizado", font=(font, 20), corner_radius=5,
                                                    fg_color=colors["soft_green"])
                    finished_label_VO.place(rely=0.55, relx=0.06, anchor="w")
                    # All label are set as "00"
                    self.next_alert_MM_VO.set("00")
                    self.next_alert_SS_VO.set("00")
                    self.breaktime_MM_VO.set("00")
                    self.breaktime_SS_VO.set("00")
                    # Varible change to stop next alert and break time countdowns.
                    self.stop_countdown_VO = True
                    break

    def NA_VO_countdown(self):
        """This method starts the countdown "Next Alert" of the visual options."""

        # Minutes and seconds of next alert are gotten.
        initial_value_MM = self.next_alert_MM_VO.get()
        initial_value_SS = self.next_alert_SS_VO.get()

        NA_MM_value = int(initial_value_MM)
        NA_SS_value = int(initial_value_SS)

        while NA_MM_value > -1:

            # Conditional that stop bucle when return button is pressed or time remaining is finished.
            if self.app_running == False or self.stop_countdown_VO == True:
                break
            # Verify if values have one or two digits in order to add a "0" in front.
            elif NA_SS_value > 9:
                self.next_alert_SS_VO.set(NA_SS_value)
            else:
                self.next_alert_SS_VO.set("0" + str(NA_SS_value))
            if NA_MM_value > 9:
                self.next_alert_MM_VO.set(NA_MM_value)
            else:
                self.next_alert_MM_VO.set("0" + str(NA_MM_value))

            # After 1 second one is subtracted from the seconds.
            if NA_SS_value > 0:
                self.init_timer(1, "VO_countdown")
                NA_SS_value -= 1
            # When second is cero one is subtracted from the minutes.
            elif NA_MM_value > 0:
                self.init_timer(1, "VO_countdown")
                NA_MM_value -= 1
                NA_SS_value = 59
            else:
                # Sound alert is called.
                if self.sound_VO == "True":
                    self.play_sounds(2)
                # Minutes and second are set as there was at the beggining.
                self.next_alert_SS_VO.set(initial_value_SS)
                self.next_alert_MM_VO.set(initial_value_MM)
                # New threading is run to start BT_VO_countdown function.
                threading.Thread(target=self.BT_VO_countdown).start()
                break

    def BT_VO_countdown(self):
        """This method starts the countdown "Break Time" of the visual options."""

        # Minutes and seconds of next alert are gotten.
        initial_value_MM = self.breaktime_MM_VO.get()
        initial_value_SS = self.breaktime_SS_VO.get()

        BT_MM_value = int(initial_value_MM)
        BT_SS_value = int(initial_value_SS)

        while BT_MM_value > -1:
            # Conditional that stop bucle when return button is pressed or time remaining is finished.
            if self.app_running == False or self.stop_countdown_VO == True:
                break

            # Verify if values have one or two digits in order to add a "0" in front.
            if BT_MM_value > 9:
                self.breaktime_MM_VO.set(BT_MM_value)
            else:
                self.breaktime_MM_VO.set("0" + str(BT_MM_value))
            if BT_SS_value > 9:
                self.breaktime_SS_VO.set(BT_SS_value)
            else:
                self.breaktime_SS_VO.set("0" + str(BT_SS_value))

            # After 1 second one is subtracted from the seconds.
            if BT_SS_value > 0:
                self.init_timer(1, "VO_countdown")
                BT_SS_value -= 1
            # When second is cero one is subtracted from the minutes.
            elif BT_MM_value > 0:
                self.init_timer(1, "VO_countdown")
                BT_MM_value -= 1
                BT_SS_value = 59
            else:
                # Sound alert is called.
                if self.sound_VO == "True":
                    self.play_sounds(2)
                # Minutos and second are set as there was at the beggining.
                self.breaktime_SS_VO.set(initial_value_SS)
                self.breaktime_MM_VO.set(initial_value_MM)
                # New threading is run to start BT_VO_countdown function.
                threading.Thread(target=self.NA_VO_countdown).start()
                break

    def TR_SO_countdown(self):
        """This method starts the main countdown "Time Remaining" of the stretch options."""

        TR_HH_value = int(self.time_left_HH_SO.get())
        TR_MM_value = int(self.time_left_MM_SO.get())

        while True:
            if self.app_running == False:
                self.stop_countdown_SO = True
                break
            else:
                if TR_MM_value > 9:
                    self.time_left_MM_SO.set(TR_MM_value)
                else:
                    self.time_left_MM_SO.set("0" + str(TR_MM_value))
                if TR_HH_value > 9:
                    self.time_left_HH_SO.set(TR_HH_value)
                else:
                    self.time_left_HH_SO.set("0" + str(TR_HH_value))

                self.init_timer(60, "TR_SO")
                if TR_MM_value > 0:
                    TR_MM_value -=1
                elif TR_HH_value > 0:
                    TR_HH_value -=1
                    TR_MM_value = 59
                if TR_HH_value == 0 and TR_MM_value == 0:
                    if self.sound_SO == "True":
                        self.play_sounds(1)
                    self.time_left_HH_SO.set("")
                    self.time_left_MM_SO.set("")
                    self.colon_SO_1.place_forget()
                    finished_label_SO = ctk.CTkLabel(self.frame_stretch, text="Finalizado", font=(font, 20), corner_radius=5,
                                                     fg_color=colors["soft_green"])
                    finished_label_SO.place(rely=0.55, relx=0.06, anchor="w")
                    self.next_alert_MM_SO.set("00")
                    self.next_alert_SS_SO.set("00")
                    self.breaktime_MM_SO.set("00")
                    self.breaktime_SS_SO.set("00")
                    self.stop_countdown_SO = True
                    break

    def NA_SO_countdown(self):
        """This method starts the countdown "Next Alert" of the stretch options."""

        initial_value_MM = self.next_alert_MM_SO.get()
        initial_value_SS = self.next_alert_SS_SO.get()

        NA_MM_value = int(initial_value_MM)
        NA_SS_value = int(initial_value_SS)

        while NA_MM_value > -1:
            # Conditional that stop bucle when return button is pressed or time remaining is finished.
            if self.app_running == False or self.stop_countdown_SO == True:
                break
            elif NA_SS_value > 9:
                self.next_alert_SS_SO.set(NA_SS_value)
            else:
                self.next_alert_SS_SO.set("0" + str(NA_SS_value))
            if NA_MM_value > 9:
                self.next_alert_MM_SO.set(NA_MM_value)
            else:
                self.next_alert_MM_SO.set("0" + str(NA_MM_value))

            if NA_SS_value > 0:
                self.init_timer(1, "SO_countdown")
                NA_SS_value -=1
            elif NA_MM_value > 0:
                self.init_timer(1, "SO_countdown")
                NA_MM_value -= 1
                NA_SS_value = 59
            else:
                if self.sound_SO == "True":
                    self.play_sounds(2)
                self.next_alert_SS_SO.set(initial_value_SS)
                self.next_alert_MM_SO.set(initial_value_MM)
                threading.Thread(target=self.BT_SO_countdown).start()
                break

    def BT_SO_countdown(self):
        """This method starts the countdown "Break Time" of the stretch options."""

        initial_value_MM = self.breaktime_MM_SO.get()
        initial_value_SS = self.breaktime_SS_SO.get()

        BT_MM_value = int(initial_value_MM)
        BT_SS_value = int(initial_value_SS)

        while BT_MM_value > -1:
            # Conditional that stop bucle when return button is pressed or time remaining is finished.
            if self.app_running == False or self.stop_countdown_SO == True:
                break

            if BT_SS_value > 9:
                self.breaktime_SS_SO.set(BT_SS_value)
            else:
                self.breaktime_SS_SO.set("0" + str(BT_SS_value))
            if BT_MM_value > 9:
                self.breaktime_MM_SO.set(BT_MM_value)
            else:
                self.breaktime_MM_SO.set("0" + str(BT_MM_value))

            if BT_SS_value > 0:
                self.init_timer(1, "SO_countdown")
                BT_SS_value -=1
            elif BT_MM_value > 0:
                self.init_timer(1, "SO_countdown")
                BT_MM_value -=1
                BT_SS_value = 59
            else:
                if self.sound_SO == "True":
                    self.play_sounds(2)
                self.breaktime_SS_SO.set(initial_value_SS)
                self.breaktime_MM_SO.set(initial_value_MM)
                threading.Thread(target=self.NA_SO_countdown).start()
                break

    def play_sounds(self, value):
        """This method runs sounds alerts."""
        
        if self.app_running == True:
            # When value is "1" the sound related to "Time Remaining" is set.
            if value == 1:
                try:
                    if self.final_sound == "":
                        pygame.mixer.music.load(os.path.join(sounds_path, "Final.mp3"))
                        pygame.mixer.music.play(loops=0)
                    else:
                        pygame.mixer.music.load(self.final_sound)
                        pygame.mixer.music.play(loops=0)
                except:
                    pygame.mixer.music.load(os.path.join(sounds_path, "Final.mp3"))
                    pygame.mixer.music.play(loops=0)

            # When value is "2" the sound related to "Lapse" is set.
            elif value == 2:
                try:
                    if self.lapse_sound == "":
                        pygame.mixer.music.load(os.path.join(sounds_path, "Lapse.mp3"))
                        pygame.mixer.music.play(loops=0)
                    else:
                        pygame.mixer.music.load(self.lapse_sound)
                        pygame.mixer.music.play(loops=0)
                except:
                    pygame.mixer.music.load(os.path.join(sounds_path, "Final.mp3"))
                    pygame.mixer.music.play(loops=0)

    def stop_app(self):
        """This method stops the app when return button is pressed."""
        
        # Variable to stop all bucles running.
        self.app_running = False
        # Method is called to stop the sound alert.
        pygame.mixer.quit()
        self.window_RS.destroy()
        self.root.deiconify()

    def stop_sound(self):
        """This method stops sounds."""
        
        pygame.mixer.quit()
        pygame.mixer.init()

    def init_timer(self, num_seconds, thread):
        """This method start timer and compare the time elapsed with "time.perf_counter"."""

        # This conditional compense the delay between when the class is "init" with the moment that the timer is run. Only happend once
        if self.init_TR_VO_multiplier == 0 and self.init_TR_SO_multiplier == 0 and self.init_VO_countdown_multiplier == 0 and self.init_SO_countdown_multiplier == 0:
            init_elapsed_seconds = time.perf_counter() - self.start_time
            time.sleep(num_seconds - 0.1 - init_elapsed_seconds)
        else:
            # Time sleep is run with minus 0.1 to be compensated after and avoid irregulars rounds, have precision and the timer sinchronized.
            time.sleep(num_seconds - 0.1)

        current_time = time.perf_counter()

        elapsed_seconds = current_time - self.start_time

        # These conditionals get the final value to compensate and avoid the desynchronization in large timers
        if thread == "TR_VO":
            remaining_to_compensate = num_seconds - (elapsed_seconds - (num_seconds * self.init_TR_VO_multiplier))
            self.init_TR_VO_multiplier += 1
        if thread == "TR_SO":
            remaining_to_compensate = num_seconds - (elapsed_seconds - (num_seconds * self.init_TR_SO_multiplier))
            self.init_TR_SO_multiplier += 1
        elif thread == "VO_countdown":
            remaining_to_compensate = num_seconds - (elapsed_seconds - (num_seconds * self.init_VO_countdown_multiplier))
            self.init_VO_countdown_multiplier += 1
        elif thread == "SO_countdown":
            remaining_to_compensate = num_seconds - (elapsed_seconds - (num_seconds * self.init_SO_countdown_multiplier))
            self.init_SO_countdown_multiplier += 1
        from datetime import datetime
        if remaining_to_compensate < 0:
            remaining_to_compensate = 0

        time.sleep(remaining_to_compensate)


class RelaxApp_MessageBox_Options(RelaxApp_MessageBox_Structure):
    """Defines all pop-ups of the App. Inherit all structure from parent."""

    def __init__(self, root, frame, message_type, **kwargs):

        super().__init__()

        self.root = root
        self.frame = frame
        self.message_type = message_type
        self.message = kwargs.get("message")
        self.data = kwargs.get("data")
        self.action = kwargs.get("action")

        # Variable to set when the button "Accept", "Cancel" is activated
        self.select_button1 = False
        # Variable to set when the button "Return" is activated
        self.select_button2 = False

        # It creates the label, the message and set the variable to create two buttons (accept and cancel).
        if self.action == "Accept":
            self.accept_label = ctk.CTkLabel(self.window_MS, text=self.message, font=(font,15), wraplength=500, bg_color=colors["soft_grey"])
            self.accept_label.place(rely=0.3, relx=0.5, anchor="center")
            self.select_button1 = True
        
        # It creates the label, the message and set the variable to create one button (return).
        if self.action == "Return":

            self.return_label = ctk.CTkLabel(self.window_MS, text=self.message, font=(font,15), wraplength=500, bg_color=colors["soft_grey"])
            self.return_label.place(rely=0.3, relx=0.5, anchor="center")
            self.select_button2 = True   

        # It creates two buttons (accept and cancel).
        if self.select_button1 == True:
            # Button to accept a change.
            self.accept_ask_cancel_button = ctk.CTkButton(self.window_MS, width=80, height=17, text="Aceptar", font=(font,14),
                                                          command=lambda: self.accept_button(self.message_type), corner_radius=10,
                                                          hover=True, fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                                          bg_color=colors["soft_grey"])
            self.accept_ask_cancel_button.place(rely=0.65, relx=0.25, anchor="w")

            # Button to cancel a change.
            self.cancel_ask_cancel_button = ctk.CTkButton(self.window_MS, width=80, height=17, text="Cancelar", font=(font,14),
                                                          command=self.cancel_button, corner_radius=10, hover=True,
                                                          fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                                          bg_color=colors["soft_grey"])
            self.cancel_ask_cancel_button.place(rely=0.65, relx=0.75, anchor="e")

        # It creates one button (return).
        if self.select_button2 == True:
            # Button to continue after a change.
            self.continue_registration_button = ctk.CTkButton(self.window_MS, width=80, height=17, text="Volver", font=(font,14),
                                                              command=self.return_button, corner_radius=10, hover=True,
                                                              fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                                              bg_color=colors["soft_grey"])
            self.continue_registration_button.place(rely=0.65, relx=0.5, anchor="center")

    def accept_button(self, message_type):
        """This method confirm a change."""
        
        valid_values = False
        
        # This conditional accept the registration. 
        if message_type == "Sign up":
            # Request to create an user is confirmed.
            response_dict = comms.register(self.data)
            
        # This conditional accept the change of password.
        elif message_type == "Confirm Change PW":
            # Request to reset a password is confirmed.
            response_dict = comms.reset_password_confirmation(self.data)
        
        elif message_type == "Sign Out":
            Session.clear()
            TemporaryProfile.clear()
            self.window_MS.destroy()
            RelaxApp_Structure.close_create2(self, RelaxApp_Initial_Frame, self.root, self.frame)
            return
        
        elif message_type == "Remove Account":
            # Request to remove the account is confirmed.
            response_dict = comms.remove_account(Session.username)
             
        # User registration or change of password are canceled and turn back to main menu as weel as sign out.
        elif message_type == "Cancel" or message_type == "Cancel Change PW" or message_type == "Cancel Confirm Change PW":
            self.window_MS.destroy()
            RelaxApp_Structure.close_create2(self, RelaxApp_Initial_Frame, self.root, self.frame)
            return

        response, message = Requests_Status.check_server_connection(response_dict)
        
        if response != None:
            if message_type == "Sign up":
                status_expected = 201
            else:
                status_expected = 200
                
            valid_request, values, message = Requests_Status.check_request_status(response, status_expected, "accept_button_MB")

            if valid_request:
                request_type = values["request_type"]
                
                if request_type == "user_registration" or request_type == "user_pw_reset_confirmation":
                    valid_values = True
                    
                elif request_type == "remove_account":
                    Session.clear()
                    TemporaryProfile.clear()
                    self.window_MS.destroy()
                    RelaxApp_Structure.close_create2(self, RelaxApp_Initial_Frame, self.root, self.frame)
                    return
           
        # The request is checked. 
        if valid_values:
            # A pop-up window is displayed to confirm that the request has been succesful.
            # First the pop-up window is cleaned.
            RelaxApp_MessageBox_Structure.clean_MB_widgets(self, self.window_MS)
            # Second a new label is created with a new message.
            self.new_message_box("Continue", message)
        else:
            
            RelaxApp_MessageBox_Structure.clean_MB_widgets(self, self.window_MS)
            self.new_message_box("Error", message) 

    def cancel_button(self):
        """This method accepts cancelation or cancels cancelation."""
        
        self.window_MS.destroy()

    def continue_button(self, message_type):
        """This method is run after a message box is asking to "continue" or not."""
        
        if message_type == "Continue":
            self.window_MS.destroy()
            RelaxApp_Structure.close_create(self, RelaxApp_Initial_Frame, self.root, self.frame)
        elif message_type == "Continue2":
            self.window_MS.destroy()

    def return_button(self):
        """This method turns back to the last menu opened."""
        
        self.window_MS.destroy()

    def new_message_box(self, message_type, message):
        """This method runs a new message box after a message box when is needed a second confirmation."""

        if message_type == "Error":
            # Label confirm user registration.
            self.continue_registration = ctk.CTkLabel(self.window_MS, text=message, font=(font,15),
                                                      wraplength=500, bg_color=colors["soft_grey"])
            self.continue_registration.place(rely=0.3, relx=0.5, anchor="center")

            # Button to continue to the main menu.
            self.continue_registration_button = ctk.CTkButton(self.window_MS, width=80, height=17, text="Volver", font=(font,14),
                                                              command=self.return_button, corner_radius=10, hover=True,
                                                              fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                                              bg_color=colors["soft_grey"])
            self.continue_registration_button.place(rely=0.65, relx=0.5, anchor="center")

            return

        elif message_type == "Continue":
            
            # Label confirm user registration.
            self.continue_registration = ctk.CTkLabel(self.window_MS, text=message, font=(font,15),
                                                      wraplength=500, bg_color=colors["soft_grey"])
            self.continue_registration.place(rely=0.30, relx=0.5, anchor="center")

        # Button to continue to the main menu.
        self.continue_registration_button = ctk.CTkButton(self.window_MS, width=80, height=17, text="Continuar", font=(font,14),
                                                            command=lambda: self.continue_button(message_type), corner_radius=10, hover=True,
                                                            fg_color=colors["soft_green"], hover_color=colors["dark_green"],
                                                            bg_color=colors["soft_grey"])
        self.continue_registration_button.place(rely=0.65, relx=0.5, anchor="center")

