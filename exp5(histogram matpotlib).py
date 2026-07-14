import cv2
import matplotlib.pyplot as plt

path = r"C:\Users\91934\OneDrive\Desktop\cv\img.jpg"

image = cv2.imread(path)

if image is None:
    print("Image not found!")
    exit()

colors = ('b', 'g', 'r')

plt.figure(figsize=(8,5))

for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])

plt.show()
