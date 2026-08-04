import cv2
import numpy as np

# Read the input image
image = cv2.imread("img.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found")
else:
    # Create a copy of the original image
    result_image = image.copy()

    # Convert the image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    harris_corners = cv2.cornerHarris(
        gray,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    # Dilate the corners
    harris_corners = cv2.dilate(
        harris_corners,
        None
    )

    # Mark detected corners in red
    result_image[
        harris_corners >
        0.01 * harris_corners.max()
    ] = [0, 0, 255]

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow(
        "Harris Corner Detection",
        result_image
    )

    # Save the output image
    cv2.imwrite(
        "harris_corners.jpg",
        result_image
    )

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
