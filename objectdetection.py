import cv2 
import matplotlib.pyplot as plt
import numpy as np  
import sys


def imshow(img, figsize=(6, 6)):
    fig, ax = plt.subplots(1, 1, figsize=(figsize))
    ax.axis('off')
    ax.imshow(img)
    
img = cv2.imread(sys.argv[1])
#Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread(sys.argv[2], 0)
w, h = template.shape[1], template.shape[0]
imshow(img)

res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
imshow(res)

if sys.argv[3]:
    THRESHOLD = float(sys.argv[3])
else:
    THRESHOLD = 0.75
    
print(THRESHOLD)

loc = np.where(res >= THRESHOLD)

#Draw boudning box
for y, x in zip(loc[0], loc[1]):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 1)
imshow(img)

# Filename 
filename = 'savedImage.jpg'
  
# Using cv2.imwrite() method 
# Saving the image 
cv2.imwrite(filename, img)


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))