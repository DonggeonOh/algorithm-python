def insert_sort(values):
    for targetindex in range(1, len(values)):
        for sortedindex in range(targetindex, 0, -1):
            if values[sortedindex] < values[sortedindex - 1]:
                values[sortedindex], values[sortedindex - 1] = values[sortedindex - 1], values[sortedindex]
            else:
                break
