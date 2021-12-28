def insert_sort(values):
    for targetindex in range(1, len(values)):
        if values[targetindex] >= values[targetindex - 1]:
            print(values[targetindex])
            continue

        insertindex = targetindex

        for sortedindex in range(targetindex - 1, -1, -1):
            if values[sortedindex] > values[targetindex]:
                insertindex = sortedindex
            else:
                break

        values.insert(insertindex, values.pop(targetindex))
