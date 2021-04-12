import cv2

src = cv2.imread("C:/image/face-test-image1.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)

cv2.imshow("src", src)
cv2.imshow("sobel", sobel)
cv2.waitKey()
cv2.destroyAllWindows()

"""
import cv2
import numpy as np

src = cv2.imread('C:/image/Road-and-house.jpg', 0)

data = src.reshape((-1, 3)).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for K in range(3, 11):
    print('K:', K)
    ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)

    dst = center[label.flatten()]
    dst = dst.reshape((src.shape))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
"""

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/image/Road-and-house.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
"""