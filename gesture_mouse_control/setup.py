import sys
import os
import subprocess
from error import ErrorHandler

def check_python_version():
    """Check if running on a compatible Python version"""
    major, minor = sys.version_info.major, sys.version_info.minor
    if major != 3 or minor > 12:
        print(f"Warning: Unsupported Python version: {major}.{minor}")
        print("This application is tested on Python 3.12 or lower")
        print("Some features may not work correctly")
        return False
    return True

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        "opencv-python", 
        "mediapipe", 
        "pyautogui", 
        "pyyaml", 
        "win10toast", 
        "numpy"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_').split('>=')[0].split('==')[0])
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install -r requirements.txt")
        return False
        
    return True

def setup():
    """Perform initial setup and checks"""
    if not check_python_version():
        return False
        
    if not check_dependencies():
        return False
    
    return True

if __name__ == "__main__":
    if setup():
        print("All system checks passed!")
        print("You can run 'python main.py' to start the application")
    else:
        print("System checks failed. Please fix the issues above before running the application.")
