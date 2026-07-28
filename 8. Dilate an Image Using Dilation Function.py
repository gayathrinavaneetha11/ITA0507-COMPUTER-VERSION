import cv2
import os

# Get the folder where this Python file is saved
folder = os.path.dirname(os.path.abspath(__file__))

# Image path
image_path = os.path.join(folder, "img.jpg")

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Create a kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply dilation
dilated_image = cv2.dilate(
    image,
    kernel,
    iterations=1
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
