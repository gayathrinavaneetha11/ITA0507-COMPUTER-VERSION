import cv2

image = cv2.imread(r"C:\Users\91934\Downloads\image.jpg")

if image is None:
    print("Image not found!")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
