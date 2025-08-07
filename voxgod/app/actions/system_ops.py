import platform
import os

def get_system_info():
    return platform.uname()

def list_files(directory="."):
    return os.listdir(directory)
