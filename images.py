import cv2

# Load an image from the Images folder
image = cv2.imread('Images/ss1.png')

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait for any key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
