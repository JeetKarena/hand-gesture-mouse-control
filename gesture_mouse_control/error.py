import logging
from win10toast import ToastNotifier
import os

# Configure logging
log_file = os.path.join(os.path.dirname(__file__), "gesture_mouse.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialize ToastNotifier for Windows notifications
toaster = ToastNotifier()

class ErrorHandler:
    @staticmethod
    def handle_error(message, error=None, notify_user=True):
        """Handle errors, log them, and optionally notify the user."""
        full_message = f"{message}" + (f": {str(error)}" if error else "")
        logger.error(full_message)
        if notify_user:
            try:
                toaster.show_toast(
                    "Gesture Mouse Control Error",
                    full_message,
                    duration=10,  # Notification visible for 10 seconds
                    threaded=True
                )
            except Exception as e:
                logger.warning(f"Failed to show notification: {e}")
        return False  # Indicate error occurred

    @staticmethod
    def log_info(message):
        """Log informational messages."""
        logger.info(message)

# Example usage (to be called from other modules)
if __name__ == "__main__":
    ErrorHandler.handle_error("Test error", ValueError("Test exception"))
    ErrorHandler.log_info("Test info message")