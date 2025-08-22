import cv2
import mediapipe as mp
import utils
import pyautogui

# Set the screen resolution
screen_width, screen_height = pyautogui.size()

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.4,
    model_complexity=1,
)

# Add state variables to track click status
click_performed = False
double_click_performed = False

def find_landmark(processed, landmark_type):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        return hand_landmarks.landmark[landmark_type]
    return None

def move_mouse(index_finger_tip):
    if index_finger_tip:
        x = int(index_finger_tip.x * screen_width * 1.2)
        y = int(index_finger_tip.y * screen_height * 1.2)
        pyautogui.moveTo(x, y)

def click_mouse():
    pyautogui.leftClick()

def double_click_mouse():
    pyautogui.doubleClick()

# Modify the detect_gestures function to use these state variables
def detect_gestures(landmarks_list, processed):
    global click_performed, double_click_performed

    if len(landmarks_list) >= 21:
        thumb_tip = find_landmark(processed, mpHands.HandLandmark.THUMB_TIP)
        index_finger_tip = find_landmark(processed, mpHands.HandLandmark.INDEX_FINGER_TIP)
        thumb_index_distance = utils.get_distance([landmarks_list[4], landmarks_list[5]])

        angle_index = utils.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
        angle_middle = utils.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12])

        if thumb_index_distance < 80 and angle_index < 90:
            move_mouse(thumb_tip)
            click_performed = False
            double_click_performed = False
        elif thumb_index_distance > 80 and angle_index > 90:
            if angle_middle < 90 and not click_performed:
                print('mouse clicking')
                click_mouse()
                click_performed = True
                double_click_performed = False
            elif angle_middle > 90 and not double_click_performed:
                print('mouse double clicking')
                double_click_mouse()
                double_click_performed = True
                click_performed = False

def main():
    cap = cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils

    try:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Store the processed frame
            processed = hands.process(frame_rgb)

            # Store the landmarks from hands
            landmarks_list = []

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

                landmarks_list = [(lm.x, lm.y) for lm in hand_landmarks.landmark]

            detect_gestures(landmarks_list, processed)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()