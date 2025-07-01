import cv2
from error import ErrorHandler

def get_camera(camera_id=0):
    """
    Initialize and return a camera device.
    
    Args:
        camera_id (int): ID of the camera to use (default: 0)
    
    Returns:
        cv2.VideoCapture: Camera object or None if failed
    """
    cap = cv2.VideoCapture(camera_id)
    
    if not cap.isOpened():
        ErrorHandler.handle_error(f"Failed to open camera with ID {camera_id}", notify_user=True)
        return None
        
    # Set camera properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Check if camera settings were applied
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    ErrorHandler.log_info(f"Camera initialized: {actual_width}x{actual_height}")
    return cap