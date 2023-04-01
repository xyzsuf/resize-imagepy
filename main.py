import cv2

source = "swift.jpg"
destination = "taylor.jpg"
scale_perc = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_width = int(src.shape[1] * scale_perc / 100)
new_height = int(src.shape[0] * scale_perc / 100)

output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(1)
