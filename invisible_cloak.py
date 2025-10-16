import cv2
import numpy as np

print("""
Harry :  Hey !! Would you like to try my invisibility cloak ??
         It's awesome !!

         Prepare to get invisible .....................
""")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

# Try background image first, then video
try:
    bg_video = cv2.VideoCapture('video.mp4')
    if not bg_video.isOpened():
        # Use static background image if video not available
        background = cv2.imread('image.jpg')
        use_video = False
    else:
        use_video = True
except:
    background = cv2.imread('image.jpg')
    use_video = False

ret, test_frame = cap.read()
if not ret:
    print("❌ Error: Could not read frame from webcam")
    cap.release()
    exit()

frame_height, frame_width = test_frame.shape[:2]

if not use_video:
    background = cv2.resize(background, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if use_video:
        ret_bg, back = bg_video.read()
        if not ret_bg:
            bg_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret_bg, back = bg_video.read()
        back = cv2.resize(back, (frame_width, frame_height))
    else:
        back = background

    if not ret:
        print("❌ Error: Could not read frame from webcam")
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color ranges
    lower_red1 = np.array([0, 80, 20])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([160, 80, 20])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Improve mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Apply invisibility effect
    part1 = cv2.bitwise_and(back, back, mask=mask)
    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.add(part1, part2)

    cv2.imshow("🧙‍♂️ Invisibility Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if use_video:
    bg_video.release()
cv2.destroyAllWindows()