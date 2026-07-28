import cv2

# Load the video
cap = cv2.VideoCapture("myvideo.mp4")

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file!")
    exit()

# Default mode = Normal
mode = "normal"

while True:
    ret, frame = cap.read()

    if not ret:
        # Restart video when it ends
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display the video
    cv2.imshow("Video Processing", frame)

    # Set playback speed
    if mode == "slow":
        delay = 100      # Slow motion
    elif mode == "fast":
        delay = 10       # Fast motion
        # Skip one frame to make it faster
        cap.read()
    else:
        delay = 30       # Normal speed

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        mode = "normal"
    elif key == ord('s'):
        mode = "slow"
    elif key == ord('f'):
        mode = "fast"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
