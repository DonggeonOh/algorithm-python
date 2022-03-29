def mock_test(answers):
    """
    프로그래머스 코딩테스트 고득점 Kit 완전탐색 - 모의고사 솔루션

    Author: Oh Donggeon
    Date: 2022/03/28
    Link: https://programmers.co.kr/learn/courses/30/lessons/42840

    :param answers: 문제의 답들
    :return: 가장 많이 맞춘 학생의 순서대로 출력 (같을 경우 오름차순으로 출력)
    """
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
