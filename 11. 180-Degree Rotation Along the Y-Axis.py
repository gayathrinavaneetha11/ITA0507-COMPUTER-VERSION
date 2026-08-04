import cv2

# Read the input image
image = cv2.imread("img.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found")
else:
    # Flip the image along the Y-axis
    flipped_image = cv2.flip(image, 1)

    # Rotate the flipped image by 180 degrees
    rotated_image = cv2.rotate(
        flipped_image,
        cv2.ROTATE_180
    )

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow(
        "180 Degree Rotation Along Y-axis",
        rotated_image
    )

    # Save the output image
    cv2.imwrite("rotated_image.jpg", rotated_image)

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
