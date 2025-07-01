import cv2
import time
import signal
import sys
import os
from camera import get_camera
from hand_tracker import HandTracker
from gesture_classifier import classify_gesture
from action_mapper import perform_action
from error import ErrorHandler

def check_python_version():
    """Check if running on a compatible Python version"""
    major, minor = sys.version_info.major, sys.version_info.minor
    if major != 3 or minor > 12:
        ErrorHandler.handle_error(
            f"Unsupported Python version: {major}.{minor}. "
            f"This application is tested on Python 3.12 or lower.",
            notify_user=True
        )
        return False
    return True

def main():
    # Check Python version first
    if not check_python_version():
        return

    # Initialize error handling
    ErrorHandler.log_info(f"Starting Gesture Mouse Control (Python {sys.version})")

    # Initialize camera
    cap = get_camera()
    if cap is None:
        ErrorHandler.handle_error("Could not initialize camera. Exiting.", notify_user=True)
        return

    # Initialize hand tracker
    tracker = HandTracker()

    # Set up FPS limiting
    prev_time = time.time()
    fps_limit = 30  # Target FPS

    def signal_handler(sig, frame):
        ErrorHandler.log_info('Exiting gracefully...')
        cleanup(cap, tracker)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    # Display information to user
    ErrorHandler.log_info("Gesture Mouse Control is running")
    ErrorHandler.log_info("Press ESC to exit")

    try:
        while True:
            try:
                ret, frame = cap.read()
                if not ret:
                    if ErrorHandler.handle_error("Failed to capture frame", notify_user=True):
                        break

                current_time = time.time()
                elapsed = current_time - prev_time
                if elapsed >= 1.0 / fps_limit:
                    # Process frame only at desired FPS
                    landmarks = tracker.detect(frame)
                    gesture = classify_gesture(landmarks)
                    if gesture:
                        perform_action(gesture)
                        # Show recognized gesture on frame
                        if gesture:
                            cv2.putText(frame, f"Gesture: {gesture}", (10, 30), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    prev_time = current_time

                # Display FPS on frame
                fps = 1 / elapsed if elapsed > 0 else 0
                cv2.putText(frame, f"FPS: {fps:.1f}", (10, 70), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                cv2.imshow("Gesture Mouse Control", frame)
                if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
                    break
                    
            except Exception as e:
                if ErrorHandler.handle_error("Error in main loop", e, notify_user=True):
                    break
    finally:
        # Make sure we release resources properly
        cleanup(cap, tracker)

def cleanup(cap, tracker):
    """Clean up resources properly"""
    ErrorHandler.log_info("Cleaning up resources...")
    if cap:
        cap.release()
    if tracker:
        tracker.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
cv2.destroyAllWindows()
logger = ErrorHandler.log_info("Stopped Gesture Mouse Control")