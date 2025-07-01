import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False, 
            max_num_hands=1, 
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        landmarks = []
        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            # Draw hand landmarks on the frame for visual feedback
            self.mp_draw.draw_landmarks(
                frame, hand, self.mp_hands.HAND_CONNECTIONS)
            for lm in hand.landmark:
                landmarks.append((lm.x, lm.y))
        return landmarks
        
    def release(self):
        """Release resources used by the hand tracker"""
        if hasattr(self, 'hands'):
            self.hands.close()