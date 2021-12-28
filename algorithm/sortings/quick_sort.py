def quick_sort(values):
    stack = [(0, len(values) - 1)]

    while stack:
        start, end = stack.pop()

        if end - start < 1:
            continue

        pivot = values[start]
        left = start + 1
        right = end

        while left <= right:
            for index in range(left, end + 1):
                if values[index] <= pivot:
                    left += 1
                else:
                    break

            for index in range(right, start, -1):
                if values[index] >= pivot:
                    right -= 1
                else:
                    break

            if left > right:
                values[start], values[right] = values[right], values[start]
            else:
                values[left], values[right] = values[right], values[left]

        stack.append((start, right - 1))
        stack.append((right + 1, end))

test = [5, 1, 2, 4, 8, 10]

quick_sort(test)