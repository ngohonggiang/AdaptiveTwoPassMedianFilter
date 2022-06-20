import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = numpy.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])
            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def difArr(data1, data2):
    e = numpy.subtract(data1, data2)
    for row in range(e.shape[0]):
        for col in range(e.shape[1]):
            if e[row][col] != 0:
                e[row][col] = 1
    return e


def avgNoiseRatio(data):
    return numpy.sum(data) / data.shape[1]


def noiseRatioCol(data, col):
    sigma = numpy.std(data[col])
    arr = numpy.sum(data, axis=1)
    ratio = arr[col] / data.shape[0]
    return ratio, sigma


def twoPass(data, filter_size, a, b):
    Y1 = median_filter(data, filter_size)
    E1 = difArr(data, Y1)

    Y2 = Y1
    anr = avgNoiseRatio(E1)
    for i in range(E1.shape[1]):
        ratio, sigma = noiseRatioCol(E1, i)
        n = a * sigma  # a=1

        if (ratio - anr) > n:
            e = numpy.subtract(data[:][i], Y1[:][i])
            K = round(ratio - anr + b * sigma)  # b=1
            v = numpy.transpose(numpy.reshape(e, K))
            for m in v:
                Y2[m][i] = data[m][i]
    E2 = difArr(Y1, Y2)

    Z = median_filter(Y2, filter_size)
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            if E2[row][col] == 1:
                Z[row][col] = data[row][col]
    return Z


def main():
    img = Image.open("noisyimg.png").convert("L")
    arr = numpy.array(img)

    # mf = median_filter(arr, 3)
    # img = Image.fromarray(mf)
    # img.show()

    tP = twoPass(arr, 3, 1, 1)
    img = Image.fromarray(tP)
    img.show()


main()
