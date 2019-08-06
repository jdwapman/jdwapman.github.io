import cv2
import sys
import os

def append_file_text(filename, text):
    name, ext = os.path.splitext(filename)
    return "{name}_{uid}{ext}".format(name=name, uid=text, ext=ext)

# Input error catching
num_args = len(sys.argv)

if num_args != 3:
    print("Usage: python3 ./resize_image <filename> <width (px)>")
    exit()

img_path = sys.argv[1]
width = int(sys.argv[2])

img = cv2.imread(img_path)

img_size = img.shape

act_height = int(img_size[0])
act_width = int(img_size[1])

width_ratio = width / act_width
#height_ratio = height / act_height

#ratio = min(width_ratio, height_ratio)

ratio = width_ratio

resized_width = int(act_width * ratio)
resized_height = int(act_height * ratio)

new_size = (resized_width, resized_height)

resized_img = cv2.resize(img, new_size)


save_path = append_file_text(img_path, "resized")
print(save_path)
cv2.imwrite(save_path, resized_img)
