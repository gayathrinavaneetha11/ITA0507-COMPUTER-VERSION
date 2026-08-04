import cv2
import numpy as np

# Read the input image
image = cv2.imread("img.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found")
else:
    # Get image dimensions
    rows, cols, ch = image.shape

    # Define source points
    pts1 = np.float32([
        [50, 50],
        [400, 50],
        [50, 400],
        [400, 400]
    ])

    # Define destination points
    pts2 = np.float32([
        [10, 100],
        [300, 50],
        [100, 300],
        [350, 350]
    ])

    # Calculate the perspective matrix
    matrix = cv2.getPerspectiveTransform(
        pts1,
        pts2
    )

    # Apply perspective transformation
    transformed_image = cv2.warpPerspective(
        image,
        matrix,
        (cols, rows)
    )

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow(
        "Perspective Transformed Image",
        transformed_image
    )

    # Save the output image
    cv2.imwrite(
        "perspective_transformed.jpg",
        transformed_image
    )

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
