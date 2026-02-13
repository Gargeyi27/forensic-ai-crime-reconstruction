import cv2
import matplotlib.pyplot as plt


def identify_blood_patterns(scene_file):
    image = cv2.imread(scene_file)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    red_mask1 = cv2.inRange(hsv_image, (0,50,50), (10,255,255))
    red_mask2 = cv2.inRange(hsv_image, (170,50,50), (180,255,255))
    combined_mask = cv2.bitwise_or(red_mask1, red_mask2)

    output = cv2.bitwise_and(image, image, mask=combined_mask)

    plt.figure(figsize=(12,6))

    plt.subplot(1,2,1)
    plt.title("Original Scene")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(1,2,2)
    plt.title("Detected Blood Patterns")
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

    plt.show()
