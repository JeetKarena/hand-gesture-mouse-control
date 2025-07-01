import pyautogui
import yaml
import os
import time
from error import ErrorHandler

# Define safe actions that can be executed
ACTIONS = {
    "click": lambda: pyautogui.click(),
    "right_click": lambda: pyautogui.rightClick(),
    "double_click": lambda: pyautogui.doubleClick(),
    "scroll_up": lambda: pyautogui.scroll(50),
    "scroll_down": lambda: pyautogui.scroll(-50),
    "alt_tab": lambda: pyautogui.hotkey("alt", "tab"),
    "copy": lambda: pyautogui.hotkey("ctrl", "c"),
    "paste": lambda: pyautogui.hotkey("ctrl", "v"),
    "undo": lambda: pyautogui.hotkey("ctrl", "z"),
}

# Default mappings in case config fails to load
DEFAULT_MAPPINGS = {
    "ONE_FINGER": "click",
    "TWO_FINGERS": "scroll_down",
    "THREE_FINGERS": "alt_tab",
}

def load_config():
    """Load gesture mappings from config file"""
    gesture_actions = {}
    config_path = os.path.join(os.path.dirname(__file__), "config.yml")
    
    try:
        if os.path.exists(config_path):
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
                if config and "gesture_mappings" in config:
                    gesture_actions = config.get("gesture_mappings", {})
                    ErrorHandler.log_info(f"Loaded gesture mappings: {gesture_actions}")
                else:
                    ErrorHandler.handle_error("Invalid config format - missing gesture_mappings section", notify_user=True)
                    gesture_actions = DEFAULT_MAPPINGS
        else:
            ErrorHandler.handle_error(f"Config file not found at {config_path}", notify_user=True)
            gesture_actions = DEFAULT_MAPPINGS
    except Exception as e:
        ErrorHandler.handle_error(f"Failed to load config file: {str(e)}", e, notify_user=True)
        gesture_actions = DEFAULT_MAPPINGS
        
    return gesture_actions

# Load gesture mappings
gesture_actions = load_config()

# Keep track of last action time to prevent rapid firing
last_action_time = 0
ACTION_COOLDOWN = 0.5  # seconds between actions

def perform_action(gesture):
    """
    Perform the action associated with a gesture
    
    Args:
        gesture: The detected gesture name
    """
    global last_action_time
    
    # Prevent actions from firing too rapidly
    current_time = time.time()
    if current_time - last_action_time < ACTION_COOLDOWN:
        return
    
    action_name = gesture_actions.get(gesture)
    if not action_name:
        return
        
    if action_name in ACTIONS:
        try:
            ErrorHandler.log_info(f"Executing action: {action_name} for gesture {gesture}")
            ACTIONS[action_name]()
            last_action_time = current_time
        except Exception as e:
            ErrorHandler.handle_error(f"Error executing action for {gesture}", e, notify_user=True)
    else:
        ErrorHandler.handle_error(f"Unknown or unsafe action: {action_name}", notify_user=False)