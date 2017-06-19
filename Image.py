#!/usr/bin/env python

import numpy
import cv2

img = cv2.imread("./image/image.jpg")
cv2.imshow("color", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
