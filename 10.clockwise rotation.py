import cv2

# Read the image
image = cv2.imread("img.jpg")    # Change extension if needed (.png, .jpeg)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Rotate image 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
