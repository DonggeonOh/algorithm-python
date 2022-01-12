def solution(numbers, hand):
    """
    카카오 인턴십 2020 코딩 테스트 키패드 누르기 솔루션

    :param numbers: 누르는 키들의 정수 배열
    :param hand: 왼손잡이, 오른손잡이
    :return: 왼손으로 누르면 L, 오른손으로 누르면 R로 하여 키패드를 누른 손가락의 문자열 반환
    """
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ["*", 0, "#"]]
    left = [1, 4, 7]
    right = [3, 6, 9]
    left_pos = (3, 0)
    right_pos = (3, 2)
    answer = ''

    for number in numbers:
        if number in left:
            left_pos = get_position(keypad, number)
            answer += "L"

        elif number in right:
            right_pos = get_position(keypad, number)
            answer += "R"

        else:
            number_pos = get_position(keypad, number)
            left_distance = get_distance(left_pos, number_pos)
            right_distance = get_distance(right_pos, number_pos)

            if left_distance < right_distance:
                left_pos = number_pos
                answer += "L"

            elif left_distance > right_distance:
                right_pos = number_pos
                answer += "R"

            else:
                if hand == "left":
                    left_pos = number_pos
                    answer += "L"

                else:
                    right_pos = number_pos
                    answer += "R"

    return answer


def get_position(keypad, target):
    for row, numbers in enumerate(keypad):
        for col, number in enumerate(numbers):
            if number == target:
                return (row, col)


def get_distance(cur_pos, next_pos):
    return abs(cur_pos[0] - next_pos[0]) + abs(cur_pos[1] - next_pos[1])
