import cv2

def nothing(x):
    pass

path_relative = 'flor.jpg'

cv2.namedWindow('trackbar')
cv2.createTrackbar('b_min','trackbar',0,255,nothing)
cv2.createTrackbar('b_max','trackbar',0,255,nothing)
# cv2.createTrackbar('r_min','trackbar',0,255,nothing)
# cv2.createTrackbar('r_max','trackbar',0,255,nothing)
# cv2.createTrackbar('g_min','trackbar',0,255,nothing)
# cv2.createTrackbar('g_max','trackbar',0,255,nothing)


while True:
    image_color = cv2.imread(path_relative,1)
    b_min = cv2.getTrackbarPos('b_min','trackbar')
    b_max = cv2.getTrackbarPos('b_max','trackbar')
    # r_min = cv2.getTrackbarPos('r_min','trackbar')
    # r_max = cv2.getTrackbarPos('r_max','trackbar')
    # g_min = cv2.getTrackbarPos('g_min','trackbar')
    # g_max = cv2.getTrackbarPos('g_max','trackbar')
    # image_binary_range = cv2.inRange(image_color,(b_min,g_min,r_min),(b_max,g_max,r_max))
    
    image_binary_range = cv2.inRange(image_color,(b_min),(b_max))
    cv2.imshow('trackbar',image_binary_range)
    # cv2.imshow('trackbar',cv2.resize(image_binary_range,980,720))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
