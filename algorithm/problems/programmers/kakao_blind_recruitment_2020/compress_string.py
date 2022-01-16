from sys import maxsize


def solution(data):
    """
    카카오 블라인드 채용 2020 코딩테스트 문자열 압축 솔루션

    @Date: 2022/01/16
    @Author: Oh Donggeon
    @Link: https://programmers.co.kr/learn/courses/30/lessons/60057

    :param data: 압축 할 문자열
    :return: 최대로 압축 했을 때의 길이
    """
    answer = int(maxsize)

    for compress in range(1, int(len(data) / 2) + 1):  # 나누는 단위 (1, 2, 3...) 최대 길이의 반까지만 비교
        compress_data = ""
        index = compress
        count = 1
        buffer = data[:compress]  # 비교할 초기 값
        target = data[index:index + compress]  # data를 compress 크기만큼 건너 뛰면서 buffer 와 값 비교

        while target:
            target = data[index:index + compress]

            if buffer == target:
                count += 1
            else:
                if count > 1:
                    compress_data += str(count)

                compress_data += buffer
                buffer = target
                count = 1
            index += compress

        compress_data += str(count) if count > 1 else ""
        compress_data += target

        answer = len(compress_data) if len(compress_data) < answer else answer

    return answer if answer < len(data) else len(data)
