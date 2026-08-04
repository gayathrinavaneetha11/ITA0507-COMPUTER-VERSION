import cv2
import numpy as np

# Read the input image
image = cv2.imread("img.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Create a 5 x 5 kernel
    kernel = np.ones(
        (5, 5),
        np.uint8
    )

    # Apply the Opening operation
    opened_image = cv2.morphologyEx(
        gray_image,
        cv2.MORPH_OPEN,
        kernel
    )

    # Display the images
    cv2.imshow(
        "Original Image",
        image
    )

    cv2.imshow(
        "Opened Image",
        opened_image
    )

    # Save the output image
    cv2.imwrite(
        "opened_image.jpg",
        opened_image
    )

    # Wait and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
