from error import ErrorHandler

# MediaPipe hand landmark indices
WRIST = 0
THUMB_TIP = 4
INDEX_TIP = 8
INDEX_MCP = 5
INDEX_PIP = 6
MIDDLE_TIP = 12
MIDDLE_PIP = 10
RING_TIP = 16
RING_PIP = 14
PINKY_TIP = 20
PINKY_PIP = 18

def classify_gesture(landmarks):
    """
    Classify hand gestures based on finger positions.
    
    Args:
        landmarks: List of (x,y) coordinates for hand landmarks
        
    Returns:
        str: Gesture name or None if no gesture is detected
    """
    if not landmarks or len(landmarks) < 21:
        return None
    
    try:
        # Check if each finger is extended
        fingers_up = 0
        
        # Index finger
        if landmarks[INDEX_TIP][1] < landmarks[INDEX_PIP][1]:
            fingers_up += 1
            
        # Middle finger
        if landmarks[MIDDLE_TIP][1] < landmarks[MIDDLE_PIP][1]:
            fingers_up += 1
            
        # Ring finger
        if landmarks[RING_TIP][1] < landmarks[RING_PIP][1]:
            fingers_up += 1
            
        # Pinky finger
        if landmarks[PINKY_TIP][1] < landmarks[PINKY_PIP][1]:
            fingers_up += 1

        if fingers_up == 1:
            return "ONE_FINGER"
        elif fingers_up == 2:
            return "TWO_FINGERS"
        elif fingers_up == 3:
            return "THREE_FINGERS"
        else:
            return None
            
    except IndexError as e:
        ErrorHandler.handle_error("Invalid landmark data", e)
        return None