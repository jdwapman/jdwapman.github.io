import cv2
import sys

# Input error catching
num_args = len(sys.argv)

if num_args != 4:
    print("Usage: python3 ./resize_image <filename> <height (px)> <width (px)>")
    exit()

img_path = sys.argv[1]
height = sys.argv[2]
width = sys.argv[3]

img = cv2.imread(img_path)

img_size = img.shape
print(img_size)
