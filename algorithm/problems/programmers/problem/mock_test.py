def mock_test(answers):
    students = [
        ([1, 2, 3, 4, 5], 5),
        ([2, 1, 2, 3, 2, 4, 2, 5], 8),
        ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 10)
    ]

    correct_dict = {0: 0, 1: 0, 2: 0}

    for answer_index, answer in enumerate(answers):
        for student_index, student in enumerate(students):
            index = answer_index % student[1]

            if student[0][index] == answer:
                correct_dict[student_index] += 1

    max_item = max(correct_dict.items(), key=lambda item: item[1])
    result = filter(lambda item: item[1] == max_item[1], correct_dict.items())

    return sorted(map(lambda item: item[0] + 1, result))