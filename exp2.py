import cv2

path = r"C:\Users\91934\OneDrive\Desktop\cv\img.jpg"

image = cv2.imread(path)

if image is None:
    print("Image not found!")
    exit()

blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
