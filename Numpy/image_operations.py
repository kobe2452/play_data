from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt
import numpy as np

img = imread('/Users/tl8313/Pictures/basketball.jpg')
print img.dtype, img.shape

img_tinted = img * [1, 0.95, 0.9]

# img_tinted = imresize(img_tinted, (400, 1200))

imsave('/Users/tl8313/Pictures/basketball_tinted.jpg', img_tinted)

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))

plt.show()