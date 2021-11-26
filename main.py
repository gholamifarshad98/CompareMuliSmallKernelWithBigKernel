from matplotlib import pyplot as plt
from kernel import kernel
from tqdm import tqdm
import numpy as np
import cv2


leftImage = cv2.imread('../cutSSDByPython/leftPic.png', 0)
rightImage = cv2.imread('../cutSSDByPython/rightPic.png', 0)
# leftImage = cv2.imread('/home/farshad/Desktop/drivingStereo_left/2018-07-09-16-11-56_2018-07-09-16-12-06-408.jpg', 0)
# rightImage = cv2.imread('/home/farshad/Desktop/drivingStereo_right/2018-07-09-16-11-56_2018-07-09-16-12-06-408.jpg', 0)
# leftImage = cv2.imread('/home/farshad/Desktop/crope/left.png', 0)
# rightImage = cv2.imread('/home/farshad/Desktop/crope/right.png', 0)
# leftImage = cv2.imread('/home/farshad/Desktop/myTestKittiDataSet/left/000040_11.png', 0)
# rightImage = cv2.imread('/home/farshad/Desktop/myTestKittiDataSet/right/000040_11.png', 0)


[numOfRows , numOfCols] = leftImage.shape
results = np.zeros([5, numOfRows , numOfCols])
result = np.zeros([numOfRows , numOfCols])

selectedDisparity = 10

for i in range(5):
    tempKernel = kernel(numOfRow=5, numOfColumn=5, anchorLocationRow=i, anchorLocationCol=2, kernelType="row", unZeroIndex= i)
    print(tempKernel.weightedKernel)
    results[i] = tempKernel.match(leftImage, rightImage, selectedDisparity)

#
# tempKernel = kernel(numOfRow=5, numOfColumn=5, anchorLocationRow=2, anchorLocationCol=2, kernelType="rectangle", unZeroIndex= 1)
# tempResult = tempKernel.match(leftImage, rightImage, selectedDisparity)

#
for row in tqdm(range(numOfRows)):
    for col in range(numOfCols):
        if  results[0][row][col] +results[1][row][col] + results[2][row][col] + results[3][row][col] + results[4][row][col] >4*255 :
            result[row][col] = 255
plt.imshow(result)
plt.show()
#
# #
# plt.imshow(tempResult)
# plt.show()
