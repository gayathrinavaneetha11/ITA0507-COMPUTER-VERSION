import cv2

# Read the image
image = cv2.imread("img.jpg")    # Change extension if needed (.png, .jpeg)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Enlarge image (2x)
bigger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Shrink image (0.5x)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
