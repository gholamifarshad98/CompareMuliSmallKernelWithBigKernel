from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm
class kernel:
    def __init__(self, numOfRow, numOfColumn, anchorLocationRow, anchorLocationCol,kernelType, unZeroIndex):
        self.numOfRowsOfKernel = numOfRow
        self.numOfColumnOfKernel = numOfColumn
        self.anchorLocationRow = anchorLocationRow
        self.anchorLocationCol = anchorLocationCol
        self.kernelType = kernelType
        self.unZeroIndex = unZeroIndex
        self.weightedKernel = np.zeros([self.numOfRowsOfKernel, self.numOfColumnOfKernel])
        self.createWeightedKernel()

    def createWeightedKernel(self):
        try:

            if self.kernelType == "row":
                for column in range(self.numOfColumnOfKernel):
                    self.weightedKernel[self.unZeroIndex][column] = 1
            elif self.kernelType == "column":
                for row in range(self.numOfRowsOfKernel):
                    self.weightedKernel[row][self.unZeroIndex] = 1
            elif self.kernelType == "rectangle":
                self.weightedKernel = np.ones([self.numOfRowsOfKernel,self.numOfColumnOfKernel])
            else:
                raise ValueError
        except ValueError:
                print("something wrong in definition of kernel. ")



    def calculateCostFunction(self, lefImage, rightImage, locationRow, locationCol, disparity):
        cost = 0
        for row in range(self.numOfRowsOfKernel):
            for col in range(self.numOfColumnOfKernel):
                cost = cost + self.weightedKernel[row][col]*pow((int(rightImage[row + locationRow - self.anchorLocationRow][
                                       col + locationCol - self.anchorLocationCol]) -
                                   int(lefImage[row + locationRow - self.anchorLocationRow][
                                       col + locationCol - self.anchorLocationCol + disparity])), 2)
        return cost

    def match(self,leftImage, rightImage, selectedDisparity):
        [numOfRows , numOfCols] = leftImage.shape
        result = np.zeros([numOfRows , numOfCols])
        for row in tqdm(range(self.anchorLocationRow,numOfRows-self.numOfRowsOfKernel+self.anchorLocationRow)):
            for col in range(self.anchorLocationCol,numOfCols-self.numOfColumnOfKernel+self.anchorLocationCol-selectedDisparity-1):
                costs=[]
                for disparity in range(selectedDisparity-1, selectedDisparity+2):
                    costs.append(self.calculateCostFunction(leftImage, rightImage, row, col, disparity))
                if costs[1]<costs[2] and costs[1]<costs[0]:
                    result[row][col] = 255
        # plt.imshow(result)
        # plt.show()
        return result

