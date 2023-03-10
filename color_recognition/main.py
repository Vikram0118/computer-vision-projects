import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True :
    _, frame = capture.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Only Red", red)
    cv2.imshow("Only Green", green)
    cv2.imshow("Only Blue", blue)
    cv2.imshow("All color except White", result)

    key = cv2.waitKey(1)

    if key == 27 :
        break


# import cv2
# import numpy as np

# frame = cv2.imread('./color1.jpeg')

# hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# red_lower1 = np.array([0, 100, 20])
# red_upper1 = np.array([10, 255, 255])
# red_lower2 = np.array([160,100,20])
# red_upper2 = np.array([179,255,255])
# red_lower_mask = cv2.inRange(hsv_frame, red_lower1, red_upper1)
# red_upper_mask = cv2.inRange(hsv_frame, red_lower2, red_upper2)
# red_full_mask = red_lower_mask + red_upper_mask
# red = cv2.bitwise_and(frame, frame, mask=red_full_mask)
 
# low_blue = np.array([94, 80, 2])
# high_blue = np.array([126, 255, 255])
# blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
# blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

# low_green = np.array([25, 52, 72])
# high_green = np.array([102, 255, 255])
# green_mask = cv2.inRange(hsv_frame, low_green, high_green)
# green = cv2.bitwise_and(frame, frame, mask=green_mask)

# low = np.array([0, 42, 0])
# high = np.array([179, 255, 255])
# mask = cv2.inRange(hsv_frame, low, high)
# result = cv2.bitwise_and(frame, frame, mask=mask)

# cv2.imshow("Frame", frame)
# cv2.imshow("Only Red", red)
# cv2.imshow("Only Green", green)
# cv2.imshow("Only Blue", blue)
# cv2.imshow("All color except White", result)

# key = cv2.waitKey(0)

# if key == 27 :
#     cv2.destroyAllWindows()