def selection_sort(values):
    for swapindex in range(len(values)):
        minindex = swapindex

        for targetindex in range(swapindex + 1, len(values)):
            if values[minindex] > values[targetindex]:
                minindex = targetindex

        values[minindex], values[swapindex] = values[swapindex], values[minindex]

    return values
