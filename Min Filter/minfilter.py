import cv2

def minimumBoxFilter(n, img):
    img = cv2.imread("fiony.jpg")

    # Creates the shape of the kernel
    size = (n, n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)

# Applies the minimum filter with kernel NxN
    imgResult = cv2.erode(img, kernel)

# Shows the result
    cv2.namedWindow('Result with n ' + str(n), cv2.WINDOW_NORMAL) # Adjust the window length
    cv2.imshow('Result with n ' + str(n), imgResult)

# Creates the shape of the kernel
    size = (n,n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)

# Applies the maximum filter with kernel NxN
    imgResult = cv2.dilate(img, kernel)

# Shows the result
    cv2.namedWindow('Result with n ' + str(n), cv2.WINDOW_NORMAL) # Adjust the window length
    cv2.imshow('Result with n ' + str(n), imgResult)


if __name__ == "__main__":
    img = cv2.imread("Fiony.png")

    print("Test the function minimumBoxFilter()")
    minimumBoxFilter(3, img)
    minimumBoxFilter(5, img)
    minimumBoxFilter(7, img)
    minimumBoxFilter(11, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()