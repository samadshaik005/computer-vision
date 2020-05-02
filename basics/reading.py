import cv2
import numpy as np 


input = cv2.imread('./image_examples/elephant.jpg')


cv2.imshow('Test Elephant Image', input)


cv2.waitKey(0)

cv2.destroyAllWindows()