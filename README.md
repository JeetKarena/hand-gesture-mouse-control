# Gesture Mouse Control

Control your computer mouse using hand gestures captured through your webcam.

## Features

- Control mouse cursor movements using your hand position
- Execute various actions with different finger gestures:
  - One finger: Mouse click
  - Two fingers: Scroll down
  - Three fingers: Alt+Tab (switch windows)
- Configurable gesture mappings
- Visual feedback with displayed gestures and FPS counter
- Error handling and notifications

## Requirements

- Python 3.12 or lower (Python 3.12 recommended)
- Webcam
- Windows operating system (for notifications)
- Dependencies listed in requirements.txt

## Installation

1. Clone this repository
2. Install required packages:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

```
python main.py
```

2. Position your hand in front of the camera
3. Use the following gestures:
   - Show one finger (index) for mouse click
   - Show two fingers for scrolling
   - Show three fingers for Alt+Tab
4. Press ESC to exit

## Configuration

You can customize gesture actions by editing the `config.yml` file:

```yaml
gesture_mappings:
  ONE_FINGER: "click"
  TWO_FINGERS: "scroll_down"
  THREE_FINGERS: "alt_tab"
```

Available actions include:
- click
- right_click
- double_click
- scroll_up
- scroll_down
- alt_tab
- copy (Ctrl+C)
- paste (Ctrl+V)
- undo (Ctrl+Z)

## Troubleshooting

- If the camera doesn't initialize, check if it's connected and not in use by another application
- If hand detection is poor, try improving lighting conditions
- For compatibility issues, ensure you're using Python 3.12 or lower
- Logs are stored in gesture_mouse.log in the application directory

## License

[Include license information]

## Acknowledgements

This project uses:
- MediaPipe for hand tracking
- OpenCV for video capture and processing
- PyAutoGUI for mouse and keyboard control
