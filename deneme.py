import cv2
import numpy as np

# set intensity threshold
thresh1 = 160
thresh2 = 180
thresh3 = 200

thresh4 = 220


# define rescale function
def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    boyut = (width, height)
    return cv2.resize(frame, boyut, interpolation=cv2.INTER_AREA)

# read image and rescale
img = cv2.imread('xy.jpg')
img = rescale(img)

# convert img to grayscale intensity
intensity = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get img where intensity is larger than thresh
data = img[(intensity>thresh1)&(thresh2>intensity)]

# get coordinates where intensity is larger than thresh
coords = np.argwhere(intensity>thresh1)

# print coordinates x,y vs bgr color
for (y,x),(b,g,r)in zip(coords,data):
    print(x, y, ": ", b, g, r)

# draw red pixels on intensity image where larger than thresh
result = intensity.copy()
result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
result[(intensity>thresh1)&(thresh2>intensity)] = (0,0,255)
result[(intensity>thresh2)&(thresh3>intensity)] = (0,255,0)
result[(intensity>thresh3)&(thresh4>intensity)] = (255,0,0)

# save result
cv2.imwrite('green_region_190.jpg', result)

# show thresh and result    
cv2.imshow("Original Picture", intensity)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
