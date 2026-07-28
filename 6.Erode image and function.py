import cv2

# Read the image
image = cv2.imread(r"C:\Users\91934\OneDrive\Desktop\cv\img.jpg")

# Check whether the image was loaded successfully
if image is None:
    print("Error: Image not found. Check the image path and file name.")
    exit()

# Create a kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
